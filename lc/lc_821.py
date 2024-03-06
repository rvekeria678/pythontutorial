# Leetcode Problem #821: Shortest Distance to a Character

# Description: Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s. The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        left = 0
        right = 0
        res = []
        while left < len(s):
            if s[right] == c and left <= right:
                res.append(right - left)
            elif s[right] == c:
                right += 1
                left += 1
            right += 1
        return res

s = Solution()

word = "loveleetcode"
c = "e"
print(s.shortestToChar(word,c))

word = "aaab"
c = "b"
print(s.shortestToChar(word,c))