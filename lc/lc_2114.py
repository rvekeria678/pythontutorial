# Leetcode Problem 2114: Maximum Number of Words Found in Sentences

# Description: A sentence is a list of words that are separated by a single space with no leading or trailing spaces

# You are given an array of strings sentences, where each sentences[i] represents a single sentence.

#Return the maximum number of words that appear in a single sentence.

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max = 0
        for i in sentences:
            total_words = len(i.split())
            max = total_words if total_words > max else max

        return max

s = Solution()

l1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
l2 = ["please wait", "continue to fight", "continue to win"]

print(s.mostWordsFound(l1))
print(s.mostWordsFound(l2))