from fprintx import printx

def check(n, a):
    a.sort()
    number_of_negatives = i = 0
    while a[i] < 0:
        number_of_negatives += 1
        i+=1
    print(a, number_of_negatives)


n = int(input())
a = list(map(int, input().split()))
print(check(n, a))