# Leetcode Problem #2433: Find the Original Array of Prefix Xor

# Description: You are given an integer array pref of size n. Find and return the array arr of size n that satisfies: pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]. Note that ^ denotes the bitwise-xor operation. It can be proven that the answer is unique.

class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        base, res = pref[0], [pref[0]]
        if len(pref) < 2:
            return res
        for i in range(1,len(pref)):
            el = base ^ pref[i]
            base ^= el
            res.append(el)
        return res
s = Solution()

pref = [5,2,0,3,1]
print(s.findArray(pref))
pref = [13]
print(s.findArray(pref))
