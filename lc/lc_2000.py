# Leetcode Problem #2000: Reverse Prefix of Word

# Description: Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing. For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd". Return the resulting string.

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(word):
            if c == ch:
                word = word[0:i+1][::-1] + word[i+1:]
                break
        return word

s = Solution()

word = "abcdefd"
ch = "d"
print(s.reversePrefix(word, ch))

word = "xyxzxe"
ch = "z"
print(s.reversePrefix(word, ch))

word = "abcd"
ch = "z"
print(s.reversePrefix(word, ch))
