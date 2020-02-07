"""Three functions, which transform the given list in their own way."""


my_list = [1, 2, 3, 4, 4, 5, 6]


def func1(my_list):
    """This function squares all elements from the list."""
    new_list = []
    for i in my_list:
        new_list.append(i**2)
    return new_list


print(func1(my_list))


def func2(my_list):
    """This function returns elements standing on even positions."""
    for element in range(1, len(my_list), 2):
        print(my_list[element])


func2(my_list)


def func3(my_list):
    """This function takes even elements from uneven positions
    and raises them to a cubic degree."""
    for number in range(0, len(my_list), 2):
        if my_list[number] % 2 == 0:
            result = my_list[number] ** 3
            print(result)


func3(my_list)
