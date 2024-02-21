# Leetcode Problem #1816: Truncate Sentence

# Description: A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation). (For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.)

# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])

s = Solution()

str1 = "Hello how are you Contestant"

str2 = "What is the solution to this problem"

str3 = "chopper is not a tanuki"

print(s.truncateSentence(str1, 4))
print(s.truncateSentence(str2, 4))
print(s.truncateSentence(str3, 5))