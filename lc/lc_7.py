# Leetcode Problem #7: Reverse Integer

# Description: Given a signed 32-bit integer 'x', return 'x' with its digits reversed. If reversing 'x' causes that value to go outside the signed 32-bit integer range, then return 0

class Solution:
    def reverse(self, x: int) -> int:
        x = int(str(x)[::-1]) if str(x)[0] != '-' else -1 * int((str(x)[1:])[::-1])
        return x if (x > -2 ** 31 and x < 2 ** 31 - 1) else 0

s = Solution()

print(s.reverse(-1234))

print(s.reverse(1534236469))