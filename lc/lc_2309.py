# Leetcode Problem #2309: Greatest English Letter in Uppder and Lower Case

# Description: Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string. An English letter b is greater than another letter a if b appears after a in the English alphabet.

class Solution:
    def greatestLetter(self, s: str) -> str:
        matches = {}
        greatest = ''
        for character in s:
            if character in matches:
                greatest = max(greatest.upper(), character.upper())
            else:
                if character.islower():
                    matches[character.upper()] = ''
                else:
                    matches[character.lower()] = ''
        return greatest 

s = Solution()        

st = "lEeTcOdE"
print(s.greatestLetter(st))

st = "arRAzFif"
print(s.greatestLetter(st))

st = "AbCdEfGhIjK"
print(s.greatestLetter(st))
