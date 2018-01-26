# -*- coding: utf-8 -*-
from Tkinter import *
import commons
import functions
import ttk


def handler():
    parsed_string = functions.return_request(commons.PB_URL)
    try:
        for item in parsed_string:
            if item['ccy'] == selection():
                clear_insert([item['buy'], item['sale']])
    except Exception:
        pass


def clear_insert(values_list):
    output_label_buy['text'] = round(float(values_list[0]), 2)
    output_label_sale['text'] = round(float(values_list[1]), 2)


def selection():
    return Currency_combobox.get()


root = Tk()
root.title('Currency exchange')
root.minsize(400, 200)
root.resizable(width=False, height=False)

first_label = Label(root, text='You can find out the exchange rate for next currencies:').place(x=5, y=5)
usd_label = Label(root, text='- USD').place(x=5, y=20)
eur_label = Label(root, text='- EUR').place(x=5, y=40)
rur_label = Label(root, text='- RUR').place(x=5, y=60)
btc_label = Label(root, text='- BTC').place(x=5, y=80)
enter_label = Label(root, text='Select currency: ').place(x=5, y=105)
buy_label = Label(root, text='Buy: ').place(x=5, y=141)
sale_label = Label(root, text='Sale: ').place(x=5, y=171)
grn_label_buy = Label(root, text='UAH').place(x=100, y=141)
grn_label_sale = Label(root, text='UAH').place(x=100, y=171)
output_label_buy = Label(root, text='')
output_label_buy.place(x=45, y=141)
output_label_sale = Label(root, text='')
output_label_sale.place(x=45, y=171)


main_button = Button(root, text="Ok", command=handler).place(x=250, y=102)
Currency_combobox = ttk.Combobox(root,values = [u"USD",u"EUR",u"RUR",u"BTC"],height=4)
Currency_combobox.set(u"USD")
Currency_combobox.place(x=100, y=105)
root.mainloop()

