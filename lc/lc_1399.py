# Leetcode Problem #1399: Count Largest Group

# Description: You are given an integer n. Each number from 1 to n is grouped according to the sum of its digits. Return the number of groups that have the largest size.

class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        m = 0
        count = 0
        for num in range(1,n+1):
            digitSum = self.getDigitSum(num) 
            if digitSum in d:
                d[digitSum] += 1
            else:
                d[digitSum] = 1
        for num in d:
            if m < d[num]:
                m = d[num]
                count = 0
            if d[num] == m:
                count += 1
        return count
    
    def getDigitSum(self, num: int):
        total = 0
        while num:
            total += num % 10
            num //= 10
        return total


s = Solution()

n = 13
print(s.countLargestGroup(n))

n = 2
print(s.countLargestGroup(n))

n = 24
print(s.countLargestGroup(n))