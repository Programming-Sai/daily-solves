class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        l, r, n, vowel_set, count = 0, 0, len(word), {'a', 'e', 'i', 'o', 'u'}, 0
        while l < n:
            seen = set()
            r = l
            while r < n:
                if word[r] not in vowel_set:
                    break
                seen.add(word[r])
                if len(seen) == 5:
                    count += 1
                r += 1
            l += 1
        return count