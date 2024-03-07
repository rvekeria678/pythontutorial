# Leetcode Problem #2562: Find the Array Concatenation Value

# Description: You are given a 0-indexed integer array nums. The concatenation of two numbers is the number formed by concatenating their numerals. For example, the concatenation of 15, 49 is 1549. The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty: If there exists more than one number in nums, pick the first element and last element in nums respectively and add the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums, If one element exists, add its value to the concatenation value of nums, then delete it. Return the concatenation value of the nums.

class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        left, right = 0, len(nums)-1
        concat = 0
        while left <= right:
            if left != right:
                num = int(str(nums[left])+str(nums[right]))
            else:
                num = nums[left]
            concat += num

            right -= 1
            left += 1
        return concat

s = Solution()

nums = [7,52,2,4]
print(s.findTheArrayConcVal(nums))

nums = [5,14,13,8,12]
print(s.findTheArrayConcVal(nums))

