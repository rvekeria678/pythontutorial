# Leetcode Problem #2135: Count Asterisks

# Description: You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth. Return the number of '*' in s, excluding the '*' between each pair of '|'. Note that each '|' will belong to exactly one pair.

class Solution:
    def countAsterisks(self, s: str) -> int:
        b_count, a_count = 0, 0
        for char in s:
            if char == '|':
                b_count += 1
            if b_count % 2 == 0 and char == '*':
                a_count += 1
        return a_count

s = Solution()

str1 = "l|*e*et|c**o|*de|"
str2 = "iamprogrammer"
str3 = "yo|uar|e**|b|e***au|tifu|l"

print(s.countAsterisks(str1))
print(s.countAsterisks(str2))
print(s.countAsterisks(str3))