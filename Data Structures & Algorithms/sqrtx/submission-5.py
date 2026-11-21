class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        l,r=1,(x//2)+1
        while l<=r:
            m=(l+r)//2
            if m*m>x:
                r=m-1
            elif m*m<x:
                l=m+1
            else:
                return m
        return l-1