class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,-1
        s=s.lower()
        n=len(s)
        m=0
        while m<=n//2 and l<n and r>-n:
            if s[l].isalpha() or s[l].isdigit():
                if s[r].isalpha() or s[r].isdigit():
                    if s[l]!=s[r]:
                        return False
                    m+=1
                    r+=-1
                    l+=1
                else:
                    r+=-1
            else:
                l+=1

        return True