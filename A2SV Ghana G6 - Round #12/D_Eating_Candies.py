from fprintx import printx


def check(n, w):
    l, r, max_len, a_eat, b_eat, a_count, b_count = 0 , n-1, 0, 0, 0, 0, 0
    while (l<=r):
        if a_eat+w[l] == b_eat and l:
            a_eat += w[l]
            max_len+=1
            l+=1
            # continue
        elif a_eat == b_eat+w[r] and l:
            b_eat += w[r]
            max_len += 1
            r -=1
            # continue
        elif a_eat+w[l] == b_eat+w[r] and l:
            a_eat += w[l]
            b_eat += w[r]
            max_len+=2
        l+=1
        r-=1


        

#         # printx(b_eat, b_count, r, w[r], max_len)
#         b_eat += w[r]
#         b_count+=1
#         r -= 1
#         if a_eat == b_eat:
#             max_len = max(max_len, (a_count+b_count))
# # printx(a_eat, a_count, l, w[l], max_len)
#         a_eat += w[l]
#         a_count+=1
#         l += 1
#         if a_eat == b_eat:
#             max_len = max(max_len, (a_count+b_count))


        
        # print("---")
    
    return max_len

n = 9
w = [7, 3, 20, 5, 15, 1, 11, 8, 10]
# print(check(n, w))


t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    print(check(n, w))