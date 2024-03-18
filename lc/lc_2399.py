# Leetcode Problem #2399: Check Distances Between Same Letters

# Description: You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26. Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25). In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored. Return true if s is a well-spaced string, otherwise return false.

class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = abs(d[s[i]]-i) - 1
                if distance[ord(s[i])-97] != d[s[i]]:
                    return False
            else:
                d[s[i]] = i
        return True

s = Solution()

st = "abaccb"
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(s.checkDistances(st,distance))

st = "aa"
distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(s.checkDistances(st,distance))



