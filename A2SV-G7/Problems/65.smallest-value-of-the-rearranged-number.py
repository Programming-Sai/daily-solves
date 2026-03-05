def smallestNumber(num: int) -> int:
    neg_sign = num < 0
    num = (str(num))
    if neg_sign:
        num = sorted(num[1:], reverse=True)
        return -1 * (int("".join(num)))
    else:
        num = sorted(num)
        if num[0] == "0":
            for i in range(len(num)):
                if int(num[i]) > 0:
                    num[i], num[0] = num[0], num[i]
                    break
        return int("".join(num))
