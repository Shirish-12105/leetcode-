class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        for i in range(min(len(s) for s in strs)):
            for j in range(1,len(strs)):
                if(strs[0][i] != strs[j][i]):
                    return prefix
            prefix = prefix + strs[0][i]
        return prefix   