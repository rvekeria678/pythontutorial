# Leetcode Problem #917: Reverse Only Letters

# Description: Given a string s, reverse the string according to the following rules: All the characters that are not English letters remain in the same position, All the English letters (lowercase or uppercase) should be reversed. Return s after reversing it.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stk = []
        res = ""
        for i in range(len(s)):
            if s[i].isalpha():
                stk.append(s[i])

        for i in range(len(s)):
            if not s[i].isalpha():
                res += s[i]
            else:
                res += stk.pop()
        return res     
           
s = Solution()

str1 = "ab-cd"
str2 = "a-bC-dEf-ghIj"
str3 = "Test1ng-Leet=code-Q!"

print(s.reverseOnlyLetters(str1))
print(s.reverseOnlyLetters(str2))
print(s.reverseOnlyLetters(str3))
