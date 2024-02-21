# Leetcode Problem #2006: Count Number of Pairs With Absolute Difference K

# Description: Given an integer array nums and an integer k, return the number of pairs (i,j) where i < j such that [nums[i]-nums[j]] == k

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i] - nums[j]) == k and i < j:
                    print(f'{nums[i]}(i={i}), {nums[j]}(j={j})')
                    count += 1
        return count 

class Solution2:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        dict = {}
        for j,i in enumerate(nums):
            if i not in dict:
                dict[i] = k
            count += nums[j::].count(i-dict[i]) + nums[j::].count(i+k)
        return count


s = Solution()
s2 = Solution2()

l1 = [1,2,2,1]
l2 = [1,3]
l3 = [3,2,1,5,4]
l4 = [9,3,1,1,4,5,4,9,5,10]

print(s2.countKDifference(l1,1))
print(s2.countKDifference(l2,3))
print(s2.countKDifference(l3,2))
#print('s:',s.countKDifference(l4,1))
print(s2.countKDifference(l4,1))