class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        n1=len(word1)
        n2=len(word2)
        if n1>n2:
            for i,c in enumerate(word2):
                ans.extend([word1[i],c])
            for x in range(n2,n1):
                ans.append(word1[x])
        elif n2>n1:
            for i,c in enumerate(word1):
                ans.extend([c,word2[i]])
            for x in range(n1,n2):
                ans.append(word2[x])
        else:
            for i,c in enumerate(word1):
                ans.extend([c,word2[i]])
        return "".join(ans)