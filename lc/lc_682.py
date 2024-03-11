# Leetcode Problem #682: Baseball Game

# Description: You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record. You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following: An integer x: Record a new score of x, '+': Record a new score that is the sum of the previous two scores.Record a new score that is the sum of the previous two scores, 'D': Record a new score that is the double of the previous score, 'C': Invalidate the previous score, removing it from the record. Return the sum of all the scores on the record after applying all the operations. The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        numbers = []
        size = 0
        for operation in operations:
            if operation == '+':
                numbers.append(numbers[size-1]+numbers[size-2])
                size += 1
            elif operation == 'D':
                numbers.append(2*numbers[size-1])
                size += 1
            elif operation == 'C':
                numbers.pop()
                size -= 1
            else:
                numbers.append(int(operation))
                size += 1
        return sum(numbers)

s = Solution()

ops = ["5","2","C","D","+"]
print(s.calPoints(ops))
ops = ["5","-2","4","C","D","9","+","+"]
print(s.calPoints(ops))
ops = ["1","C"]
print(s.calPoints(ops))
