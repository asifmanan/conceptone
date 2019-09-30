def get_col_heads(cu):
    all_fields = cu._meta.fields
    all_field_list = []
    for fields in all_fields:
        column_head = (str(fields)).split(".")
        # print(column_head[-1])
        all_field_list.append(column_head[-1])
        field_list = all_field_list[1:-2]
        field_dct = tuple(zip(field_list,field_list))
    return field_dct
