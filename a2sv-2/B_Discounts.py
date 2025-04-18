
def split_maxes(arr, m):
    arr.sort()
    return arr[::-1][:m], arr[::-1][m:]

def sum_max_minus_last_max(max_arr):
    return sum(max_arr[:-1])

def sum_remaining(rem_arr):
    return sum(rem_arr)

def final_sum(max_arr_sum, rem_arr_sum):
    return max_arr_sum + rem_arr_sum


n=int(input())
a=list(map(int, input().split()))
m=int(input())
q=list(map(int, input().split()))
for x in q:
    print(final_sum(sum_max_minus_last_max(split_maxes(a, x)[0]), sum_remaining(split_maxes(a, x)[1])))





# print(split_maxes([7, 1, 3, 1, 4, 10, 8], 4))
# print(sum_max_minus_last_max([10, 8, 7, 4]))
# print(sum_remaining([3, 1, 1]))
# m=3
# print(final_sum(sum_max_minus_last_max(split_maxes([7, 1, 3, 1, 4, 10, 8], m)[0]), sum_remaining(split_maxes([7, 1, 3, 1, 4, 10, 8], m)[1])))




