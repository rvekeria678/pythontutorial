# Leetcode Problem #27: Remove Element

# Description: Give an integer array 'nums' and an integer 'val', remove all occurences of 'val' in 'nums' in-place. The order of the lements may be changed. Then return the number of elements in 'nums' which are not equal to 'val'. Consider the number of elements in 'nums' which are not equal to 'val' be 'k'.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if (nums[i] != val):
                nums[k] = nums[i]
                k += 1
        return k
    
s = Solution()

arr = [3,2,2,3]
val = 3

print(s.removeElement(nums=arr, val=val))