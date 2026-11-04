class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        myset=set(nums)
        maxval=0
        
        for x in myset:
            if (x-1) not in myset:  
                temp=1
                while True:
                    if x+1 in myset:
                        temp+=1
                        x+=1                    
                    else:
                        break
                if temp>maxval: maxval=temp


        return maxval