# -*- coding: utf-8 -*-
from Tkinter import *
import requests
import json


def clear_insert(*values_list):
    output_buy.delete("0.0", "end")
    output_buy.insert("0.0", values_list[0])
    output_sale.delete("0.0", "end")
    output_sale.insert("0.0", values_list[1])


def handler():
    values_list = []
    name_of_currency = str(main_edit.get())
    if name_of_currency == 'EUR':
        values_list.append(str(parsed_string[0]['buy']))
        values_list.append(str(parsed_string[0]['sale']))
        clear_insert(values_list)
    elif name_of_currency == 'USD':
        values_list.append(str(parsed_string[2]['buy']))
        values_list.append(str(parsed_string[2]['sale']))
        clear_insert(values_list)
    elif name_of_currency == 'RUR':
        values_list.append(str(parsed_string[1]['buy']))
        values_list.append(str(parsed_string[1]['sale']))
        clear_insert(values_list)


r = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
json_string = r.text
parsed_string = json.loads(json_string)

root = Tk()
root.title('Currency exchange')
root.minsize(600, 400)
root.resizable(width=False, height=False)

first_label = Label(root, text='You can find out the exchange rate for such currencies:').place(x=5, y=5)
usd_label = Label(root, text='- USD').place(x=5, y=20)
eur_label = Label(root, text='- EUR').place(x=5, y=40)
rur_label = Label(root, text='- RUR').place(x=5, y=60)
enter_label = Label(root, text='Enter the name of the currency: ').place(x=5, y=80)
buy_label = Label(root, text='Buy: ').place(x=5, y=120)
sale_label = Label(root, text='Sale: ').place(x=5, y=150)
grn_label_buy = Label(root, text='грн.').place(x=90, y=120)
grn_label_sale = Label(root, text='грн.').place(x=90, y=150)
main_edit = Entry(root, bg='lightblue', width=5)
main_edit.place(x=180, y=82)

main_button = Button(root, text="Calculate", command=handler).place(x=220, y=78)
output_buy = Text(root, bg="lightblue", font="Arial 10", width=5, height=1)
output_buy.place(x=45, y=122)
output_sale = Text(root, bg="lightblue", font="Arial 10", width=5, height=1)
output_sale.place(x=45, y=152)
#output_sale = Text(frame, bg="lightblue", font="Arial 10", width=5, height=1)

root.mainloop()
