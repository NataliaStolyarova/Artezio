"""This module makes a request to a website."""
import requests
import config


def func1():
    """This function makes a request to a website and returns an object r."""
    r = requests.get(config.a)
    return r
