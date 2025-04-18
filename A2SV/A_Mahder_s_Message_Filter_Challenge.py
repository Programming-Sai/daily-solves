def determine_correctness(s, n):
    # First we should determine th enumber of trailing ')'
    count=0
    for i in s[-1::-1]:
        if i == ")":
            count += 1
        else:
            break
    # Next we compute the count of the remaining characters
    remaining_count=n-count
    # Finally we do the comparison for count strictly greater than the remaining count
    if count > remaining_count:
        return 'Yes'
    return 'No'


t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    print(determine_correctness(s, n))



