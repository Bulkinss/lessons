from Tkinter import *
import mysql.connector
import config
import functions
#import ttk


def push_db():
    message = enter_message.get('1.0', END)
    enter_message.delete('1.0', END)
    cn = mysql.connector.connect(**config.config)
    cur = cn.cursor()

    if config.user == 1:
        data_message = (1, message, 0)
        first_ms_label['text'] = message
    else:
        data_message = (2, message, 0)
        second_ms_label['text'] = message

    add_message = ("INSERT INTO users (id_client, text, done) VALUES (%s, %s, %s)")
    cur.execute(add_message, data_message)
    cn.commit()
    cur.close()
    cn.close()


root = Tk()
root.title('Chat')
root.minsize(400, 500)
root.resizable(width=False, height=False)
root['bg'] = 'lavender'

enter_message = Text(root, height=4, width=30, font='Arial 14', wrap=WORD)
enter_message.place(x=1, y=405)

send_button = Button(root, text='Send', command=push_db, width=7, height=5, fg='black', font='arial 10').place(x=333, y=405)

your_name_label = Label(root, text='Roma: ', bg='lavender', fg='blue').place(x=5, y=10)
first_ms_label = Label(root, text='', bg='lavender')
first_ms_label.place(x=45, y=10)
collocutor_name_label = Label(root, text='Viktor: ', bg='lavender', fg='red').place(x=5, y=30)
second_ms_label = Label(root, text='', bg='lavender')
second_ms_label.place(x=45, y=30)

# functions.clear_insert(second_ms_label)

root.mainloop()

