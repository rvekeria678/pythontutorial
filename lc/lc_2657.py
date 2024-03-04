# Leetcode Problem #2657: Find the Prefix Common Array of Two Arrays

# Description: You are given two 0-indexed integer permutations A and B of length n. A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B. Return the prefix common array of A and B. A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        ad, bd, res = {}, {}, []
        for i in range(len(A)):
            if A[i] not in ad:
                ad[A[i]] = '-'
            if B[i] not in bd:
                bd[B[i]] = '-'
            count = 0
            for i in ad:
                if i in bd:
                    count += 1
            res.append(count)
        return res
    
class Solution2:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        result = []
        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                if A[i] in B[0:i+1]:
                    count += 1
                if B[i] in A[0:i+1]:
                    count += 1
            else:
                count += 1
            result.append(count)
        return result



s = Solution()
s2 = Solution2()

A = [1,3,2,4]
B = [3,1,2,4]
print(s2.findThePrefixCommonArray(A,B))

A = [2,3,1]
B = [3,1,2]
print(s2.findThePrefixCommonArray(A,B))
