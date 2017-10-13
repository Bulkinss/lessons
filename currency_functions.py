def clear_insert(values_list, output_buy, output_sale):
    output_buy.delete("0.0", "end")
    output_buy.insert("0.0", values_list[0])
    output_sale.delete("0.0", "end")
    output_sale.insert("0.0", values_list[1])


def handler(main_edit, parsed_string):
    values_list = []
    name_of_currency = str(main_edit.get())
    if name_of_currency == 'EUR':
        values_list.append(str(parsed_string[0]['buy']))
        values_list.append(str(parsed_string[0]['sale']))
        #clear_insert(values_list)
    elif name_of_currency == 'USD':
        values_list.append(str(parsed_string[2]['buy']))
        values_list.append(str(parsed_string[2]['sale']))
        #clear_insert(values_list)
    elif name_of_currency == 'RUR':
        values_list.append(str(parsed_string[1]['buy']))
        values_list.append(str(parsed_string[1]['sale']))
    return values_list
