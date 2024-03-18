# Leetcode Problem #2085: Count Common Words With One Occurrence

# Description: Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        frequency1, frequency2 = {}, {}
        count = 0
        for word in words1:
            if word in frequency1:
                frequency1[word] += 1
            else:
                frequency1[word] = 1
        for word in words2:
            if word in frequency2:
                frequency2[word] += 1
            else:
                frequency2[word] = 1
        for freq in frequency1:
            if freq in frequency2 and frequency1[freq] == 1 and frequency2[freq] == 1:
                count += 1
        return count

s = Solution()        

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
print(s.countWords(words1, words2))

words1 = ["b","bb","bbb"]
words2 = ["a","aa","aaa"]
print(s.countWords(words1, words2))

words1 = ["a","ab"]
words2 = ["a","a","a","ab"]
print(s.countWords(words1, words2))
