from fprintx import printx

def check(n, a):
    # try:
        a.sort()
        number_of_negatives = i = 0
        while i < n and a[i] < 0:
            # if a[i] == -1:
                # continue
            number_of_negatives += 1
            i+=1
        
        has_zero = 0 in set(a)

        if number_of_negatives % 2:
            if not has_zero:
                number_of_negatives -= 1
        result = 0
        for i in range(n):
            if i < number_of_negatives:
                result += (-(a[i]))-1
            else:
                result += abs(1-a[i])
        return result
    # except Exception as e:
        # return str(e)



n = int(input())
a = list(map(int, input().split()))
print(check(n, a))