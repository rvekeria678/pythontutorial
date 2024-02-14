# Leetcode Problem #58: Length of Last Word

# Description: Given a string, 's', consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthofLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[len(a)-1])

s = Solution()
sentence = 'Hello World'
sentence2 = '     fly me   to     the moon   '

print(s.lengthofLastWord(sentence))
print(s.lengthofLastWord(sentence2))