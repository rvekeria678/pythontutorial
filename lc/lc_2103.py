# Leetcode Problem #2103: Rings and Rods

# Description: There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9. You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where: The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B'), The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9'). For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1. Return the number of rods that have all three colors of rings on them.

class Solution:
    def countPoints(self, rings: str) -> int:
        dict = {'R':[], 'G':[], 'B':[]}
        points = 0
        for i in range(len(rings)):
            if rings[i].isdigit():
                if rings[i] not in dict[rings[i-1]]:
                    dict[rings[i-1]].append(rings[i])
        for i in dict['R']:
            if i in dict['G'] and i in dict['B']:
                points += 1
        return points

s = Solution()

rings = "B0B6G0R6R0R6G9"
print(s.countPoints(rings))

rings = "B0R0G0R9R0B0G0"
print(s.countPoints(rings))

rings = "B7R5B3G5B1R2B8"
print(s.countPoints(rings))
