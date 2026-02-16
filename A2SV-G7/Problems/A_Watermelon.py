w=int(input())
for i in range(1, w+1):
    if i % 2 == 0 and (w-i) % 2 == 0:
        print("YES")
        break
else:
    print("NO")