# Leetcode Problem #190: Reverse Bits

# Description: Reverse buts of a given 32 bits unsigned integer

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(bin(n))[::-1],2)
    
class Solution2:
    def reverseBits(self, n: int) -> int:
        n = ~((~n) << 32)
        return n
    
s = Solution()
s2 = Solution2()

#print(s.reverseBits('00000010100101000001111010011100'))
#print(s.reverseBits('11111111111111111111111111111101'))

print(s2.reverseBits(43261596))