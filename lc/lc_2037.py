# Leetcode Problem #2037: Minimum Number of Moves to Seat Everyone

# Description: There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student. You may perform the following move any number of times: Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1). Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat. Note that there may be multiple seats or students in the same position at the beginning.

class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])
        return moves
s = Solution()

seats = [3,1,5]
students = [2,7,4]

print(s.minMovesToSeat(seats, students))

seats = [4,1,5,9]
students = [1,3,2,6]

print(s.minMovesToSeat(seats, students))

seats = [2,2,6,6]
student = [1,3,2,6]

print(s.minMovesToSeat(seats, students))

