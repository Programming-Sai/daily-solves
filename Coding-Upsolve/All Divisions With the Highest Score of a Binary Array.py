from fprintx import printx

def maxScoreIndices(nums):
    score_indices = []
    res = []
    count_ones = nums.count(1)
    max_score = count_ones
    current_ones_count = 0
    current_zeros_count = 0
    total_ones_count = 0
    

    score_indices.append(max_score)

    for i in range(len(nums)):
        # if i == 0:    
            # continue
        if nums[i] == 0:
            current_zeros_count += 1
        else:
            current_ones_count += 1
            
        
        total_ones_count = count_ones - current_ones_count
        max_score = max(max_score, (current_zeros_count + total_ones_count))
        score_indices.append((current_zeros_count + total_ones_count))

        # printx(i, max_score, nums[:i], nums[i:], current_zeros_count, total_ones_count, widths=[len(nums)*5])


   

    for i in range(len(score_indices)):
        if score_indices[i] == max_score:
            res.append(i)

    return res



print(maxScoreIndices(nums = [0,0,1,0]))
print(maxScoreIndices(nums = [0,0,0]))
print(maxScoreIndices(nums = [1,1]))