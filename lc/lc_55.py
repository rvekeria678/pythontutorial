# Leetcode Problem #55: Jump Game

# Description: You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        idx = 0
        size = len(nums)
        if size == 1: return True
        while idx < size-1:
            print(idx, nums)
            if nums[idx]:
                idx += 1
            else:
                idx -= 1
                if nums[idx]:
                    nums[idx] -= 1
                    idx += nums[idx] + 1
            if not nums[0]:
                return False
        return True 
    
class Solution2:
    def canJump(self, nums: list[int]) -> bool: 
        x = 0
        for num in nums:
            if x < 0:
                return False
            elif x < num:
                x = num
            x -= 1
        return True

s = Solution()
s2 = Solution2()

nums = [2,3,1,1,4]
print(s2.canJump(nums))

nums = [1,1,1,1,1]
print(s2.canJump(nums))

nums = [3,2,1,0,4]
print(s2.canJump(nums))

nums = [0]
print(s2.canJump(nums))

nums = [2, 0]
print(s2.canJump(nums))