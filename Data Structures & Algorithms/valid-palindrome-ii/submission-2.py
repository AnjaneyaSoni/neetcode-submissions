class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        def palindrone(l,r,s):
            while l<r:
                if s[l]!=s[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True
        while l<r :
            if s[l]!=s[r]:
                return True if palindrone(l+1,r,s) or palindrone(l,r-1,s) else False
            else:
                l+=1
                r-=1


        return True