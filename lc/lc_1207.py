# Leetcode Problem #1207: Unique Number of Occurrences

# Description: Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:  
        freq, temp = {}, {}
        for number in arr:
            if number in temp:
                temp[number] += 1
            else:
                temp[number] = 1
            if temp[number] in freq:
                freq[temp[number]] += 1
                if temp[number]-1:
                    freq[temp[number]-1] -= 1
            else:
                freq[temp[number]] = 1
                if temp[number]-1:
                    freq[temp[number]-1] -= 1
        for occurences in freq:
            if freq[occurences] > 1:
                return False
        return True
            
s = Solution()

arr = [1,2,2,1,1,3]
print(s.uniqueOccurrences(arr))

arr = [1,2]
print(s.uniqueOccurrences(arr))

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(s.uniqueOccurrences(arr))
