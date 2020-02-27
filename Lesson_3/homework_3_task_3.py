"""Finding the maximum argument among all calls
and calculating the mean."""
import statistics


MAX_NUMBER = 0


def calc(first, second, third, fourth):
    """Returns the average meaning from the list
    and max argument."""
    my_list = [first, second, third, fourth]
    global MAX_NUMBER
    if max(my_list) > MAX_NUMBER:
        MAX_NUMBER = max(my_list)
    average = statistics.fmean(my_list)
    return average, MAX_NUMBER


print(calc(1, 2, 3, 4))
print(calc(-3, -2, 10, 1))
print(calc(7, 8, 8, 1))
