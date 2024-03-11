# Leetcode Problem #1544: Make the String Great

# Description: Given a string s of lower and upper case English letters. A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where: 0 <= i <= s.length - 2, s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa. To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good. Return the string after making it good. The answer is guaranteed to be unique under the given constraints. Notice that an empty string is also good.

class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            if result and s[i] != result[-1] and (s[i].upper() == result[-1] or s[i].lower() == result[-1]):
                result.pop()
            else:
                result.append(s[i])
        return ''.join(result)

s = Solution()

str1 = "leEeetcode"
str2 = "abBAcC"
str3 = "s"

print(s.makeGood(str1))
print(s.makeGood(str2))
print(s.makeGood(str3))

