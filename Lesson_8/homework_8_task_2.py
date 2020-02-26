"""Real time currency converter."""
import requests


def convert(source_am=float(input("Amount of source currency: ")),
            source_cur=str(input("Source currency: ")),
            target_cur=str(input("Target currency: "))) -> float:
    """Receives quantity and currency and
    converts according to the exchange rate."""
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    rate = data['rates']
    if target_cur and source_cur in rate:
        target_am = (rate[target_cur]/rate[source_cur])*source_am
        print(f'{source_am} {source_cur} is {target_am} {target_cur}')


convert()
