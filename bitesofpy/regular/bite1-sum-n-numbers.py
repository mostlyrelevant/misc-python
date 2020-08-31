""" Write a function that can sum up numbers:

    * It should receive a list of n numbers.
    * If no argument is provided, return sum of numbers 1..100.
    * Look closely to the type of the function's default argument ...

    Have fun!"""

# numbers = range(1,100)


def sum_numbers(numbers=None):
    pass

    # my code
    if numbers is None:
        numbers = range(1,100)

    return sum(numbers)
