"""Function that returns cycle iterator."""


def cycle():
    """Returns elements cyclically"""
    my_lst = ['a', 'b', 'c']
    while True:
        for element in my_lst:
            yield element


ELEMENTS = cycle()

print(next(ELEMENTS))
print(next(ELEMENTS))
print(next(ELEMENTS))
print(next(ELEMENTS))
