# Leetcode Problem #1002: Find Common Characters

# Description: Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = {}
        res = []
        for i in range(len(words)):
            for character in words[i]:
                if character in common:
                    if i not in common[character]:
                        common[character][i] = 1
                    else:
                        common[character][i] += 1
                else:
                    common[character] = {}
                    common[character][i] = 1
        for character in common:
            if len(common[character]) == len(words):
                res += [character] * min(common[character].values())

        return res

s = Solution()

words = ["bella","label","roller"]
print(s.commonChars(words))

words = ["cool","lock","cook"]
print(s.commonChars(words))
