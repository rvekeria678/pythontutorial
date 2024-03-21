# Leetcode Problem #383: Ransom Notes

# Description: Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise. Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for character in magazine:
            if character in d:
                d[character] += 1
            else:
                d[character] = 1
        for character in ransomNote:
            if character not in d or not d[character]:
                return False
            else:
                d[character] -= 1
        return True

s = Solution()

ransomNote = "a"
magazine = "b"
print(s.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "ab"
print(s.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "aab"
print(s.canConstruct(ransomNote, magazine))
