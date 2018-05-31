def fizz_numbers(value):
    result = []
    for v in value:
        if v % 3 == 0 and  v % 5 == 0:
            result.append('ThreeFive')
        elif v % 3 == 0:
            result.append('Three')
        elif v % 5 == 0:
            result.append('Five')
        else:
            result.append(v)

    return result
