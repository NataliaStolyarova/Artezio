"""Generator that iterates arguments in series.
The number of arguments is random."""
import itertools

FIRST_ARG = iter([1, 2, 3])
SECOND_ARG = iter([4, 5])


def chain(*args):
    """Returns arguments in series."""
    while True:
        arg_chain = itertools.chain(*args)
        yield next(arg_chain)


EL = chain(FIRST_ARG, SECOND_ARG)

print(next(EL))
print(next(EL))
print(next(EL))
print(next(EL))
print(next(EL))
