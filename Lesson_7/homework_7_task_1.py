"""Returns average working time of function among n calls."""
from time import sleep, time


def my_decorator(n_calls):
    """Remembers the previous results and calculates
    the average meaning of n calls."""

    def average_time(function):
        how_much = []

        def wrapper(*args, **kwargs):
            current_time = time()
            function(*args, **kwargs)
            res = (time() - current_time) * 1000
            how_much.append(res)
            if len(how_much) < n_calls:
                print(f'Среднее время работы: {res} ms')
            else:
                print(f'Среднее время работы: '
                      f'{sum(how_much[-n_calls:]) / n_calls} ms')

        return wrapper

    return average_time


@my_decorator(2)
def my_func(sec):
    """Sleeps a few seconds."""
    sleep(sec)
    return sec


my_func(3)
my_func(7)
my_func(1)
my_func(8)
