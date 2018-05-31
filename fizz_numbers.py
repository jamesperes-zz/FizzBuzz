def fizz_numbers(value):
    result = []
    for v in value:
        if v % 3 == 0:
            result.append('Three')
        else:
            result.append(v)

    return result
