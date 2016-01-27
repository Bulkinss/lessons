__author__ = 'v_sypko'
import requests, datetime, config, MySQLdb

def get_currency(currency, action):
    """
    Example: get_currency('USD', 'sell')
    :param currency: USD, EUR
    :param action: buy, sell
    :return: USD sell: value
    """

    today_currency = requests.Session().get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    for x in today_currency.json():
        # print x
        if (x['ccy'] == currency) and (action == 'sell'):
            return '%s sell: %s' % (currency, x['sale'][:-3])
        if (x['ccy'] == currency) and (action == 'buy'):
            return '%s buy: %s' % (currency, x['buy'][:-3])

        if (x['ccy'] == currency and action == 'sell'):
            return '%s sell: %s' % (currency, x['sale'][:-3])
        if (x['ccy'] == currency and action == 'buy'):
            return '%s buy: %s' % (currency, x['buy'][:-3])

def day_now():
    return str((datetime.datetime.now()))[:-16]

def write_to_db():
    db = MySQLdb.connect(host=config.HOST , user=config.USER, passwd=config.PASSWORD, db=config.NAME)
    cursor = db.cursor()
    sql = "SELECT * FROM %s WHERE id = %s" % ('collect', 1)
    cursor.execute(sql)
    results = cursor.fetchall()
    # db.commit()
    print results

print write_to_db()




