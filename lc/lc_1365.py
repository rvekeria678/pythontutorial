# LeetCode Problem #1365: How Many Number Are Smaller Than the Current Number

# Description: Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        dict = {}
        res = []
        count = 0
        for i in nums:
            if i in dict:
                res.append(dict[i])
            else:
                for j in nums:
                    if i > j:
                        count += 1
                dict[i] = count
                res.append(count)
                count = 0      
        return res
            

s = Solution()

l1 = [8,1,2,2,3]
l2 = [6,5,4,8]
l3 = [7,7,7,7]

print(s.smallerNumbersThanCurrent(l1))
print(s.smallerNumbersThanCurrent(l2))
print(s.smallerNumbersThanCurrent(l3))