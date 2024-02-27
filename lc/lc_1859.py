# Leetcode Problem #1859: Sorting the Sentence

# Description: A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters. A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence. For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3". Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        sentence = [''] * len(s)
        for i in s:
            sentence[int(i[len(i)-1])-1] = i[:len(i)-1]
        return ' '.join(sentence)


s = Solution()

str1 = "is2 sentence4 This1 a3"
str2 = "Myself2 Me1 I4 and3"

print(s.sortSentence(str1))
print(s.sortSentence(str2))
