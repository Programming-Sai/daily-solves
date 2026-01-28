k, n, w = map(int, input().split())
actual_price = ((k*w)*(w+1))//2
borrow_amt = actual_price - n
if n < actual_price:
    print(borrow_amt)
else:
    print(0)