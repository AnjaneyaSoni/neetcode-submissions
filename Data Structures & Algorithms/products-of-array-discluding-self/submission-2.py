class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            res=[1]
            prod=nums[-1]
            l=len(nums)
            for x in range (l-1):
                res.append(res[x]*nums[x])
            
            for x in range(l-2,-1,-1):
                res[x]=prod*res[x]
                prod=prod*nums[x]
            return res