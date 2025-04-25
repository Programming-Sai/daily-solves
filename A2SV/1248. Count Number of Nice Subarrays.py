from collections import defaultdict
from itertools import accumulate
from fprintx import printx


def numberOfSubarrays(nums, k):
    l = r = odd_count = subarr_count = 0
    odd_stack = []
    # next_odd = 0
    n = len(nums)
    while r < n:
        if nums[r] % 2 != 0:
            odd_stack.append(r)
            # odd_count += 1cls

        if len(odd_stack) == k:
            first_odd = odd_stack[0]
            subarr_count += (first_odd - l + 1)

        if len(odd_stack) > k:
            l = odd_stack.pop(0) + 1


        # printx(nums[l:r+1], odd_count, l, r, next_odd, subarr_count, odd_stack, widths=[27])
        r += 1
    return subarr_count
    # nums[:] = [0 if i%2==0 else 1 for i in nums]
    # prefix_nums = list(accumulate(nums))
    # prefix_seen_before = defaultdict(int)
    # prefix_seen_before[0] += 1
    # # print(nums, prefix_nums, dict(prefix_seen_before))

    # l = r = odd_count = subarr_count = 0
    # n = len(nums)
    # while r < n:
    #     odd_count
            

def numberOfSubarrays(nums, k):
    l = r = subarr_count = 0
    odd_stack = []
    n = len(nums)

    while r < n:
        if nums[r] % 2 != 0:
            odd_stack.append(r)

        if len(odd_stack) == k:
            first_odd = odd_stack[0]
            next_odd = odd_stack[1] if len(odd_stack) > 1 else r + 1

            left_choices = first_odd - l + 1
            right_choices = 1  # Will extend as far right as the next odd
            while r + 1 < n and nums[r + 1] % 2 == 0:
                r += 1
                right_choices += 1

            subarr_count += (left_choices+1) * (right_choices+1)

        if len(odd_stack) > k:
            l = odd_stack.pop(0) + 1
        r += 1

    return subarr_count





def numberOfSubarrays(nums, k):
    n = len(nums)
    odd_indices = [-1]  # Sentinel for easier math
    for i, num in enumerate(nums):
        if num % 2!=0:
            odd_indices.append(i)
    odd_indices.append(n)  # Sentinel for end
    print(odd_indices)

    subarr_count = 0
    for i in range(1, len(odd_indices) - k):
        left_count = odd_indices[i] - odd_indices[i - 1]
        right_count = odd_indices[i + k] - odd_indices[i + k - 1]
        subarr_count += left_count * right_count

    return subarr_count




print(numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
# print(numberOfSubarrays(nums = [2,4,6], k = 1))
# print(numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))