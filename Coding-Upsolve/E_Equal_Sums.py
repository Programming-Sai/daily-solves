def check(sk):
    sum_map = {} 

    for i, seq in enumerate(sk):
        total_sum = sum(seq)
        
        for j, num in enumerate(seq):
            new_sum = total_sum - num
            
            if new_sum in sum_map:
                prev_i, prev_j = sum_map[new_sum]
                if prev_i != i:
                    print("YES")
                    print(prev_i + 1, prev_j + 1) 
                    print(i + 1, j + 1)
                    return
            
            sum_map[new_sum] = (i, j)
    
    print("NO")



k=int(input())
sk = []
for _ in range(k):
    n=int(input())
    s=list(map(int, input().split()))
    sk.append(s)
check(sk)
 