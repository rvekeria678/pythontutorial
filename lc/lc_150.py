# Leetcode Problem #134: Gas Station:

# Description: There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i]. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations. Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        max_so_far = 0
        max_ending_here = 0
        net = []
        start = 0
        tank = 0
        # Finds gas - cost for the ith value
        for i in range(len(gas)):
            net.append(gas[i] - cost[i])
        # Kadane's Algorithm (Finds the largest subarray)
        for i in range(len(net)):
            if not max_ending_here:
                start = i
            max_ending_here += net[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        # Determins if travel is possible given best start
        for i in range(len(net)):
            tank += net[(start + i) % len(net)]
            if tank < 0:
                return -1
        return start
            

s = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(s.canCompleteCircuit(gas, cost))

gas = [2,3,4]
cost = [3,4,3]
print(s.canCompleteCircuit(gas, cost))