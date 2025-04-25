from fprintx import printx


def productExceptSelf(nums):
    first_prefix_product = [1]
    prefix = 1
    for i in range(len(nums)):
        if i == len(nums)-1: break
        first_prefix_product.append(prefix * nums[i])
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums)-2, -1, -1):
        # print(i, i-1, i+1)
        suffix *= nums[i+1]
        first_prefix_product[i] *= suffix
    return(first_prefix_product)



print(productExceptSelf(nums = [1,2,3,4]))
print(productExceptSelf(nums = [-1,1,0,-3,3]))