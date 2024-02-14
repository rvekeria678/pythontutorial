# Leetcode Problem #28: Find the Index of the First Occurence in a String

# Description: Given two strings 'needle' and 'haystack', return the index of the first occurence of 'needle', or -1 of 'needle' is not part of 'haystack'

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if (haystack[i:i + len(needle)] == needle):
                return i
        return -1

s = Solution()

haystack = 'daybreak'
needle = 'break'

print(s.strStr(haystack=haystack,needle=needle))