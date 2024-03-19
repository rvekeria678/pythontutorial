# Leetcode Problem #2062: Count Vowel Substrings of a String

# Description: A substring is a contiguous (non-empty) sequence of characters within a string. A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it. Given a string word, return the number of vowel substrings in word.

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        left, right, count = 0,0,0
        vowels = 'aeiou'
        size = len(word)
        while left <= size - len(vowels):
            if word[left] not in vowels:
                left += 1
            if right < size and word[right] in vowels:
                right += 1
                if len(set(word[left:right])) >= len(vowels):
                    count += 1
            elif left < right:
                left += 1
                right = left + 1
            else:
                right += 1
                left = right
        return count
    
class Solution2:
    def countVowelSubstrings(self, word: str) -> int:
        left, right, count = 0,0,0
        vowels = 'aeiou'
        vowel_size, size = len(vowels), len(word)
        while left <= size - vowel_size:
            if word[left] not in vowels:
                left += 1
                right = left
            else:
                if right < size and word[right] in vowels:
                    right += 1
                    if len(set(word[left:right])) >= vowel_size:
                        count += 1
                elif left < right:
                    left += 1
                    right = left + 1
                else:
                    right += 1
        return count

s = Solution()
s2 = Solution2()

word = "aeiouu"
print(s2.countVowelSubstrings(word))

word = "unicornarihan"
print(s2.countVowelSubstrings(word))

word = "cuaieuouac"
print(s2.countVowelSubstrings(word))

word = "poazaeuioauoiioaouuouaui"
print(s2.countVowelSubstrings(word))




