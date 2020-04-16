import io

from reportlab.pdfgen import canvas

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import doctemplate, Paragraph, Frame, BaseDocTemplate, SimpleDocTemplate, PageTemplate, NextPageTemplate, Spacer
from reportlab.platypus.tables import Table, TableStyle

from reportlab.rl_config import defaultPageSize

def generatePdf(po_obj,po_lines):
    buffer = io.BytesIO()
    c=canvas.Canvas(buffer, pagesize=A4)

    PAGE_WIDTH=A4[0]
    PAGE_HEIGHT=A4[1]

    c.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-26, "Purchase Order")

    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']

    story = []
    elements = []

    buyerDetail = []

    p=Paragraph("This is just an example",styleN)
    aW = PAGE_WIDTH
    aH = PAGE_HEIGHT
    w,h = p.wrap(aW,aH)
    # print(w,h)

    # story.append(Paragraph("This is a Heading",styleH))
    # story.append(Paragraph("This is a Paragraph in Normal Style",styleN))
    line_description = Paragraph("Excavation of trench, pipe laying and backfilling in normal soil as per specifications",styleN)
    # print(line_description)
    data = [["Line","Description","Quantity","UoM","Unit Price","Total"],[1,line_description,"100","KM","155","15500"]]
    tData = [["Line","Description","Quantity","UoM","Unit Price","Total"],]

    for item in po_lines:
        line_description = Paragraph(item.order_item.item_description,styleN)
        # print(line_description)
        tData.append([item.po_line_number,line_description,
                        item.order_quantity,item.order_item.item_uom,
                        item.purchase_price,item.total_price])

    t=Table(tData,(2.0*cm,6*cm,2.5*cm,2*cm,3*cm,3*cm))
    w,h = t.wrap(aW,aH)

    elements.append(t)

    # buyerName = Paragraph()
    infoTableStyle = TableStyle(
                    [('LINEABOVE', (0,0), (-1,0), 1, colors.green),
                    ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                    ('LINEBELOW', (0,-1), (-1,-1), 1, colors.green),
                    ('ALIGN', (1,1), (-1,-1), 'LEFT')]
                    )

    buyerInfo = [["PO Number",po_obj.po_number],["PO Date",po_obj.po_date]]
    supplierInfo = [["Supplier Name",po_obj.po_supplier.supplier_name],
                    ["Supplier Address",po_obj.po_supplier.supplier_address+", "+po_obj.po_supplier.supplier_city],
                    ["Supplier NTN",po_obj.po_supplier.supplier_ntn_number],
                    ["Supplier Phone",po_obj.po_supplier.supplier_phone],
                    ["supplier_email",po_obj.po_supplier.supplier_email],
                    ]



    infoTable = Table(supplierInfo,(3.0*cm,6*cm),style=infoTableStyle)
    infoTable.hAlign = 'LEFT'
    story.append(infoTable)

    f1 = Frame(1*cm,23.7*cm,19*cm,5*cm,showBoundary=0)
    f2 = Frame(1*cm,10.7*cm,19*cm,12.5*cm,showBoundary=1)
    f1.addFromList(story,c)
    f2.addFromList(elements,c)

    buffer2 = io.BytesIO()
    Print_PO(buffer2, "Their address", po_lines, po_obj)
    buffer2.seek(0)

    c.save()
    buffer.seek(0)
    # print(tData)
    return buffer2

