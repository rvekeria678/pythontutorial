# Leetcode Problem #696: Count Binary Substrings

# Description: Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively. Substrings that occur multiple times are counted the number of times they occur.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        size = len(s)
        buff = size - 1 if size % 2 else size
        left = 0
        right = buff
        count = 0
        while buff:
            if right > size:
                buff -= 2
                right = buff
                left = 0
            if buff:
                if s[left:right][buff//2:] == '1' * (buff//2) and not int(s[left:right][:buff//2],2):
                    print(s[left:right])
                    count += 1
                elif s[left:right][:buff//2] == '1' * (buff//2) and not int(s[left:right][buff//2:],2):
                    print(s[left:right])
                    count += 1
            left += 1
            right += 1
        return count
    
class Solution2:
    def countBinarySubstrings(self, s: str) -> int:
        size = len(s)
        res = 0
        substr_size = 2

        while substr_size <= size:
            first = '1' * (substr_size // 2)
            second = '0' * (substr_size // 2)

            res += s.count(first+second)
            res += s.count(second+first)

            substr_size += 2

        return res

class Solution3:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr = 0, 1
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                prev, curr = curr, 1
            if curr <= prev:
                res += 1
        return res

s = Solution()
s2 = Solution2()
s3 = Solution3()

sequence = "00110011"
print(s3.countBinarySubstrings(sequence))

sequence = "10101"
print(s3.countBinarySubstrings(sequence))

sequence = "000111000"
print(s3.countBinarySubstrings(sequence))