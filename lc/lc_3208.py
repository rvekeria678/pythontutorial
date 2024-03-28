# Leetcode Problem #3208: Ant on the Boundary

# Description: An ant is on a boundary. It sometimes goes left and sometimes right. You are given an array of non-zero integers nums. The ant starts reading nums from the first element of it to its end. At each step, it moves according to the value of the current element: If nums[i] < 0, it moves left by -nums[i] units. If nums[i] > 0, it moves right by nums[i] units. Return the number of times the ant returns to the boundary. (There is an infinite space on both sides of the boundary.) (We check whether the ant is on the boundary only after it has moved |nums[i]| units. In other words, if the ant crosses the boundary during its movement, it does not count.)

class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        res = pos = 0
        for num in nums:
            pos += num
            if not pos:
                res += 1
        return res

s = Solution()

nums = [2,3,-5]
print(s.returnToBoundaryCount(nums))

nums = [3,2,-3,-4]
print(s.returnToBoundaryCount(nums))
