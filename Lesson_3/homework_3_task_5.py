"""Returns the closest to zero value from the list."""


def f(n=str):
    """Selects the value with the minimal modulus. """
    b = map(float, n.split())
    return min(b, key=abs)


print(f('1 2 -0.5 0.75 22'))
