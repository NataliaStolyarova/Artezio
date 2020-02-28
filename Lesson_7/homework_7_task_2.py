"""The decorator measures the running time of class methods."""
from time import sleep, time


def calc(function):
    """Measures the running time."""
    def wrapper(*args, **kwargs):
        current_time = time()
        function(*args, **kwargs)
        print(f'Время работы метода {function.__name__}:'
              f' {(time() - current_time)*1000} ms')
    return wrapper


def time_methods(*method_name):
    """Sets attributes and passes an object
    to the calc function."""
    def class_obj(obj):
        def wrapper(*args, **kwargs):
            for name in method_name:
                if hasattr(obj, name):
                    setattr(obj, name, calc(getattr(obj, name)))
            return obj(*args, **kwargs)

        return wrapper
    return class_obj


@time_methods('inspect')
class Spam:
    """The class decorated by decorator."""

    def __init__(self, s):
        self.s = s

    def inspect(self):
        sleep(self.s)

    def func(self):
        return self.s


A = Spam(2)
A.inspect()
A.func()
