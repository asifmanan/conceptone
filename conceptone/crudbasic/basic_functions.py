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
