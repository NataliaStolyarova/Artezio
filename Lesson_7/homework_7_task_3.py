"""Currying of function with a finite number
of positional arguments with the help of decorator."""


def carry(function):
    """The function makes currying."""

    def dec_1(first_arg):
        def dec_2(second_arg):
            def dec_3(third_arg):
                def dec_4(fourth_arg):
                    print(first_arg + second_arg +
                          third_arg + fourth_arg)
                    return function

                return dec_4

            return dec_3

        return dec_2

    return dec_1


@carry
def given_func(arg_1, arg_2, arg_3, arg_4):
    """The function to curry."""
    return arg_1 + arg_2 + arg_3 + arg_4


given_func(1)(2)(3)(4)
