# Leetcode Problem #3083: Existence of Substring in a String and Its Reverse

# Description: Given a string s, find any substring of length 2 which is also present in the reverse of s Return true if such a substring exists, and false otherwise.

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        left = 0
        right = 2
        size = len(s)
        rs = s[::-1]
        while left < size - 1:
            if s[left:right] in rs:
                return True
            left += 1
            right += 1
        return False
    
s = Solution()

st = "leetcode"
print(s.isSubstringPresent(st))

st = "abcba"
print(s.isSubstringPresent(st))

st = "abcd"
print(s.isSubstringPresent(st))
