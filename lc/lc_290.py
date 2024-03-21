# Leetcode Problem #290: Word Pattern

# Description: Given a pattern and a string s, find if s follows the same pattern. Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m1, m2 = {}, {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in m1:
                if m1[pattern[i]] != s[i]:
                    return False
            else:
                m1[pattern[i]] = s[i]
            if s[i] in m2:
                if m2[s[i]] != pattern[i]:
                    return False
            else:
                m2[s[i]] = pattern[i]

        return True
    
class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, d = s.split(), {}
        if len(pattern) != len(words): return False
        if len(set(pattern)) != len(set(words)): return False

        for i in range(len(words)):
            if pattern[i] in d:
                if d[pattern[i]] != words[i]:
                    return False
            else:
                d[pattern[i]] = words[i]
        return True

s = Solution()
s2 = Solution2()

pattern = "abba"
sentence = "dog cat cat dog"
print(s2.wordPattern(pattern, sentence))

pattern = "abba"
sentence = "dog cat cat fish"
print(s2.wordPattern(pattern, sentence))

pattern = "aaaa"
sentence = "dog cat cat dog"
print(s2.wordPattern(pattern, sentence))
