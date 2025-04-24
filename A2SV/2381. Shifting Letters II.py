from fprintx import printx


def shiftingLetters(s, shifts):
    n = len(s)
    difference_array = [0] * (n+1)
    result = []
    for shift in shifts:
        difference_array[shift[0]] += shift[2] if shift[2] == 1 else -1
        # if shift[1] + 1 < (n+1):
        difference_array[shift[1] + 1] += -(shift[2] if shift[2] == 1 else -1)
    printx(difference_array)
    current_shift_sum = 0
    for i in range(n):
        current_shift_sum += difference_array[i]
        result.append(    chr((((current_shift_sum + ord(s[i])) - ord('a')) % 26  + ord('a')) )    )
        printx(current_shift_sum, s[i], ord(s[i]), chr((((current_shift_sum + ord(s[i])) - ord('a')) % 26  + ord('a')) ), (((current_shift_sum + ord(s[i])) - ord('a')) % 26  + ord('a')) , widths=[6])
    return "".join(result)


# print(shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]))
# print(shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]]))
print(shiftingLetters(s = "iaozjb", shifts = [[0,4,0],
                                              [0,2,1],
                                              [1,3,1],
                                              [0,4,1],
                                              [4,4,1],
                                              [2,3,0],
                                              [5,5,0],
                                              [3,3,0],
                                              [2,3,0],
                                              [5,5,1],
                                              [5,5,1],
                                              [5,5,0]]))