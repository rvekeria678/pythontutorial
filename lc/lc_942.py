# Leetcode Problem #942: DI String Match

# Description: A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where: s[i] == 'I' if perm[i] < perm[i + 1], and s[i] == 'D' if perm[i] > perm[i + 1]. Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        small, large = 0, len(s)
        res = []
        for i in s:
            if i == 'I':
                res.append(small)
                small += 1
            else:
                res.append(large)
                large -= 1
        res.append(small)

        return res

s = Solution()

seq = "IDID"
print(s.diStringMatch(seq))
seq = "III"
print(s.diStringMatch(seq))

seq = "DDI"
print(s.diStringMatch(seq))
