"""The function combines two lists of different lengths
to create a dictionary."""
import itertools


def func():
    """Creates a dictionary from two lists."""
    key_lst = ['Maths', 'Literature', 'PE']
    val_lst = ['5', '3']
    if len(key_lst) > len(val_lst):
        my_dict = dict(itertools.zip_longest
                       (key_lst, val_lst, fillvalue=None))
    else:
        my_dict = dict(zip(key_lst, val_lst))
    print(my_dict)


func()
