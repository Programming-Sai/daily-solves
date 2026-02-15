def findRestaurant(list1, list2):
    map1 = {x:i for i, x in enumerate(list1)}
    map2 = {x:i for i, x in enumerate(list2)}
    commons = []
    result = []
    min_common=float("inf")
    for s in list1:
        if s in map2:
            commons.append((s, map1[s] + map2[s]))
            min_common = min(min_common, map1[s] + map2[s])
    print(map1, map2, commons, min_common)
    for common, common_sum in commons:
        if common_sum <= min_common:
            result.append(common)
    return result
        
