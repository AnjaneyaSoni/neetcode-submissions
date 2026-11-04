class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        myset=set(nums)
        maxval=0
        start=[]
        for x in myset:
            if (x-1) not in myset:
                start.append(x)
        for x in start:
            temp=1
            while True:
                if x+1 in myset:
                    temp+=1
                    myset.remove(x)
                    x+=1
                    
                else:
                    myset.remove(x)
                    break
            if temp>maxval: maxval=temp


        return maxval