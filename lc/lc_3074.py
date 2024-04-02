# Leetcode Problem #3074: Apple Redistribution Into Boxes

# Description: You are given an array apple of size n and an array capacity of size m. There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples. Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes. (Note that, apples from the same pack can be distributed into different boxes.)

class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity = sorted(capacity, reverse=True)
        number_of_boxes = current_capacity = 0
        total_number_of_apples = sum(apple)
        while total_number_of_apples > current_capacity:
            current_capacity += capacity[number_of_boxes]
            number_of_boxes += 1
        return number_of_boxes

s = Solution()

apple = [1,3,2]
capacity = [4,3,1,5,2]
print(s.minimumBoxes(apple, capacity))

apple = [5,5,5]
capacity = [2,4,2,7]
print(s.minimumBoxes(apple, capacity))
