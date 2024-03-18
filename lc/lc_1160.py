# Leetcode Problem #1160: Find Words That Can Be Formed by Characters

# Description: You are given an array of strings words and a string chars. A string is good if it can be formed by characters from chars (each character can only be used once). Return the sum of lengths of all good strings in words.

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        d = {}
        res = 0
        for character in chars:
            if character in d:
                d[character] += 1
            else:
                d[character] = 1
        for word in words:
            temp = {}
            word_size = len(word)
            for character in word:
                if character in temp:
                    temp[character] += 1
                else:
                    temp[character] = 1
                if character not in d or temp[character] > d[character]:
                    res -= word_size
                    break
            res += word_size
        return res        


s = Solution()        

words = ["cat","bt","hat","tree"]
chars = "atach"
print(s.countCharacters(words, chars))

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(s.countCharacters(words, chars))
