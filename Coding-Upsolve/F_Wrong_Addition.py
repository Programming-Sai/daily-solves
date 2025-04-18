def solve(a_str, s_str):
    
    result = []
    i = len(a_str) - 1
    j = len(s_str) - 1

    while j >= 0:
        digit_s = int(s_str[j])
        if i >= 0:
            digit_a = int(a_str[i])
            if digit_s >= digit_a:
                digit_b = digit_s - digit_a
                result.append(str(digit_b))
                i -= 1
                j -= 1
            elif j > 0:
                two_digits_s = int(s_str[j-1] + s[j])
                if two_digits_s >= digit_a and two_digits_s <= 19:
                    digit_b = two_digits_s - digit_a
                    result.append(str(digit_b))
                    i -= 1
                    j -= 2
                else:
                    print(-1)
                    return
            else:
                print(-1)
                return
        else:
            result.append(s_str[j])
            j -= 1

    if i >= 0:
        print(-1)
        return

    b_str = "".join(result[::-1])
    if not b_str:
        print(-1)
        return

    # if len(b_str) > 1 and b_str[0] == '0':
    #     print(-1)
    #     return

    print(int(b_str))


t = int(input())
for _ in range(t):
    a, s = input().split()
    solve(a, s)

