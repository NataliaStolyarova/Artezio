"""Test divides numbers and detect errors during execution"""

for t in range(int(input("Number of test cases: "))):
    try:
        a, b = map(int, input("Enter a and b: ").split())
        print(a // b)
    except ZeroDivisionError:
        print("Error Code")
    except ValueError:
        print("Error Code")
