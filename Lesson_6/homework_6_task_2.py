"""Generator returns all public attributes of the test class Foo"""


class SomeFoo:
    """Test class with attributes"""
    arg1 = None
    _arg2 = None
    __arg3 = None

    def __init__(self):
        super(SomeFoo, self)

    def some_bar(self):
        pass


def public_attr(SomeFoo):
    """Generator that filters public attributes"""
    print([arg for arg in dir(SomeFoo) if not arg.startswith('_')])


public_attr(SomeFoo)
