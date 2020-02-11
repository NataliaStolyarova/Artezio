"""Iterator returns elements from even positions in list."""


class EvenIterator:
    """Receive a list of elements."""
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(0, len(self.lst), 2):
            print(self.lst[i])


MY_LST = [1, 2, 3, 4, 5, 6]
MY_IT = EvenIterator(MY_LST)
print(next(MY_IT))
