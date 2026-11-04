class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        mydict={}

        thresh=len(nums)//3
        for num in nums:
            if num in mydict:
                mydict[num]+=1
                if mydict[num]>thresh and num not in res :
                    res.append(num)
            else:
                mydict[num]=1
                if mydict[num]>thresh and num not in res :
                    res.append(num)
        return res