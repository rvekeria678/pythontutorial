# Leetcode Problem #2367: Number of Arithmetic Triplets

# Description: You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met: i < j < k; nums[j] - nums[i] == diff; nums[k] - nums[j] == diff

class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        left, mid, right, count = 0,1,2,0
        d = {}

        while left < len(nums)-2:
            if nums[mid] - nums[left] == diff and nums[right] - nums[mid] == diff:
                count += 1
                if right < len(nums)-1:
                    right += 1
                elif mid < len(nums)-2:
                    mid += 1
                else:
                    left += 1
            elif right < len(nums)-1:
                right += 1
            elif mid < len(nums) - 2:
                mid += 1
                right = mid + 1
            else:
                left += 1
                mid = left + 1
                right = mid + 1
        return count
    
class Solution2:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count = 0
        for n in nums:
            lower = n - diff
            upper = n + diff
            if lower in nums and upper in nums:
                count += 1
        return count


s = Solution()
s2 = Solution2()

nums1 = [0,1,4,6,7,10]
diff1 = 3

nums2 = [4,5,6,7,8,9]
diff2 = 2

print(s2.arithmeticTriplets(nums1, diff1))
print(s2.arithmeticTriplets(nums2, diff2))