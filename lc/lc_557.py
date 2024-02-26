# Leetcode Problem #557: Reverse Words in a String III

# Description: Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        rs = []
        for i in s:
            rs.append(i[::-1])
        return ' '.join(rs)

s = Solution()

str1 = "Let's take LeetCode contest"
str2 = "Mr Ding"

print(s.reverseWords(str1))
print(s.reverseWords(str2))