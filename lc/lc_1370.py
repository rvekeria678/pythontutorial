# Leetcode Problem #1370: Increasing Decreasing String:

# Description: You are given a string s. Reorder the string using the following algorithm: 1) Pick the smallest character from s and append it to the result. 2) Pick the smallest character from s which is greater than the last appended character to the result and append it. 3) Repeat step 2 until you cannot pick more characters. 4) Pick the largest character from s and append it to the result. 5) Pick the largest character from s which is smaller than the last appended character to the result and append it. 6) Repeat step 5 until you cannot pick more characters. 7) Repeat the steps from 1 to 6 until you pick all characters from s. In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result. Return the result string after sorting s with this algorithm.

class Solution:
    def sortString(self, s: str) -> str:
        d = {}
        res = ''
        count = 0
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        ordered_seq = sorted(d)
        while count < len(s):
            for char in ordered_seq:
                if (d[char]):
                    res += char
                    d[char] -= 1
                    count += 1
            for char in ordered_seq[::-1]:
                if(d[char]):
                    res += char
                    d[char] -= 1
                    count += 1
        return res

s = Solution()

string = "aaaabbbbcccc"
print(s.sortString(string))

string = "rat"
print(s.sortString(string))
