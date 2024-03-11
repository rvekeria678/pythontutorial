# Leetcode Problem #1047: Remove All Adjacent Duplicates in String

# Description: You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them. We repeatedly make duplicate removals on s until we no longer can. Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for character in s:
            if stack and character == stack[-1]:
                stack.pop()
            else:
                stack.append(character)
        return ''.join(stack)

s = Solution()

str1 = "abbaca"
str2 = "azxxzy"

print(s.removeDuplicates(str1))
print(s.removeDuplicates(str2))