"""The function returns the sum
and product of arbitrary arguments."""


def sum_and_mul(*args, **kwargs):
    """Creates combined list of arguments
    for summation and multiplication."""
    total_lst = []
    lst_of_args = list(args)
    lst_of_args.extend(dict(kwargs).values())

    def flatten(array):
        for item in array:
            if isinstance(item, (list, tuple)):
                try:
                    flatten(item)
                except RecursionError:
                    print('Cyclic reference was found')
                    total_lst.clear()
                    return None
            else:
                total_lst.append(item)
        return total_lst
    if flatten(lst_of_args):
        if 0 in total_lst:
            total_lst.remove(0)
        total_sum = sum(total_lst)
        total_mul = 1
        for element in total_lst:
            total_mul *= element
        return total_sum, total_mul
    return None


ARR = (3, 4, [5, 6, [7, 8], []])
ARR[2][3].append(ARR)
print(sum_and_mul(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=ARR))

