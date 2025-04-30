from fprintx import printx

def  check3(perm, n):
    left, right, max_item, min_item = 0, n-1, n, 1

    while left <= right:
        printx(left, right, min_item, max_item)
        if perm[left] == max_item:
            left += 1
            max_item -= 1
        elif perm[left] == min_item:
            left += 1
            min_item += 1
        elif perm[right] == max_item:
            right -= 1
            max_item -= 1
        elif perm[right] == min_item:
            right -= 1
            min_item += 1
        else: break
    if left > right:
        print("-1")
    else:
        print(left + 1, right + 1)


n=6
a=[2, 3, 6, 5, 4, 1]
check3(a, n)
        


# t=int(input())
# for _ in range(t):
#     n = int(input())
#     permutation=list(map(int, input().split()))
#     check3(permutation, n)