class Print_PO(BaseDocTemplate):
    def __init__(self, filename, their_adress, po_lines, po_obj, **kwargs):
        super().__init__(filename, page_size=A4,leftMargin=cm, rightMargin=cm, topMargin=cm, bottomMargin=cm,_pageBreakQuick=0, **kwargs)
        self.their_adress = their_adress
        self.objects = po_lines
        self.po_obj = po_obj

        self.page_width = (self.width + self.leftMargin * 2)
        self.page_height = (self.height + self.bottomMargin * 2)

        styles = getSampleStyleSheet()
        styleN = styles['Normal']

        # Setting up the frames, frames are use for dynamic content not fixed page elements
        supplierInfo = [["Supplier Name",po_obj.po_supplier.supplier_name],
                        ["Supplier Address",po_obj.po_supplier.supplier_address+", "+po_obj.po_supplier.supplier_city],
                        ["Supplier NTN",po_obj.po_supplier.supplier_ntn_number],
                        ["Supplier Phone",po_obj.po_supplier.supplier_phone],
                        ["Supplier Email",po_obj.po_supplier.supplier_email],
                        ]
        supplier_info_table = Table(supplierInfo,(3.0*cm,6*cm))
        info_table_w,info_table_h = supplier_info_table.wrap(0,0)
        # info_table = Frame(self.leftMargin,)
        first_page_table_frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id='small_table')
        later_pages_table_frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id='large_table')

        # Creating the page templates
        first_page = PageTemplate(id='FirstPage', frames=[first_page_table_frame], onPage=self.on_first_page)
        later_pages = PageTemplate(id='LaterPages', frames=[later_pages_table_frame], onPage=self.add_default_info)
        self.addPageTemplates([first_page, later_pages])

        # Tell Reportlab to use the other template on the later pages,
        # by the default the first template that was added is used for the first page.
        story = [NextPageTemplate(['*', 'LaterPages'])]

        table_grid = [["Line","Description","Quantity","UoM","Unit Price","Total"],]

        # Add the objects
        for item in po_lines:
            line_description = Paragraph(item.order_item.item_description,styleN)
            table_grid.append([item.po_line_number,line_description,
                            item.order_quantity,item.order_item.item_uom,
                            item.purchase_price,item.total_price])

        item_table = Table(table_grid, repeatRows=1, colWidths=(2.0*cm,6.1*cm,2.5*cm,2*cm,3*cm,3*cm),
                           style=TableStyle([('GRID',(0,1),(-1,-1),0.25,colors.gray),
                                             ('BOX', (0,0), (-1,-1), 1.0, colors.black),
                                             ('BOX', (0,0), (-1,0), 1.0, colors.black),
                                             ('ALIGN', (2,1), (2,-1), 'RIGHT'),
                                             ('ALIGN', (3,0),(3,-1), 'CENTER'),
                                             ('ALIGN', (4,1),(5,-1), 'RIGHT'),
                                             ]))

        calculation_data = [["Total Amount",po_obj.po_amount],
                            ["Tax",po_obj.po_tax_amount],
                            ["Total (inc Tax)","Value"]]
        calculation_table = Table(calculation_data, colWidths=(3*cm,3*cm),
                            style=TableStyle([('GRID',(0,0),(-1,-1),0.25,colors.gray),
                                              ('BOX', (0,0), (-1,-1), 1.0, colors.black),
                                              ('ALIGN', (1,0), (-1,-1), 'RIGHT'),
                                              ]))

        calculation_table.hAlign = 'RIGHT'
        # story.append(supplier_info_table)
        # story.append(Spacer(1,0.25*cm))
        story.append(item_table)
        story.append(Spacer(1,0.25*cm))
        story.append(calculation_table)
        self.build(story)

    def on_first_page(self, canvas, doc):
        canvas.saveState()
        # Add the logo and other default stuff
        self.add_default_info(canvas, doc)

        supplierInfo = [["Supplier Name",self.po_obj.po_supplier.supplier_name],
                        ["Supplier Address",self.po_obj.po_supplier.supplier_address+", "+po_obj.po_supplier.supplier_city],
                        ["Supplier NTN",self.po_obj.po_supplier.supplier_ntn_number],
                        ["Supplier Phone",self.po_obj.po_supplier.supplier_phone],
                        ["Supplier Email",self.po_obj.po_supplier.supplier_email],
                        ]
        supplier_info_table = Table(supplierInfo,(3.0*cm,6*cm))
        info_table_w,info_table_h = supplier_info_table.wrap(0,0)
        supplier_info_table.drawOn(canvas,self.leftMargin,doc.height-(info_table_h+0.5*cm))

        canvas.drawString(doc.leftMargin, doc.height, "My address")
        canvas.drawString(0.5 * doc.page_width, doc.height, self.their_adress)

        canvas.restoreState()

    def add_default_info(self, canvas, doc):
        canvas.saveState()
        canvas.drawCentredString(0.5 * (doc.page_width), doc.page_height - 1 * cm, "Amanullah Khan & Co (Pvt) Ltd")

        canvas.restoreState()

# if __name__ == '__main__':
#     ShippingListReport('example.pdf', "Their address", ["Product", "Product"] * 50)

def printpo2pdf(po_obj, po_lines):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer,pagesize=A4)
    po_num = "PO Number: "+po_obj.po_number
    po_date = "Date: "+ str(po_obj.po_date)
    su_name = "Supplier: "+ po_obj.po_supplier.supplier_name
    su_add = "Address: "+po_obj.po_supplier.supplier_address+", "+po_obj.po_supplier.supplier_city
    su_phone = "Phone: "+po_obj.po_supplier.supplier_phone
    su_email = "Email: "+po_obj.po_supplier.supplier_email

    xSize = 21.0
    ySize = 29.7

    textobject = p.beginText()
    textobject.setTextOrigin(1.27*cm, (ySize-1.27)*cm)
    textobject.setFont("Helvetica",12)
    textobject.textOut("Purchase Order")
    textobject.moveCursor(8*cm,0)
    textobject.textOut(po_num)
    p.line(1.27*cm,28.25*cm,19.73*cm,28.25*cm)
    p.drawText(textobject)
    # p.drawString(255,800,po_num)
    # p.line(35,797,565,797)
    textobject = p.beginText()
    textobject.setTextOrigin(1.27*cm,(ySize-2.54)*cm)
    textobject.setFont("Helvetica",10)
    textobject.textLine(su_name)
    textobject.textLine(po_date)
    textobject.textLine(su_add)
    textobject.textLine()
    textobject.textLine(su_phone)
    textobject.textLine(su_email)
    p.drawText(textobject)

    data = [["S.no","Line Number","Line Description","Quantity","UoM","Unit Price","Total"],[1,1,"Excavation of trench, pipe laying and backfilling in normal soil as per specifications","100","KM","155","15500"]]
    t=Table(data)
    t.wrapOn(p,460,100)
    t.drawOn(p,1.27*cm,(ySize-6)*cm)

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

def get_col_heads(caller):
    caller_fields = caller._meta.fields
    field_list = []
    human_rdable_list =[]
    for fields in caller_fields:
        column_head = (str(fields)).split(".")
        human_rdable_name = column_head[-1].replace("_"," ").title()
        human_rdable_list.append(human_rdable_name)
        field_list.append(column_head[-1])
    field_list = field_list[1:-2]
    human_rdable_list = human_rdable_list[1:-2]
    field_dct = tuple(zip(field_list,human_rdable_list))
    return field_dct
