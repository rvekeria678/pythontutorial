# Leetcode Problem #1974: Minimum Time to Type Word Using Special Typewriter

# Description: There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'. Each second, you may perform one of the following operations: Type the character the pointer is currently on, Move the pointer one character counterclockwise or clockwise. Given a string word, return the minimum number of seconds to type out the characters in word.

class Solution:
    def minTimeToType(self, word: str) -> int:
        start = seconds = 0
        for character in word:            
            clockwise = abs(start + 97 - ord(character))
            counter_clockwise = 26 - clockwise
            seconds += min(clockwise, counter_clockwise) + 1
            start = ord(character) - 97
        return seconds


s = Solution()

word = "abc"
print(s.minTimeToType(word))

word = "bza"
print(s.minTimeToType(word))

word = "zjpc"
print(s.minTimeToType(word))