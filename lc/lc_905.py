# Leetcode Problem #905: Sort Array by Parity

# Description: Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.Return any array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even, odd = [], []
        for i in nums:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)

        return even + odd

class Solution2:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, 1

        while right < len(nums):
            if not nums[right] % 2:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                left += 1
                right = left
            right += 1
        
        return nums

s = Solution()        
s2 = Solution2()

nums = [3,1,2,4]
print(s2.sortArrayByParity(nums))

nums = [0]
print(s2.sortArrayByParity(nums))
