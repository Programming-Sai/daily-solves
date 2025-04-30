from fprintx import printx


def maxArea(height):
    result = 0
    n = len(height)
    l, r = 0, n-1

    while l < r:
        result = max(result, ((r-l) * (min(height[l], height[r]))))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return result



# print(maxArea(height = [1,8,6,2,5,4,8,3,7]))
print(maxArea( height = [1,1]))