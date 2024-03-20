# Leetcode Problem #242: Valid Anagram

# Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s, freq_t = {}, {}
        for char in s:
            if char in freq_s:
                freq_s[char] += 1
            else:
                freq_s[char] = 1
        for char in t:
            if char in freq_t:
                freq_t[char] += 1
            else:
                freq_t[char] = 1
        for char in freq_s:
            if char not in freq_t or freq_s[char] != freq_t[char]:
                return False
        return True if len(freq_s) == len(freq_t) else False
    
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))
    
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                return False
        for char in freq:
            if freq[char]:
                return False
        return True

s = Solution()   
s2 = Solution2()
s3 = Solution3()

word1 = "anagram"
word2 = "nagaram"
print(s3.isAnagram(word1, word2))

word1 = "rat"
word2= "car"
print(s3.isAnagram(word1, word2))
