n = int(input())
for _ in range(n):
    word = input()
    len_of_word = len(word)
    if len_of_word <= 10:
        print(word)
    else:
        print(word[0]+str(len_of_word - 2)+word[-1])