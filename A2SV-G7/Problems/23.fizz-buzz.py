def fizzBuzz(n):
    result = []
    for i in range(1, n+1):
        if not (i % 3) and not (i % 5):
            result.append("FizzBuzz")
        elif not (i % 3):
            result.append("Fizz")
        elif not (i % 5):
            result.append("Buzz")
        else: result.append(str(i))
    return result