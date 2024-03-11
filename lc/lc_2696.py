# Leetcode Problem #2696: Minimum String Length After Removing Substrings

# Description: You are given a string s consisting only of uppercase English letters. You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s. Return the minimum possible length of the resulting string that you can obtain. Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for character in s:
            if stack and ((character == 'B' and stack[-1] == 'A') or (character == 'D' and stack[-1] == 'C')):
                stack.pop()
            else:
                stack.append(character)

        return len(stack)

s = Solution()

str1 = "ABFCACDB"
str2 = "ACBBD"

print(s.minLength(str1))
print(s.minLength(str2))