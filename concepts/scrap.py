class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums = list(set(nums))
        print(nums)
        return len(nums)
    
    def removeDups(self, nums: list[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if (nums[k] != nums[i]):
                k += 1
                nums[k] = nums[i]
        print(nums)
        return k + 1
    
arr = [1,1,2]
s = Solution()

print(s.removeDups(nums=arr))