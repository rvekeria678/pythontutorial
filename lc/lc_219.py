# Leetcode Problem #219: Contains Duplicate II

# Description: Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i-j) <= k

class Solution:
    def containsNearbyDuplicates(self, nums: list[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                if i <= d[nums[i]]:
                    return True
                else:
                    d[nums[i]] = i + k
            else:
                d[nums[i]] = i + k
        return False
    
s = Solution()

l1 = [1,2,3,1]
l2 = [1,0,1,1]
l3 = [1,2,3,1,2,3]
l4 = [1]

print(s.containsNearbyDuplicates(l1,3))
print(s.containsNearbyDuplicates(l2,1))
print(s.containsNearbyDuplicates(l3,2))
print(s.containsNearbyDuplicates(l4,2))

