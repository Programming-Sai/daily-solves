from fprintx import printx

# def arrayManipulation(n, queries):
    # result = [0] * n
    # for query in queries:
        # result[query[0]-1 : query[1]] = [query[2] + m for m in result[query[0]-1 : query[1]]]
        # printx(query, query[0]-1, query[1], query[2], result, widths=[5])
    # return max(result)



def arrayManipulation(n, queries):
    difference_array = [0] * (n+1)
    # printx(difference_array)


    for q in queries:
        # printx(q)
        difference_array[q[0]] += q[2]
        if q[1] + 1 < len(difference_array):
            difference_array[q[1] + 1] += -q[2]


    # printx(difference_array)
    for i in range(1, len(difference_array)):
        difference_array[i] += difference_array[i - 1]
    # printx(difference_array, max(difference_array))


    return max(difference_array[1:])





n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

n = 5
queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
print(arrayManipulation(n, queries))