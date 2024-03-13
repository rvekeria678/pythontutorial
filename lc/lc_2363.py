# Leetcode Problem #2363: Merge Similar Items

# Description: You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties: items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item, The value of each item in items is unique. Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei. (Note: ret should be returned in ascending order by value.)

class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        d = {}
        for item in items1:
            if item[0] in d: d[item[0]] += item[1]
            else: d[item[0]] = item[1]
        for item in items2:
            if item[0] in d: d[item[0]] += item[1]
            else: d[item[0]] = item[1]
        d = sorted(d.items())
        return d

s = Solution()

items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
print(s.mergeSimilarItems(items1, items2))

items1 = [[1,1],[3,2],[2,3]]
items2 = [[2,1],[3,2],[1,3]]
print(s.mergeSimilarItems(items1, items2))

items1 = [[1,3],[2,2]]
items2 = [[7,1],[2,2],[1,4]]
print(s.mergeSimilarItems(items1, items2))

