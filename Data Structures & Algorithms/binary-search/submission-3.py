class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if n<4:
            for x in range(n):
                if nums[x]==target:
                    return x
                else:
                    continue
            return -1
        l,r,m=0,n-1,n//2
        while True:
            

            if nums[m]==target:
                return m
            elif r-l<4:
                for x in range(l,r+1):
                    if nums[x]==target:
                        return x
                    else:
                        continue
                return -1

               
            elif nums[m]<target:
                l=m
                m=(l+r)//2
            elif nums[m]>target:
                r=m
                m=(l+r)//2
            
