from fprintx import printx

def check(n, l):
    total_sum = sum(l)
    result = []
    for i in range(n):
        if (total_sum - l[i]) % (n-1) == 0 and l[i] == ((total_sum - l[i]) //(n - 1)):
            result.append(i+1)
            # printx(l[i], i, (total_sum - l[i]), (n - 1), ((total_sum - l[i]) //(n - 1)))
    # print(len(result), result)
    print(len(result))
    print(*result)
    

n=int(input())
l=list(map(int, input().split()))
check(n, l)

# n=5
# l=[1, 2, 3, 4, 5]
# n=4
# l = [50, 50, 50, 50]

# check(n, l)

