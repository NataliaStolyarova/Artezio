"""Decorator checks if arguments in function match to annotation."""


def accepts(*types):
    """Decorator to verify arguments and return types."""
    def check_accepts(function):
        assert len(types) == function.__code__.co_argcount

        def new_f(*args, **kwargs):
            for (argum, tp_a) in zip(args, types):
                if not isinstance(argum, tp_a):
                    print("arg %r does not match %s" % (argum, tp_a))
                elif len(args) != len(types):
                    raise AssertionError
                else:
                    function(*args, **kwargs)
        new_f.__name__ = function.__name__
        return new_f
    return check_accepts


@accepts(int, float)
def func(arg1='int', arg2='float'):
    """Function with annotation
    which must be checked."""
    print(arg1*arg2)


func(3, 2.0)
func(3.0, '2')
