# Leetcode Problem 1221: Split a String in Balanced Strings

# Description: Balanced strings are those that have an equal quantity of 'L' and 'R' characters. Given a balanced string s, split it into some number of substrings such that: Each substring is balanced. Return the maximum number of balanced strings you can obtain.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        prev, weight, count = 0, 1, 0
        for i in range(1, len(s)):
            prev = i if prev < 0 else prev
            if prev != i:
                weight = weight + 1 if s[prev] == s[i] else weight - 1
            if not weight:
                count += 1
                prev = -1
                weight = 1
        return count

s = Solution()

str1 = "RLRRLLRLRL"
str2 = "RLRRRLLRLL"
str3 = "LLLLRRRR"

print(s.balancedStringSplit(str1))
print(s.balancedStringSplit(str2))
print(s.balancedStringSplit(str3))
