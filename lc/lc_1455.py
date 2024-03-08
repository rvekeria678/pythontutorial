# Leetcode Problem #1455: Check If a Word Occurs As a Prefix of Any Word in a Sentence

# Description: Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence. Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1. A prefix of a string s is any leading contiguous substring of s.

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        

s = Solution()

sentence = "i love eating burger"
searchWord = "burg"
print(s.isPrefixOfWord(sentence, searchWord))

sentence = "this problem is an easy problem"
searchWord = "pro"
print(s.isPrefixOfWord(sentence, searchWord))

sentence = "i am tired"
searchWord = "you"
print(s.isPrefixOfWord(sentence, searchWord))
