# Leetcode Problem #2135: Number of Laser Beans in a Bank

# Description: Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device. There is one laser beam between any two security devices if both conditions are met: The two devices are located on two different rows: r1 and r2, where r1 < r2; For each row i where r1 < i < r2, there are no security devices in the ith row. Laser beams are independent, i.e., one beam does not interfere nor join with another. Return the total number of laser beams in the bank.

class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        if len(bank) < 2:
            return 0
        left, right, beams, bank_size = 0, 1, 0, len(bank)
        while right < bank_size:
            left_val = bank[left].count('1')
            right_val = bank[right].count('1')
            
            if left_val and right_val:
                beams += left_val * right_val
                left = right
                right += 1
            elif not right_val:
                right += 1
            else:
                left += 1
                right = left + 1

        return beams

class Solution2:
    def numberOfBeams(self, bank: list[str]) -> int:
        num, prev = 0, 0
        for i in bank:
            val = i.count('1')
            if val != 0:
                num += prev * val
                prev = val
        return num

s = Solution()
s2 = Solution2()

bank = ["011001","000000","010100","001000"]
print(s2.numberOfBeams(bank))
bank = ["000","111","000"]
print(s2.numberOfBeams(bank))

