# Leetcode Problem #2810: Faulty Keyboard

# Description: Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have written. Typing other characters works as expected. You are given a 0-indexed string s, and you type each character of s using your faulty keyboard. Return the final string that will be present on your laptop screen.

class Solution:
    def finalString(self, s: str) -> str:
        t_str = ''
        for i,j in enumerate(s):
            if j == 'i':
                t_str = t_str[:i][::-1] + t_str[i:]
            else:
                t_str += j
        return t_str

s = Solution()

str1 = "string"
str2 = "poiinter"

print(s.finalString(str1))
print(s.finalString(str2))

