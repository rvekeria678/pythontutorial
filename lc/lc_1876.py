# Leetcode Problem #1876: Substrings of Size Three with Distinct Characters

# Description: A string is good if there are no repeated characters. Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​. Note that if there are multiple occurrences of the same substring, every occurrence should be counted. A substring is a contiguous sequence of characters in a string.

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = 0
        right = 2
        count = 0
        while right < len(s):
            if len(s[left:right+1]) == len(set(s[left:right+1])):
                count += 1
            left += 1
            right += 1
        return count
    
s = Solution()    

str1 = "xyzzaz"
str2 = "aababcabc"

print(s.countGoodSubstrings(str1))
print(s.countGoodSubstrings(str2))
