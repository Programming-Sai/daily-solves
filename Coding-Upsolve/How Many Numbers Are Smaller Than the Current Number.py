def smallerNumbersThanCurrent(nums):
    sort_counter = [0] * ( max(nums) + 1)
    output = []
    prefix_sum = [0] * len(sort_counter)


    # Implementing Counting Sort
    for num in nums:
        sort_counter[num] += 1
    print(sort_counter)
    prefix_sum[0] = sort_counter[0]

    # Performing PRefix Sum
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i-1] + sort_counter[i]
    print(prefix_sum)

    # Getting counts per prefix
    for num in nums:
        output.append(prefix_sum[num-1] if num != 0 else 0)

    return(output)



# print(smallerNumbersThanCurrent(nums = [8,1,2,2,3]))
# print(smallerNumbersThanCurrent(nums = [6,5,4,8]))
# print(smallerNumbersThanCurrent(nums = [7,7,7,7]))
print(smallerNumbersThanCurrent(nums = [5,0,10,0,10,6]))
