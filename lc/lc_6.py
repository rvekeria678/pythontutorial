# Leetcode Problem #6: Zigzag Conversion

# Description: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) And then read line by line: "PAHNAPLSIIGYIR". Write the code that will take a string and make this conversion given a number of rows:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        switch = False
        grid = [[] * len(numRows)]
        for i in range(len(s)):
            if not i % numRows:
                switch = not switch
            

s = Solution()        

line = "PAYPALISHIRING"
numRows = 3
print(s.convert(line, numRows))

line = "PAYPALISHIRING"
numRows = 4
print(s.convert(line, numRows))

line = "A"
numRows = 1
print(s.convert(line, numRows))
