from fprintx import printx




def check(nums, k):
    l = r = length = s_sum = 0
    n = len(nums)
    while r < n:
        s_sum += nums[r]
        while l < n and s_sum > k:
            s_sum -= nums[l]
            l += 1
        length = max(length, r - l + 1)
        r += 1
    return length


print(check(nums = [1, 2, 3, 4, 5], k = 8 ))
print(check(nums = [5, 1, 1, 1, 1, 1, 5], k = 7))
print(check(nums = [10, 20, 30], k = 5 ))