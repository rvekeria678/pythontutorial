# Leetcode Problem #66: Plus One

# Description: Given a large integer represented as an integer array digits, where each digit[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in reversed(range(len(digits))):
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] %= 10
            else:
                return digits
        return [1] + digits

s = Solution()
arr = [1,2,3]
arr2 = [9,9,9]

print(s.plusOne(digits=arr))
print(s.plusOne(digits=arr2))