# Leetcode Problem #1436: Destination City

# Description: You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city. It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        departure, arrival = {}, {}

        for i in paths:
            departure[i[0]] = '.'
            arrival[i[1]] = '.'
        
        print(departure)
        print(arrival)

        for a in arrival:
            if a not in departure:
                return a


s = Solution()

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]     
print(s.destCity(paths))

paths = [["B","C"],["D","B"],["C","A"]]
print(s.destCity(paths))

paths = [["A","Z"]]
print(s.destCity(paths))
