k, n, w = map(int, input().split())
sol = (((k*w)*(w+1))//2) - n
print(sol if sol > 0 else 0)
