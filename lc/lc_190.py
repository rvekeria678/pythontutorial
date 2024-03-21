# Leetcode Problem #190: Reverse Bits

# Description: Reverse buts of a given 32 bits unsigned integer

class Solution:
    def reverseBits(self, n: int) -> int:
        binary_number = str(bin(n))[2:]
        rev = binary_number[::-1] + '0' * (32-len(binary_number))
        return int(rev, 2)
       
s = Solution()

print(s.reverseBits(43261596))
print(s.reverseBits(4294967293))

