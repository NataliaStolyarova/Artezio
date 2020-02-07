"""Inheritance between classes"""


class Observable:
    """Base class receiving kwargs"""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__,
                           (', '.join('%s=%s' % (key, val) for (key, val)
                                      in iter(self.__dict__.items()) if not
                                      key.startswith('_'))))


class NewClass(Observable):
    """Child class of the base class"""


X = NewClass(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print(X)
