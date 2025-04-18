def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify numss1 in-place instead.
    """
    if m == 0 and nums2:
        nums1[0] = nums2[0]
        # print(nums1, nums2)
        return
    result = []
    l, r = 0, 0
    while l < len(nums1) and r < len(nums2):
        if nums1[r] < nums2[l]:
            result.append(nums1[r])
            r+=1
        else:
            result.append(nums2[l])
            l += 1
    end1 = nums1[r:]
    end2 = nums2[l:]
    print(end1, end2, result)
    if len(set(end1)) > 1 or (len(set(end1)) == 1 and 0 not in set(end1)):
        result.extend(end1)
    if len(set(end2)) > 1 or (len(set(end2)) == 1 and 0 not in set(end2)): 
        result.extend(end2)
    for i in range(len(result)):
        nums1[i] = result[i]   



# print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
# print(merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(merge(nums1 = [0], m = 0, nums2 = [1], n = 1))