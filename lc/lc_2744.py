# Leetcode Problem #2744: Find Maximum Number of String Pairs

# Description: You are given a 0-indexed array words consisting of distinct strings. The string words[i] can be paired with the string words[j] if: The string words[i] is equal to the reversed string of words[j]. 0 <= i < j < words.length. Return the maximum number of pairs that can be formed from the array words. Note that each string can belong in at most one pair.

class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        dict, count = {}, 0

        for i in words:
            if i[::-1] in dict:
                count +=1
            if i not in dict:
                dict[i] = '-'
        return count
    

s = Solution()

words = ["cd","ac","dc","ca","zz"]
print(s.maximumNumberOfStringPairs(words))

words = ["ab","ba","cc"]
print(s.maximumNumberOfStringPairs(words))

words = ["aa","ab"]
print(s.maximumNumberOfStringPairs(words))





