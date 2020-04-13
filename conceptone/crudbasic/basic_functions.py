import io

from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import doctemplate, Paragraph, Frame
from reportlab.platypus.tables import Table

def generatePdf():
    buffer = io.BytesIO()
    c=canvas.Canvas(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']

    story = []

    story.append(Paragraph("This is a Heading",styleH))
    story.append(Paragraph("This is a Paragraph in Normal Style",styleN))

    data = [["S.no","Line Number","Line Description","Quantity","UoM","Unit Price","Total"],[1,1,"Excavation of trench, pipe laying and backfilling in normal soil as per specifications","100","KM","155","15500"]]
    t=Table(data)

    f = Frame(1*cm,24.7*cm,18*cm,5*cm,showBoundary=1)
    f.addFromList(story,c)
    c.save()
    buffer.seek(0)
    return buffer

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
