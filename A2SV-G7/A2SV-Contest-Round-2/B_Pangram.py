len=int(input())
string=input().lower()
freq_list=[0 for _ in range(26)]
for s in string:
    freq_list[ord(s)-ord("a")]+=1
for i in freq_list:
    if i < 1:
        print("NO")
        break
else:
    print("YES")