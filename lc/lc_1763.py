# Leetcode Problem #1763: Longest Nice Substring

# Description: A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not. Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        bank = {}

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                uppercaseletters = ''.join(list(set(sorted(char.lower() for char in s[i:j+1] if char.isupper()))))
                lowercaseletters = ''.join(list(set(sorted(char for char in s[i:j+1] if char.islower()))))
            
                if uppercaseletters == lowercaseletters:
                    bank[i] = s[i:j+1]

        bank = dict(sorted(bank.items()))
        ans = ''
        for i in bank:
            if len(ans) < len(bank[i]):
                ans = bank[i]
        return ans

s = Solution()

st = "YazaAay"
print(s.longestNiceSubstring(st))

st = "Bb"
print(s.longestNiceSubstring(st))

st = "c"
print(s.longestNiceSubstring(st))
