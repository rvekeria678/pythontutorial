# Leetcode Problem #2389: Longest Subsequence With Limited Sum

# Description: You are given an integer array nums of length n, and an integer array queries of length m. Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i]. A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        answer = [0] * len(queries)
        for id, query in enumerate(queries):
            spec_sum = 0
            for i, number in enumerate(sorted(nums)):
                spec_sum += number

                if spec_sum <= query:
                    answer[id] += 1
                else:
                    break

        return answer

s = Solution()

nums = [4,5,2,1]
queries = [3,10,21]
print(s.answerQueries(nums, queries))

nums = [2,3,4,5]
queries = [1]
print(s.answerQueries(nums, queries))
