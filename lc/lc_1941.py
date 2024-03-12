# Leetcode Problem #1941: Check if All Characters Have Equal Number of Occurences

# Description: Given a string s, return true if s is a good string, or false otherwise. A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq, temp = {}, {}
        last = 1
        for character in s:
            if character in temp:
                temp[character] += 1
            else:
                temp[character] = 1
            if temp[character] in freq:
                freq[temp[character]] += 1
            else:
                freq[temp[character]] = 1
                last = temp[character]
        return freq[last] == (len(s) / last)

s = Solution()

str1 = "abacbc"
str2 = "aaabb"

print(s.areOccurrencesEqual(str1))
print(s.areOccurrencesEqual(str2))