class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=set()
        mydict={}

        thresh=len(nums)//3
        for num in nums:
            if num in mydict:
                mydict[num]+=1
                if mydict[num]>thresh and num not in res :
                    res.add(num)
            else:
                mydict[num]=1
                if mydict[num]>thresh and num not in res :
                    res.add(num)
        return list(res)