# Leetcode Problem #2160: Minimum Sum of Four Digit Number After Splitting Digits

# Description: You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used. For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329]. Return the minimum possible sum of new1 and new2.

class Solution:
    def minimumSum(self, num: int) -> int:
        ns = sorted(str(num))
        return int(ns[0]) * 10 + int(ns[1]) * 10 + int(ns[2]) + int(ns[3])

s = Solution()

num1 = 2932
num2 = 4009

print(s.minimumSum(num1))
print(s.minimumSum(num2))

