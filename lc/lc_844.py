# Leetcode Problem #844: Backspace String Compare

# Description: Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character. Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack, t_stack = [], []
        for character in s:
            if character == '#' and len(s_stack):
                s_stack.pop()
            elif character != '#':
                s_stack.append(character)
        for character in t:
            if character == '#' and len(t_stack):
                t_stack.pop()
            elif character != '#':
                t_stack.append(character)
        return ''.join(s_stack) == ''.join(t_stack)

s = Solution()        

st = "ab#c"
t = "ad#c"
print(s.backspaceCompare(st, t))

st = "ab##"
t = "c#d#"
print(s.backspaceCompare(st, t))

st = "a#c"
t = "b"
print(s.backspaceCompare(st, t))

st = "y#fo##f"
t = "y#f#o##f"
print(s.backspaceCompare(st, t))