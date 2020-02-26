import re


match = re.findall(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[\w\d*%&]{8,12}', r'*A&b_c12%3_')


