from fprintx import printx


def numberOfSubarrays(nums, k):
    l = r = current_count = result = 0
    n = len(nums)
    while r < n:
        print(nums[l:r+1])
        if nums[r] % 2 != 0:
            current_count += 1
        while current_count >= k:
            if current_count == k:
                print(nums[l])
                result += (r-l+1)  # We found a valid subarray
            if nums[l] % 2 != 0:
                current_count -= 1  # Shrink the window from the left
            l += 1  # Move left pointer to shrink the window

        r += 1 

    return result
            


print(numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
# print(numberOfSubarrays(nums = [2,4,6], k = 1))
# print(numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))