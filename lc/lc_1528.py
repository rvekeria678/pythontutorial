# Leetcode Problem #1528: Shuffle String

# Description: You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string. Return the shuffled string.

class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        dict = {}
        shuffled = ""
        for i in indices:
            dict[indices[i]] = s[i]
        for i in range(len(s)):
            shuffled += dict[i]
        return shuffled

s = Solution()

str1 = "codeleet"
indices1 = [4,5,6,7,0,2,1,3]

str2 = "abc"
indices2 = [0,1,2]

print(s.restoreString(str1, indices1))
print(s.restoreString(str2, indices2))