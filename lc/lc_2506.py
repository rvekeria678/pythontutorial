# Leetcode Problem #2506: Count Pairs of Similar Strings:

# Description: You are given a 0-indexed string array words. Two strings are similar if they consist of the same characters. For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c', However, "abacba" and "bcfd" are not similar since they do not consist of the same characters. Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.

class Solution:
    def similarPairs(self, words: list[str]) -> int:
        count = 0
        for word1 in range(len(words)):
            for word2 in range(word1+1,len(words)):
                if 2 * len(set(words[word1]+words[word2])) == len(set(words[word1])) + len(set(words[word2])):
                    count += 1
        return count

class Solution2:
    def similarPairs(self, words: list[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if ''.join(sorted(set(words[i]))) == ''.join(sorted(set(words[j]))):
                    count += 1
        return count  

class Solution3:
    def similarPairs(self, words: list[str]) -> int:
        seen = {}
        count = 0
        for word in words:
            chars = ''.join(sorted(set(word)))
            if chars in seen:
                seen[chars] += 1
            else:
                seen[chars] = 1 
        for sequence in seen:
            count += seen[sequence] * (seen[sequence] - 1) //2 
        return count
    
s = Solution() 
s2 = Solution2()
s3 = Solution3()

words = ["aba","aabb","abcd","bac","aabc"]
print(s3.similarPairs(words))

words = ["aabb","ab","ba"]
print(s3.similarPairs(words))

words = ["nba","cba","dba"]
print(s3.similarPairs(words))
