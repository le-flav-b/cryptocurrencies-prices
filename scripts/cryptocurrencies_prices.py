import requests
import json
from datetime import date
from threading import Thread
from scripts.loading_window import LoadingWindow


ALL_CRYPTOS = ['BTC', 'ETH', 'XRP', 'LTC', 'SHIB']
ALL_PHYSICAL = ['USD', 'EUR', 'JPY', 'GBP']

CRYPTOCURRENCIES_SYMBOLS = {
    'USD': '$',
    'EUR': '€',
    'JPY': '¥',
    'GBP': '£'
}


actual_prices = {}
crypto_currencies_prices = {}
# ex: {
#   'BTC':{
#      'USD': [153, 156, 120, 178, 164],
#      'EUR': [140, 141, 108, 160, 148]
#   },
#   'ETH':{
#      'USD': [15, 15, 12, 18, 16],
#      'EUR': [14, 14, 11, 16, 15]
#   }
# }


def get_crypto_prices(crypto: str, physical_currency: str, limit: int = 364, one_value: bool = True) -> list:
    """Return the list of the last 2000 average values between the high and the low of a day

    Parameters
    ----------
    crypto : str
    physical_currency : str
    limit: int [optional]
    one_value: bool [optional]

    Returns
    -------
    list
    """
    url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=' \
          f'{crypto}&tsym={physical_currency}&limit={limit}'

    # check if the crypto is the Shiba because this last was created less than a year ago
    if crypto == 'SHIB':
        nb_values = (date.today() - date(day=30, month=9, year=2021)).days
        url = url.replace('364', str(nb_values if nb_values < 364 else 364))

    answer = requests.get(url)
    tab_json = json.loads(answer.text)

    # return a list of float if we ask for the graph or a list of list of float if it's for the day info
    if one_value:
        return [round(day['high'] + day['low'] / 2, 6) for day in tab_json['Data']['Data']]

    return [[round(day['open'], 6), round(day['close'], 6), round(day['low'], 6), round(day['high'], 6)]
            for day in tab_json['Data']['Data']]


def get_actual_prices(crypto: str) -> dict:
    """Return the the dict of the actual price of [crypto] in USD, EUR, JPY, and GBP

    Parameters
    ----------
    crypto : str

    Returns
    -------
    dict
    """
    url = f'https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms=BTC,ETH,XRP,LTC,SHIB,USD,EUR,JPY,GBP'
    answer = requests.get(url)
    tab_json = json.loads(answer.text)

    return tab_json


# create the loading window with the number of actions to do with the API in args
loading_window = LoadingWindow(len(ALL_CRYPTOS) * len(ALL_PHYSICAL) + len(ALL_CRYPTOS) + len(ALL_PHYSICAL))


def collect_the_data() -> None:
    """Collects all data on the API and interacts with the loading window
    """

    global crypto_currencies_prices
    global actual_prices

    # generation of the values of the different cryptos in the different physical
    for cryptocurrency in ALL_CRYPTOS:

        crypto_currencies_prices[cryptocurrency] = {}

        for physical in ALL_PHYSICAL:

            crypto_currencies_prices[cryptocurrency][physical] = get_crypto_prices(cryptocurrency, physical)
            loading_window.increment()

    # generation of the actual values of the different currencies in all the different currencies
    for currency in ALL_CRYPTOS + ALL_PHYSICAL:

        actual_prices[currency] = get_actual_prices(currency)
        loading_window.increment()


# create a new thread to do the collect of the data and show it on the loading window at the same time
process = Thread(target=collect_the_data)
process.start()

# generate the loading window
loading_window.run()
