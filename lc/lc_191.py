# Leetcode Problem #191: Number of 1 Bits

# Description: Write a function that takes the binary representation of an unsigned integer and returns the nubmer of '1' bits is has (alsno known as the Hamming weight)

class Solution:
    def hammingWeight(self, n: int) -> int:
        b_string = str(bin(n))[2::]

        print(b_string, ',', type(b_string))
        count = 0

        for i in len(b_string):
            if b_string[0] == '1':
                count += 1

        return count

class Solution2:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count
    
s = Solution()
s2 = Solution2()

print(s2.hammingWeight(11))
print(s2.hammingWeight(128))
print(s2.hammingWeight(2147483645))