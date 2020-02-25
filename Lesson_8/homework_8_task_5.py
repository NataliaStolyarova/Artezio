"""Checks if password contains all required characters
and avoids unwanted ones."""
import re


def password_check():
    """Checks if the password meets the criteria."""
    match = re.findall(r'[a-zA-Z0-9]{1,}[_*%&]{0,}', r'*a&b_c12%3_')
    print('The password is correct' if match else 'It is incorrect')


password_check()
