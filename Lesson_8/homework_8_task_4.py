"""The function compares the string
with the format YYYY-MM-DDThh:mm:ss±hh:mm"""
import re


def matching():
    """Checks if the string matches the pattern."""
    match = re.fullmatch(r'[0-2][0-9]{3}(-[0-1][0-9])'
                         r'(-[0-3][0-9])T([0-2][0-9])'
                         r'(:[0-5][0-9]){2}[-+][0-2][0-9]'
                         r'(:[0-5][0-9])', r'2005-08-09T18:31:42+03:30')
    print('YES' if match else 'NO')


matching()
