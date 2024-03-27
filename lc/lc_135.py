# Leetcode Problem #135: Candy

# Description: There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings. You are giving candies to these children subjected to the following requirements: Each child must have at least one candy. Children with a higher rating get more candies than their neighbors. Return the minimum number of candies you need to have to distribute the candies to the children.

class Solution:
    def candy(self, ratings: list[int]) -> int:
        res = 0
        flag = True
        while flag:
            flag = False
            for i in range(len(ratings)):
                ratings[i] -= 1
                if ratings[i] > 0: flag = True
            res += 1
        return res


s = Solution()

ratings = [1,0,2]
print(s.candy(ratings))

ratings = [1,2,2]
print(s.candy(ratings))