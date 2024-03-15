# Leetcode Problem #2351: First Letter to Appear Twice

# Description: Given a string s consisting of lowercase English letters, return the first letter to appear twice. (Note: A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b. s will contain at least one letter that appears twice.)

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}
        for character in s:
            if character in d:
                return character
            d[character] = ''

s = Solution()

str1 = "abccbaacz"
str2 = "abcdd"

print(s.repeatedCharacter(str1))
print(s.repeatedCharacter(str2))