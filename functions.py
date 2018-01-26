import mysql.connector
import config


def clear_insert(ms_label):
    cn = mysql.connector.connect(**config.config)
    cur = cn.cursor()

    pull_message = ("SELECT text FROM users WHERE id=10")
    cur.execute(pull_message)

    ms_label['text'] = cur.fetchone()

    cur.close()
    cn.close()


# def handler():
#     message = main.enter_message.get('1.0', END)
