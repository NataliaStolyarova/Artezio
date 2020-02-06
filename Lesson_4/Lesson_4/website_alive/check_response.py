"""This module checks if website is alive."""
import config
from make_request import func1


def get_url():
    """This function gets URL from User and make a request to a website."""
    func1()
    if config.r.status_code == 200:
        print("The website is alive")
    else:
        print("The website is not alive")
