# Leetcode Problem #1935: Maximum Number of Words You can Type

# Description: There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly. Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        typed = len(text)
        for word in text:
            for broken in brokenLetters:
                if broken in word:
                    typed -= 1
                    break
        return typed

s = Solution()

text = "hello world"
brokenLetters = "ad"
print(s.canBeTypedWords(text, brokenLetters))

text = "leet code"
brokenLetters = "lt"
print(s.canBeTypedWords(text, brokenLetters))

text = "leet code"
brokenLetters = "e"
print(s.canBeTypedWords(text, brokenLetters))
