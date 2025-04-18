from collections import Counter

def counter(d):
    count = Counter(d)
    highest_frequency = count.most_common()[0]
    highest_frequency_count = highest_frequency[1]
    highest_frequency_value = highest_frequency[0]


    if highest_frequency_count >= 3:
        print(highest_frequency_value)
    else:
        print(-1)




t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    counter(arr)
    