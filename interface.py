# -*- coding: utf-8 -*-
from Tkinter import *
#mport tkinter.ttk as ttk
#import wgrs

root = Tk()

root.title('WGRS Web Testing')
# root.overrideredirect(True)
root.geometry('1000x800+450+150') # ширина=500, высота=400, x=300, y=200
root.resizable(False, False)

def make_start_button():
    start_button = Button(root, text="Start", borderwidth=3, width=6, height=1, fg='black', font='arial 14', command=show_result)
    start_button.place(x=150, y=650)
    # start_button.bind('<Button-1>', show_result)

def make_result_windows():
    font_text_field = 'Arial 11'
    font_label_field = 'Arial 10'
    time_text_field = Text(root, height=43, width=7, font=font_text_field, wrap=WORD)
    time_text_field.place(x=400, y=40)
    time_text_label = Label(root, height=1, width=5, text= "Time", font=font_label_field)
    time_text_label.place(x=404, y=15)

    realm_text_field = Text(root, height=43, width=14, font=font_text_field)
    realm_text_field.place(x=459, y=40)
    realm_text_label = Label(root, height=1, width=5, text= "Realm", font=font_label_field)
    realm_text_label.place(x=485, y=15)

    url_text_field = Text(root, height=43, width=30, font=font_text_field)
    url_text_field.place(x=565, y=40)
    url_text_label = Label(root, height=1, width=5, text="Url", font=font_label_field)
    url_text_label.place(x=650, y=15)

    status_text_field = Text(root, height=43, width=7, font=font_text_field)
    status_text_field.place(x=783, y=40)
    status_text_label = Label(root, height=1, width=5, text="Status", font=font_label_field)
    status_text_label.place(x=785, y=15)

    return time_text_field, realm_text_field, url_text_field, status_text_field

'''def show_result():
    text_result_window = make_result_windows()
    returning_text = wgrs.test_ping_pong()
    for returning_text_item in returning_text:
        text_result_window[0].tag_configure('time', justify='center')
        text_result_window[1].tag_configure('realm', justify='center')
        text_result_window[3].tag_configure('status', justify='center', foreground='red' if returning_text_item[3] != 'ok' else 'black')
        text_result_window[0].insert('1.0', returning_text_item[0] + '\n', ('time'))
        text_result_window[1].insert('1.0', returning_text_item[1] + '\n', ('realm'))
        text_result_window[2].insert('1.0', returning_text_item[2] + '\n')
        text_result_window[3].insert('1.0', returning_text_item[3] + '\n', ('status'))'''


make_start_button()
make_result_windows()
root.mainloop()

