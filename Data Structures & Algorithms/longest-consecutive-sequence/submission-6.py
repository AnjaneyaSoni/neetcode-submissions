class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset=set(nums)
        maxval=0
        
        for x in myset:
            if (x-1) not in myset:  
                temp=1
                while x+1 in myset:
                    temp+=1
                    x+=1                    

                if temp>maxval: maxval=temp


        return maxval