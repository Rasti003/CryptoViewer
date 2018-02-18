import os

from _pydecimal import Decimal

from bittrex import bittrex


def percentage(a, b):
    return round(a / b * 100, 2)


def getLastPrice(currency):
    market = '{0}-{1}'.format(trade, currency)
    summary = api.getmarketsummary(market)
    price = summary[0]['Last']
    return price


# Get these from https://bittrex.com/Account/ManageApiKey

myCurrency = "NXT"
myPrice = 0.00004750
api = bittrex('key', 'secret')
trade = 'BTC'

currencyPrice = round(Decimal(getLastPrice(myCurrency)), 9)

print("Aktualna cena: ", myCurrency, currencyPrice, "BTC ", "To jest: ", percentage(getLastPrice(myCurrency), myPrice),
      "%", " ceny zakupu")

os.system('pause')
