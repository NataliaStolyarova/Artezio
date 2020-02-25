"""Getting the size of the web-page."""
import requests


def len_counter():
    """Counts symbols of web-page."""
    resp = requests.get('https://google.com')
    print(len(resp.text))


len_counter()
