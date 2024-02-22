# Leetcode Problem #804: Unique Morse Code Words

# Description: International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes. Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word. Return the number of different transformations among all words we have.

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        transformations = []
        morse_table = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}

        for word in words:
            morse_word = ""
            for letter in word:
                morse_word += morse_table[letter]
            transformations.append(morse_word)

        return len(set(transformations))

s = Solution()

words1 = ["gin","zen","gig","msg"]
words2 = ["a"]

print(s.uniqueMorseRepresentations(words1))
print(s.uniqueMorseRepresentations(words2))