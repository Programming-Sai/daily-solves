from fprintx import printx


def minimumRemoval(beans):
    beans.sort()
    total_bean_sum = sum(beans)
    # print(total_bean_sum)
    min_removal = float('inf')
    n = len(beans)
    for i in range(n):
        # printx(min_removal, (total_bean_sum - (n - i) * beans[i]))
        min_removal = min(min_removal, (total_bean_sum - (n - i) * beans[i]))
    return min_removal


print(minimumRemoval(beans = [4,1,6,5]))
print(minimumRemoval(beans = [2,10,3,2]))