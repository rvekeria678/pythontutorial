# Leetcode Problem #2391: Minimum Amount of Time to Collect Garbage

# Description: You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute. You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1. There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house. Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything. Return the minimum number of minutes needed to pick up all the garbage.

class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        minutes = sum(travel) * 3
        M, P, G = False, False, False
        for i in range(len(garbage)-1, -1, -1):          
            if 'M' not in garbage[i] and not M and i:
                minutes -= travel[i-1]
            else:
                M = True
            if 'P' not in garbage[i] and not P and i:
                minutes -= travel[i-1]
            else:
                P = True
            if 'G' not in garbage[i] and not G and i:
                minutes -= travel[i-1]
            else:
                G = True
            minutes += len(garbage[i])
        return minutes

s = Solution()

garbage = ["G","P","GP","GG"]
travel = [2,4,3]
print((s.garbageCollection(garbage, travel)))

garbage = ["MMM","PGM","GP"]
travel = [3,10]
print((s.garbageCollection(garbage, travel)))

