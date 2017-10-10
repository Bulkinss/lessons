import requests
import json

r = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
json_string = r.text
parsed_string = json.loads(json_string)
print parsed_string
print parsed_string[0]['ccy']
print type(parsed_string[0]['sale'])

print 'You can find out the exchange rate for such currencies:'
print '- ' + parsed_string[2]['ccy']
print '- ' + parsed_string[0]['ccy']
print '- ' + parsed_string[1]['ccy']
parsed_string[0]['buy'] = float(parsed_string[0]['buy'])
parsed_string[0]['sale'] = float(parsed_string[0]['sale'])

while True:
    user_choice = raw_input('Enter the name of the currency: ')

    if user_choice == 'EUR':
        print 'Name of the currency: ' + user_choice
        print 'Buy: ' + str(parsed_string[0]['buy'])
        print 'Sale: ' + str(parsed_string[0]['sale']) + '\n'
        user_answer = raw_input('Do you want to buy or sell currency? ')
        if user_answer == 'Yes':
            print "- if you want to buy currency enter '1'"
            print "- if you want to sell currency enter '2'"
            user_answer_b_s = raw_input()
            if user_answer_b_s == '1':
                user_answer_b = int(raw_input('How much do you want to buy?'))
                print 'You`ll have to pay: ' + str(user_answer_b * parsed_string[0]['sale']) + ' UAH' + '\n'
            elif user_answer_b_s == '2':
                user_answer_s = int(raw_input('How much do you want to sell?'))
                print 'You`ll get: ' + str(user_answer_s * parsed_string[0]['buy']) + ' UAH' + '\n'
    elif user_choice == 'RUR':
        print 'Name of the currency: ' + user_choice
        print 'Buy: ' + parsed_string[1]['buy']
        print 'Sale: ' + parsed_string[1]['sale'] + '\n'
    elif user_choice == 'USD':
        print 'Name of the currency: ' + user_choice
        print 'Buy: ' + parsed_string[2]['buy']
        print 'Sale: ' + parsed_string[2]['sale'] + '\n'
    elif user_choice == 'exit':
        break
