# Leetcode Problem #1108: Defanging an IP Address

# Description: Given a valid (IPv4) IP address, return a defanged version of that IP address. A defanged IP address replaces every period "." with "[.]".
 
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')

class Solution2:
    def defangIPaddr(self, address: str) -> str:   
        d_address = ""
        for i in address:
            d_address += i if i != '.' else '[.]'
        return d_address

s = Solution()
s2 = Solution2()

address = "1.1.1.1"
print(s.defangIPaddr(address))
print(s2.defangIPaddr(address))

address = "255.100.50.0"
print(s.defangIPaddr(address))
print(s2.defangIPaddr(address))

