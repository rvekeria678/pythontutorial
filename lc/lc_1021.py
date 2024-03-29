# Leetcode Problem #1021: Remove Outermost Parentheses

# Description: A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation. For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings. A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings. Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings. Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk = []
        res = ''
        l = 0
        for r in range(len(s)):
            if s[r] == ')':
                stk.pop()
                if not len(stk):
                    res += s[l+1:r]
                    l = r + 1
            else:
                stk.append(s[r])
        return res            
    
class Solution2:
    def removeOuterParentheses(self, s: str) -> str:
        count, l, res = 0, 0, ''
        for r in range(len(s)):
            count = count + 1 if s[r] == '(' else count - 1
            if not count:
                res += s[l+1:r]
                l = r + 1
        return res

s = Solution()
s2 = Solution2()

str1 = "(()())(())"
str2 = "(()())(())(()(()))"
str3 = "()()"

print(str1,':',s2.removeOuterParentheses(str1))
print(str2,':',s2.removeOuterParentheses(str2))
print(str3,':',s2.removeOuterParentheses(str3))
