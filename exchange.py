# -*- coding: utf-8 -*-
from Tkinter import *
import commons
import functions


def handler():
    list1 = functions.return_request(commons.PB_URL)
    try:
        for item in list1:
            if item['ccy'] == selection():
                clear_insert([item['buy'], item['sale']])
    except Exception:
        pass


def clear_insert(values_list):
    output_label_buy = Label(root, text=round(float(values_list[0]), 2))
    output_label_buy.place(x=45, y=141)
    output_label_sale = Label(root, text=round(float(values_list[1]), 2))
    output_label_sale.place(x=45, y=171)


def selection():
    currency = listbox1.curselection()
    for item in currency:
        return listbox1.get(item)


root = Tk()
root.title('Currency exchange')
root.minsize(600, 400)
root.resizable(width=False, height=False)

first_label = Label(root, text='You can find out the exchange rate for next currencies:').place(x=5, y=5)
usd_label = Label(root, text='- USD').place(x=5, y=20)
eur_label = Label(root, text='- EUR').place(x=5, y=40)
rur_label = Label(root, text='- RUR').place(x=5, y=60)
btc_label = Label(root, text='- BTC').place(x=5, y=80)
enter_label = Label(root, text='Enter the name of the currency: ').place(x=5, y=100)
buy_label = Label(root, text='Buy: ').place(x=5, y=140)
sale_label = Label(root, text='Sale: ').place(x=5, y=170)
grn_label_buy = Label(root, text='UAH').place(x=100, y=141)
grn_label_sale = Label(root, text='UAH').place(x=100, y=171)
#main_edit = Entry(root, bg='lightblue', width=5)
#main_edit.place(x=205, y=100)
listbox1 = Listbox(root, height=5, width=15, selectmode=SINGLE)
listbox1.place(x=150, y=150)
listbox1.insert(1, 'USD')
listbox1.insert(2, 'EUR')
listbox1.insert(3, 'RUR')
listbox1.insert(4, 'BTC')


main_button = Button(root, text="Ok", command=handler).place(x=255, y=95)
root.mainloop()

