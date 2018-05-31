def fizz_numbers(list_values):
    """Do a FizzBuzz with numbers where multiples of three change to "Three"
    instead of the number and for the multiples of five change to "Five" and
    for numbers which are multiples of both three and five change to
    "ThreeFive".

    Keyword arguments:
    list_values -- list containing only numbers

    Return:
    list containing str and int
    """
    result = []
    for v in list_values:
        if v % 15 == 0:
            result.append('ThreeFive')
        elif v % 3 == 0:
            result.append('Three')
        elif v % 5 == 0:
            result.append('Five')
        else:
            result.append(v)

    return result


if __name__ == '__main__':
    print(fizz_numbers(range(1,101)))
