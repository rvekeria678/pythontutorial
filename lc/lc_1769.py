# Leetcode Problem #1769: Minimum Number of Operations to Move All Balls to Each Box

# Description: You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball. In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes. Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box. Each answer[i] is calculated considering the initial state of the boxes.

class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        d, res = {}, []
        for e in range(len(boxes)):
            if boxes[e] == '1':
                d[e] = '1'
        for i in range(len(boxes)):
            operations = 0
            for j in d:
                operations += abs(j-i)
            res.append(operations)

        return res

s = Solution()

boxes = "110"
print(s.minOperations(boxes))
boxes = "001011"
print(s.minOperations(boxes))

