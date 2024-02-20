# Leetcode Problem #2325: Decode the Message

# Description: You are given the strings key and message, which represent a cipher key and a secret message, respectively. Returnt the decoded message.

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        decoder = {}
        decoded_text = ""
        pos = 0

        for i in key:
            if i != ' ' and i not in decoder:
                decoder[i] = letters[pos]
                pos += 1        
        for char in message:
            if char != ' ':
                decoded_text += decoder[char]
            else:
                decoded_text += ' '
        return decoded_text


s = Solution()

key1 = "the quick brown fox jumps over the lazy dog"
msg1 = "vkbs bs t suepuv"

key2 = "eljuxhpwnyrdgtqkviszcfmabo"
msg2 = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"

print("'"+s.decodeMessage(key1,msg1)+"'")
print("'"+s.decodeMessage(key2,msg2)+"'")