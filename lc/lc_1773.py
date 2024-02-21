# Leetcode Probem 1773: Count Items Matching a Rule

# Description: You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.

# ruleKey == "color" and ruleValue == colori.

# ruleKey == "name" and ruleValue == namei.

# Return the number of items that match the given rule.

class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        dict = {"type": 0, "color": 1, "name": 2}
        count = 0
        for i in items:
            if i[dict[ruleKey]] == ruleValue:
                count += 1
        return count

s = Solution()

items1 = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey1 = "color"
ruleValue1 = "silver"

items2 = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey2 = "type"
ruleValue2 = "phone"

print(s.countMatches(items1, ruleKey1, ruleValue1))
print(s.countMatches(items2, ruleKey2, ruleValue2))