# Leetcode Problem #1: Two Sum

# Description: Given an integer array 'nums' and an integer 'target', return indicies of the two numbers such that they add up to target. (Assume each input has one solution)

class Solution():
    def twoSum(self, nums, target):
        hashTab = {}
        for i in range(len(nums)):
            if nums[i] in hashTab:
                return hashTab[nums[i]], i
            else:
                hashTab[target - nums[i]] = i

arr = [3,2,4]
target = 6

s = Solution()

print(s.twoSum(nums=arr, target=target))