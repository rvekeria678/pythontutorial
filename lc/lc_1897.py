# Leetcode Problem #1897: Redistribute Characters to Make All Strings Equal

# Description: You are given an array of strings words (0-indexed). In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j]. Return true if you can make every string in words equal using any number of operations, and false otherwise.

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        bank = {}
        size = len(words)
        for word in words:
            for character in word:
                if character in bank:
                    bank[character] += 1
                else:
                    bank[character] = 1
        for character in bank:
            if bank[character] % size:
                return False
        return True

s = Solution()

words = ["abc","aabc","bc"]
print(s.makeEqual(words))

words = ["ab","a"]
print(s.makeEqual(words))
