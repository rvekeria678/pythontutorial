# Leetcode Problem #1496: Path Crossing

# Description: Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path. Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coordinates = [0,0]
        seen = {(0,0):''}
        for character in path:     
            if character == 'N':
                coordinates[1] += 1
            elif character == 'E':
                coordinates[0] += 1
            elif character == 'W':
                coordinates[0] -= 1
            else:
                coordinates[1] -= 1
            
            if tuple(coordinates) in seen:
                return True
            else:
                seen[tuple(coordinates)] = ''

        return False

s = Solution()

path = "NES"
print(s.isPathCrossing(path))

path = "NESWW"
print(s.isPathCrossing(path))

path = "SN"
print(s.isPathCrossing(path))