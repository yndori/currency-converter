import requests

def convert(base_curency,target_currency,amount):
    '''This function convert an amount from a currency to another fetching real-time data from https://frankfurter.dev/'''
    params = {
        'base' : base_curency
    }

    response = requests.get(url='https://api.frankfurter.dev/v2/rates', params=params ,timeout=5)
    if response.status_code == 200:
        raw_data = response.json()
        formated_data = {item['quote']:item['rate'] for item in raw_data}
        converted_amount = amount*formated_data[target_currency]
        print(f'{amount} {params['base']} = {converted_amount}{target_currency}')
    else:
        print('Error : currency not found.')
