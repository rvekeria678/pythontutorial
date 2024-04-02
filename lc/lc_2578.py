# Leetcode Problem #2578: Split With Minimum Sum

# Description: Given a positive integer num, split it into two non-negative integers num1 and num2 such that: The concatenation of num1 and num2 is a permutation of num (In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num), num1 and num2 can contain leading zeros. Return the minimum possible sum of num1 and num2. (Notes: It is guaranteed that num does not contain any leading zeros. The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.)

class Solution:
    def splitNum(self, num: int) -> int:
        num_list = sorted(list(str(num)))
        num1 = num2 = ''
        for i in range(len(num_list)):
            if i % 2:
                num1 += num_list[i]
            else:
                num2 += num_list[i]
        return int(num1) + int(num2)

s = Solution()

num = 4325
print(s.splitNum(num))

num = 687
print(s.splitNum(num))
