class Solution(object):
    def countKeyChanges(self, s):
        return sum(s[i].lower() != s[i - 1].lower() for i in range(1, len(s)))