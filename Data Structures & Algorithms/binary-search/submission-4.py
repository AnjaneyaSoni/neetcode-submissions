class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        def find(l,r):
            for x in range(l,r+1):
                if nums[x]==target:
                    return x
                else:
                    continue
            return -1

        l,r,m=0,n-1,n//2 

        while True:                   
            if r-l<4:
                return find(l,r) 
            if nums[m]<target:
                l=m
                m=(l+r)//2
            elif nums[m]>target:
                r=m
                m=(l+r)//2
            elif nums[m]==target:
                return m 
            
