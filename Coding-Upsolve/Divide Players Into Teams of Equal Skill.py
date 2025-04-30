from fprintx import printx


def dividePlayers(skill):
    skill.sort()
    n = len(skill)
    l, r = 1, n-2
    chemistry = (skill[0] * skill[n-1])
    # print(chemistry)
    while l < r:
        # printx(l, r, skill[l], skill[r], l-1, r+1)
        if (skill[l - 1] + skill[r + 1]) == (skill[l] + skill[r]):
            chemistry += (skill[l] * skill[r])
        else:
            return -1
        l += 1
        r -= 1
    return chemistry





print(dividePlayers(skill = [3,2,5,1,3,4]))
print(dividePlayers(skill = [3,4]))
print(dividePlayers(skill = [1,1,2,3]))