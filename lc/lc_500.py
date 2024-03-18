# Leetcode Problem #500: Keyboard Row

# Description: Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below. In the American keyboard: the first row consists of the characters "qwertyuiop", the second row consists of the characters "asdfghjkl", and the third row consists of the characters "zxcvbnm".

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first_row = 'qwertyuiop'
        second_row = 'asdfghjkl'
        third_row = 'zxcvbnm'
        ans = []
        for word in words:
            rows = {}
            for character in word.lower():
                if character in first_row:
                    rows[first_row] = ''
                elif character in second_row:
                    rows[second_row] = ''
                else:
                    rows[third_row] = ''
            if len(rows) == 1:
                ans.append(word)
        return ans

s = Solution()

words = ["Hello","Alaska","Dad","Peace"]
print(s.findWords(words))

words = ["omk"]
print(s.findWords(words))

words = ["adsdf","sfd"]
print(s.findWords(words))
