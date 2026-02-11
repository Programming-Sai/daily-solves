
n = int(input())
phone_book = {}
for _ in range(n):
    entry = input().split(" ")
    phone_book[entry[0]] = entry[1]
    
while True:
    try:
        name = input()
        print(f"{name}={phone_book[name]}" if name in phone_book else "Not found")
    except EOFError:
        break
# print(phone_book)