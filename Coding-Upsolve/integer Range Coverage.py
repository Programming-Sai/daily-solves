# def isCovered(ranges, left, right):
#     for i in ranges:
#         if all(x in range(left, right+1) for x in range(*i)):
#             re



def isCovered(ranges, left, right):
    new = set()
    for i in ranges:
        new.update(range(i[0], i[1]+1))
    return set(range(left, right+1)).issubset(new)
        




ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5

print(isCovered(ranges, left, right))

