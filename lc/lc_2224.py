# Leetcode Problem #2224: Minimum Number of Operations to Convert Time

# Description: You are given two strings current and correct representing two 24-hour times. 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59. In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times. Return the minimum number of operations needed to convert current to correct.

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        mm__current = int(current[:2]) * 60 + int(current[3:])
        mm__correct = int(correct[:2]) * 60 + int(correct[3:])

        mm__difference = abs(mm__correct - mm__current)
        operations = 0

        if mm__difference >= 60:
            operations += mm__difference // 60
            mm__difference -= 60 * (mm__difference // 60)
        if mm__difference >= 15:
            operations += mm__difference // 15
            mm__difference -= 15 * (mm__difference // 15)
        if mm__difference >= 5:
            operations += mm__difference // 5
            mm__difference -= 5 * (mm__difference // 5)
        if mm__difference >= 1:
            operations += mm__difference
        return operations


s = Solution()

current = "02:30"
correct = "04:35"
print(s.convertTime(current, correct))

current = "11:00"
correct = "11:01"
print(s.convertTime(current, correct))

current = '00:00'
correct = '23:59'
print(s.convertTime(current, correct))

current = "09:41"
correct = "10:34"
print(s.convertTime(current, correct))