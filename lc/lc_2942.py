# Leetcode Problem #2942: Find Words Containing Character

# Description: You are given a 0-indexed array of strings words and a character x. Return an array of indicies representing the words that contain the character x. The returned array may be in any order

class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        res = []
        for i,j in enumerate(words):
            if x in j:
                res.append(i)
        return res

s = Solution()

l1 = ["leet","code"]
l2 = ["abc","bcd","aaaa","cbc"]
l3 = ["abc","bcd","aaaa","cbc"]

print(s.findWordsContaining(l1, 'e'))
print(s.findWordsContaining(l2, 'a'))
print(s.findWordsContaining(l3,'z'))