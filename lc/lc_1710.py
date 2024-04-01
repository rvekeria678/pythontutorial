# Leetcode Problem #1710: Maximum Units on a Truck

# Description: You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]: numberOfBoxesi is the number of boxes of type i ; numberOfUnitsPerBoxi is the number of units in each box of the type i. You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize. Return the maximum total number of units that can be put on the truck.

class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        sorted_boxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        number_of_units = number_of_boxes = largest_stocked = 0
        while number_of_boxes < truckSize:
            if sorted_boxes[largest_stocked][0]:
                number_of_boxes += 1
                number_of_units += sorted_boxes[largest_stocked][1]
                sorted_boxes[largest_stocked][0] -= 1
            else:
                largest_stocked += 1
                if largest_stocked >= len(sorted_boxes):
                    break
        return number_of_units

s = Solution()

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(s.maximumUnits(boxTypes, truckSize))

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
print(s.maximumUnits(boxTypes, truckSize))

