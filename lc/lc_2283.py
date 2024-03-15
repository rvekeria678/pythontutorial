# Leetcode Problem #2283: Check if Number Has Equal Digit Count and Digit Value

# Description: You are given a 0-indexed string num of length n consisting of digits. Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

class Solution:
    def digitCount(self, num: str) -> bool:
        d = {}
        for i, digit in enumerate(num):
            d[i] = int(digit)

        print(d)
        for i in d:
            if d[i] != num.count(str(i)):
                return False
        return True

s = Solution()

num = "1210"
print(s.digitCount(num))

num = "030"
print(s.digitCount(num))
