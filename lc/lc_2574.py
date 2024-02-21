# Leetcode Problem #2574: Left and Right Sum Differences

# Description: Given a 0-indexed integer array nums, find a 0-indexed integer array answer where: answer.length == nums.length; answer[i] = |leftSum[i] - rightSum[i]|.

# Additional Requirements: leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0. rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0. Return the array answer.

class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            result.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return result
    
class Solution2:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        partial, total = 0, sum(nums)
        result = []

        for i in nums:
            partial += i
            result.append(abs(partial - total))
            total -= i
        return result

s = Solution()
s2 = Solution2()

l1 = [10,4,8,3]
l2 = [1]

print(s.leftRightDifference(l1))
print(s.leftRightDifference(l2))

print(s2.leftRightDifference(l1))
print(s2.leftRightDifference(l2))
