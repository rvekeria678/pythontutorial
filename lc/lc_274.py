# Leetcode Problem #274: H-Index

# Description: Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index. According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        d = {}
        for c in citations:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        return d

s = Solution()

citations = [3,0,6,1,5]
print(s.hIndex(citations))

citations = [1,3,1]
print(s.hIndex(citations))
