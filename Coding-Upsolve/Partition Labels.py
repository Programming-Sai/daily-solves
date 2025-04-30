from fprintx import printx

def partitionLabels(s):
    n = len(s)
    # print(max(s))
    intermediate_result = [0]
    result = []
    length = (ord(max(s)) - ord('a'))+1

    # last_seen = ([0] * 26)
    last_seen = ([-1] * length)
    for i in range(n):
        last_seen[ord(s[i]) - ord('a')] = i

    # last_seen.sort(key=)

    
    # last_seen[:] = [0, 8, 7, 3, 5]
    # print(last_seen)

    # for i in range(length - 1):
    #     if last_seen[i+1] == -1:
    #         continue
    #     if last_seen[i] > intermediate_result[-1]:
    #         intermediate_result.append(last_seen[i])
    # print(intermediate_result)


    # result.append(intermediate_result[0] + 1)
    # for i in range(1, len(intermediate_result)):
    #     # temp = intermediate_result[i-1]
    #     result.append(intermediate_result[i] - intermediate_result[i-1])
    #     # print(result[i-1], result[i])d;fldlfdf;l

    start_index = 0
    while start_index < n:
        current_index = start_index
        ending_index = last_seen[ord(s[current_index]) - ord('a')]
        while current_index < ending_index:
            ending_index = max(ending_index, last_seen[ord(s[current_index]) - ord('a')])
            current_index += 1
        result.append(ending_index - start_index + 1)
        start_index = ending_index + 1
    return (result)


print(partitionLabels(s = "ababcbacadefegdehijhklij"))
# print(partitionLabels(s = "eccbbbbdec"))
# print(partitionLabels(s = "caedbdedda"))