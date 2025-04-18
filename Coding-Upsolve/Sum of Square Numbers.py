from fprintx import printx
from math import ceil


def judgeSquareSum(c: int) -> bool:
        for v in range(ceil(c**(0.5))):
            b = (c - (v*v)) ** (0.5)
            printx(v, b, v*v)
            if b == int(b):
                return True
        return False


# print(judgeSquareSum(5))    
# print(judgeSquareSum(3))
# print(judgeSquareSum(2))
# print(judgeSquareSum(8))
print(judgeSquareSum(0))