# Leetcode Problem #1309: Decrypt String from Alphabet to Integer Mapping

# Description: You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows: Characters ('a' to 'i') are represented by ('1' to '9') respectively, Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. Return the string formed after mapping. The test cases are generated so that a unique mapping will always exist.

class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        for i, ch in enumerate(s):
            if ch != '#':
                res += chr(96+int(ch))
            else:
                res = res[:-2] + chr(96+int(s[i-2:i]))
        return res

s = Solution()

str1 = "10#11#12"
str2 = "1326#"

print('Result:',s.freqAlphabets(str1))
print('Result:',s.freqAlphabets(str2))

