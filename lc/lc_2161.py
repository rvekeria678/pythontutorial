# Leetcode Problem #2161: Partition Array According to Given Pivot

# Description: You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied: Every element less than pivot appears before every element greater than pivot, Every element equal to pivot appears in between the elements less than and greater than pivot, The relative order of the elements less than pivot and the elements greater than pivot is maintained, More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj. Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj. Return nums after the rearrangement.

class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        smaller, equivalent, larger = [], [], []

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                larger.append(num)
            else:
                equivalent.append(num)
        
        return smaller + equivalent + larger

class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        left = 0
        right = 1
        size = len(nums)
        while left < size-1:
            if nums[left] > pivot:
                print("swap")
                temp = nums[left]
                nums[left] = nums[left+1]
                nums[left] = temp
            left += 1
                
        return nums

s = Solution()

nums = [9,12,5,10,14,3,10]
pivot = 10
print(s.pivotArray(nums, pivot))

nums = [-3,4,3,2]
pivot = 2
print(s.pivotArray(nums, pivot))

