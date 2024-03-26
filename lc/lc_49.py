# Leetcode Problem #49: Group Anagrams

# Description: Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for s in strs:
            pattern = ''.join((sorted(s)))
            if pattern in d:
                d[pattern].append(s)
            else:
                d[pattern] = [s]
        return list(d.values())

s = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))

strs = [""]
print(s.groupAnagrams(strs))

strs = ["a"]
print(s.groupAnagrams(strs))

