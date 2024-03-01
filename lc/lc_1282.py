# Leetcode Problem #1282: Group the People Given the Group Size They Belong To

# Description: There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1. You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3. Return a list of groups such that each person i is in a group of size groupSizes[i]. Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        d, res= {}, []
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d:
                d[groupSizes[i]] = [i]
            else:
                d[groupSizes[i]].append(i)
        for n in d:
            for j in range(0,len(d[n]),n):
                res.append(d[n][j:j+n])

        return res

s = Solution()

groupSizes1 = [3,3,3,3,3,1,3]
groupSizes2 = [2,1,3,3,3,2]

print(s.groupThePeople(groupSizes1))
print(s.groupThePeople(groupSizes2))
