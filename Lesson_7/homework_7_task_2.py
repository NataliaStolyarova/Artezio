"""The decorator measures the running time of class methods."""
from time import sleep, time


def time_methods(method_name):
    """The decorator measures the running time
    of class methods."""

    def wrapper(self, *args, **kwargs):
        current_time = time()
        method_name(self, *args, **kwargs)
        print(f'Время работы метода {method_name.__name__}:'
              f' {time() - current_time}')

    return wrapper


class Spam:
    """The class decorated by decorator."""

    def __init__(self, sec):
        self.sec = sec

    def __call__(self):
        return self

    @time_methods
    def inspect(self):
        sleep(self.sec)

    def func(self):
        return self.sec


A = Spam(2)
A.inspect()
A.func()
