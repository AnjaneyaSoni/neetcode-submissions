class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        myset=set(nums)
        maxval=0
        ind=0
        l=len(nums)
        while nums:
            x=nums[ind]
            if (x-1) not in myset:
                temp=1
                while True:
                    if x+1 in myset:
                        temp+=1
                        myset.remove(x+1)
                        x+=1
                        
                    else:
                        break
                if temp>maxval: maxval=temp
            ind+=1
            if ind==l:
                break
        return maxval