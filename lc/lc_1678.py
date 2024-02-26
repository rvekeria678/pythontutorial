# Leetcode Problem #1678: Goal Parser Interpretation

# Description: You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order. Given the string command, return the Goal Parser's interpretation of command.

class Solution:
    def interpret(self, command: str) -> str:
        ignore = '(al'
        i_str = ""
        for i in range(len(command)):
            if command[i] == ')':
                i_str += 'o' if command[i-1] == '(' else 'al'
            elif command[i] not in ignore:
                i_str += command[i]        
        return i_str
    
class Solution2:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)', 'al')

s = Solution()
s2 = Solution2()

command = "G()(al)"
print(s.interpret(command))
print(s2.interpret(command))

command = "G()()()()(al)"
print(s.interpret(command))
print(s2.interpret(command))

command = "(al)G(al)()()G"
print(s.interpret(command))
print(s2.interpret(command))
