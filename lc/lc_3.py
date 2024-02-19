# Leetcode Problem #3: Longest Substring Without Repeating Characters

# Description: Given a string s, find the length of the longest substring without repeating characters

class Solution:
    def lengthofLongestSubstring(self, s: str) -> int:
        substr = ''
        longest = 0
        for i in range(len(s)):
            for j in s[i::]:
                if j in substr:
                    longest = len(substr) if len(substr) > longest else longest
                    substr = ''
                    break
                else:
                    substr += j
        return 1 if len(s) == 1 else longest

# Sliding Window Solution
class Solution2:
    def lengthofLongestSubstring(self, s: str) -> int:
        left, right, max = 0,1,0

        if len(s) < 2:
            return len(s)

        while right < len(s):
            if s[right] not in s[left:right]:
                right += 1
                if right == len(s):
                    max = len(s[left:right]) if len(s[left:right]) > max else max
            else:
                max = len(s[left:right]) if len(s[left:right]) > max else max
                left += 1

        return max

s = Solution()
s2 = Solution2()

print(s2.lengthofLongestSubstring('abcabcbb'))

print(s2.lengthofLongestSubstring('bbbbb'))

print(s2.lengthofLongestSubstring('pwwkew'))

print(s2.lengthofLongestSubstring(' '))

print(s2.lengthofLongestSubstring('h'))

print(s2.lengthofLongestSubstring('au'))