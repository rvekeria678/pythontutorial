# Leetcode Problem #821: Shortest Distance to a Character

# Description: Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s. The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        left = 0
        right = 0
        mid = 0
        res = []
        while right < len(s):
            if (s[right] == c or right + 1 >= len(s)) and right >= mid:
                if right + 1 >= len(s) and s[right] != c:
                    res.append(mid-left)
                elif s[left] == c:
                    closest = min(right-mid, mid-left)
                    res.append(closest)
                else:
                    res.append(right-mid)
                mid += 1
            else:
                right += 1
            if right and s[right-1] == c:
                left = right - 1
        return res        

s = Solution()

word = "loveleetcode"
c = "e"
print(s.shortestToChar(word,c))

word = "aaab"
c = "b"
print(s.shortestToChar(word,c))

word = "aaba"
c = "b"
print(s.shortestToChar(word,c))