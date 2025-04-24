from fprintx import printx


def checkInclusion(s1, s2):
        m = len(s1)
        n = len(s2)
        s1_counter = [0] * 26
        s2_counter = [0] * 26

        for s in s1:
            s1_counter[ord(s) - ord('a')] += 1

        l = 0
        r = m-1

        for i in range(l, r+1):
            s2_counter[ord(s2[i]) - ord('a')] += 1
        
        # print(s1_counter, s2_counter, l, r, s2[l:r+1])
        

        while r < n-1:
            
            
            if s1_counter == s2_counter:
                return True
            s2_counter[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            # if r + 1 < n:
            s2_counter[ord(s2[r]) - ord('a')] += 1
            
            # print(s1_counter, s2_counter, l, r, s2[l:r+1])
            
        return s1_counter == s2_counter





print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))
print(checkInclusion(s1 = "ab", s2 = "eidboaoo"))
print(checkInclusion(s1 = "a", s2 = "ab"))
print(checkInclusion(s1 = "adc", s2 = "dcda"))