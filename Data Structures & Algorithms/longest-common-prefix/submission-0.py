class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        mini=min(strs,key=len)
        length=len(mini)
        for x in range(length):
            for y in strs:
                if y[x]==mini[x]:
                    continue
                else:
                    return prefix
            prefix=prefix+mini[x]
        return prefix
