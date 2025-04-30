def countPrimes(n: int) -> int:
        if n == 0: return n
        bool_arr = [True] * (n+1)
        bool_arr[0], bool_arr[1] = False, False
        for i in range(2, int( n**0.5)+1):
            if bool_arr[i]:
                for j in range(i**2, len(bool_arr), i):
                    bool_arr[j] = False   
        print(bool_arr[:-1])    
        return(bool_arr[:-1].count(True))

print(countPrimes(3))

# n=int(input())
# print(countPrimes(n))