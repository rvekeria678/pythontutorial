# Leetcode Problem #1974: Minimum Time to Type Word Using Special Typewriter

# Description: There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'. Each second, you may perform one of the following operations: Type the character the pointer is currently on, Move the pointer one character counterclockwise or clockwise. Given a string word, return the minimum number of seconds to type out the characters in word.

class Solution:
    def minTimeToType(self, word: str) -> int:
        pointer = seconds = 0
        for character in word:
            print(chr(pointer+97), "->", character)
            print('Clockwise:', abs(pointer - (ord(character)-97)))
            print('Counter Clockwise:', abs((ord('a')-97) - pointer) + (ord(character)-97))
            
            print("Move and Print:",min(abs(pointer - (ord(character)-97)), abs((ord('z')-97) - pointer + (ord(character)-97))) + 1)
            
            seconds += min(abs(pointer - (ord(character)-97)), abs(0 - pointer) + abs(ord(character)-97)-ord('z')-97) + 1
            print('seconds: ', seconds, '\n')
            pointer += ord(character) - 97
        return seconds


s = Solution()

word = "abc"
print(s.minTimeToType(word))

word = "bza"
print(s.minTimeToType(word))
