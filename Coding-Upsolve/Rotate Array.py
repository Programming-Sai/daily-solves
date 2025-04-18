from fprintx import printx


def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    for _ in range(1, k+1):
        j = len(nums)-1
        # print("---")
        while j - 1 >= 0:
            # if j-1 < 0:
                # break
            # printx(nums[j], nums[j-1], j, j-1, )
            nums[j] , nums[j - 1] = nums[j - 1], nums[j]
            # printx(nums[j], nums[j-1], j, j-1, )
            j -= 1



def rotate(nums, k):
    k %= len(nums)

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    n = len(nums)
    reverse(0, n - 1)       # Reverse entire array
    reverse(0, k - 1)       # Reverse first k elements
    reverse(k, n - 1)       # Reverse rest

            
    
# nums = [1,2,3,4,5,6,7]
# k = 3

# nums = [-1,-100,3,99]
# k = 2

nums = [1,2,3]
k = 6

nums = [1, 2, 3, 4, 5]
k = 100003

rotate(nums, k)

print(nums)