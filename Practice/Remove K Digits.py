from fprintx import printx


def check(nums: str, k: int) -> str:
    """
    Given a string `num` representing a non-negative integer, remove `k` digits 
    from the number so that the new number is the smallest possible.

    Return the result as a string. Leading zeros are allowed but the final result 
    should not have any unnecessary leading zeros (i.e., return "0" instead of "0000").

    Constraints:
    - 1 <= len(num) <= 10⁵
    - 0 <= k < len(num)
    """
    if k == len(nums): return "0"
    stack = []
    for num in nums:
        while stack and k and stack[-1] > num:
            # printx(stack, num, k)
            stack.pop()
            k -= 1
        stack.append(num)
    return str(int("".join(stack)))



print(check("1432219", 3))  # Expected: "1219"
print(check("10200", 1))    # Expected: "200"
print(check("10", 2))       # Expected: "0"

print(check("1234567890", 9))  # Expected: "0" (remove everything except smallest)
print(check("9", 1))           # Expected: "0" (remove only digit)
print(check("123456", 2))           # Expected: "0" (remove only digit)
