# Leetcode Problem #1832: Check if the Sentence is Pangram

# Description: A pangram is a sentence where every letter of the English alphabet appears at least once. Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dict = {}
        for i in sentence:
            if i not in dict:
                dict[i] = 1
        return True if len(dict) >= 26 else False
    
s = Solution()

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(s.checkIfPangram(sentence))

sentence = "leetcode"
print(s.checkIfPangram(sentence))
