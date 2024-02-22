# Leetcode Problem #1282: Group the People Given the Group Size They Belong To

# Description: There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1. You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3. Return a list of groups such that each person i is in a group of size groupSizes[i]. Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        left, right = 0,1
        selected, group = [], []

        while left <= len(groupSizes) - 1:
            size = groupSizes[left]
            #print(left, right)
            while size and left not in selected and right < len(groupSizes):
                if groupSizes[left] == groupSizes[right] and groupSizes[right] not in selected:
                    size -= 1
                    selected.append(right)
                    group.append(right)
                right += 1
            left += 1
            right = left + 1
            print(group)
            group = []
        return group
s = Solution()

groupSizes1 = [3,3,3,3,3,1,3]
groupSizes2 = [2,1,3,3,3,2]

print(s.groupThePeople(groupSizes1))
print(s.groupThePeople(groupSizes2))
