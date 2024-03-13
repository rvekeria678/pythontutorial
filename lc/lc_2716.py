# Leetcode Problem #2716: Minimize String Length

# Description: Given a 0-indexed string s, repeatedly perform the following operation any number of times: Choose an index i in the string, and let c be the character in position i. Delete the closest occurrence of c to the left of i (if any) and the closest occurrence of c to the right of i (if any). Your task is to minimize the length of s by performing the above operation any number of times. Return an integer denoting the length of the minimized string.

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(char for char in s))
    
class Solution2:
    def minimizedStringLength(self, s: str) -> int:
        new_s = ''
        for char in s:
            if char not in new_s:
                new_s += char
        return len(new_s)

s1 = Solution()
s2 = Solution2()

s = "aaabc"
print(s2.minimizedStringLength(s))

s = "cbbd"
print(s2.minimizedStringLength(s))

s = "dddaaa"
print(s2.minimizedStringLength(s))
