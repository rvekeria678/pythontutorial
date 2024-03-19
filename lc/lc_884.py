# Leetcode Problem #884: Uncommon Words from Two Sentences

# Description: A sentence is a string of single-space separated words where each word consists only of lowercase letters. A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence. Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        common, bank = {}, {}
        s3, ans = (s1+' '+s2).split(), []
        for word in s3:
            if word in bank:
                common[word] = ''
            else:
                bank[word] = ''
        for word in bank:
            if word not in common:
                ans.append(word)
        return ans

s = Solution()

s1 = "this apple is sweet"
s2 = "this apple is sour"
print(s.uncommonFromSentences(s1, s2))

s1 = "apple apple"
s2 = "banana"
print(s.uncommonFromSentences(s1, s2))


