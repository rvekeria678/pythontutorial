# Leetcode Problem #3: Longest Substring Without Repeating Characters

# Description: Given a string s, find the length of the longest substring without repeating characters

class Solution:
    def lengthofLongestSubstring(self, s: str) -> int:
        substr = ''
        longest = 0
        for i in range(len(s)):
            for j in s[i::]:
                #print('j: "'+j+'"')
                if j in substr:
                    longest = len(substr) if len(substr) > longest else longest
                    substr = ''
                    break
                else:
                    substr += j
        return 1 if len(s) == 1 else longest


s = Solution()

print(s.lengthofLongestSubstring('abcabcbb'))

print(s.lengthofLongestSubstring('bbbbb'))

print(s.lengthofLongestSubstring('pwwkew'))

print(s.lengthofLongestSubstring(' '))

print(s.lengthofLongestSubstring('h'))