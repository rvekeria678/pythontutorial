# Leetcode Problem 2011: Final Value of Variable After Performing Operations

# Description: Return the value of X after performing string operations on it

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        inst = {"--X":lambda a : a - 1, 
                "X--":lambda a: a - 1,
                "++X":lambda a: a + 1,
                "X++":lambda a: a + 1}
        
        X = 0

        for i in operations:
            X = inst[i](X)
        return X

s = Solution()

l1 = ["--X","X++","X++"]
l2 = ["++X","++X","X++"]
l3 = ["X++","++X","--X","X--"]

print(s.finalValueAfterOperations(l1))
print(s.finalValueAfterOperations(l2))
print(s.finalValueAfterOperations(l3))