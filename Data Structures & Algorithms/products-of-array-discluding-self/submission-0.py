class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            flist=[1]
            blist=[1]
            l=len(nums)
            for x in range (l):
                flist.append(flist[x]*nums[x])
                blist.append(blist[x]*nums[-x-1])
           
            return [flist[x]*blist[-x-2] for x in range(l)]
