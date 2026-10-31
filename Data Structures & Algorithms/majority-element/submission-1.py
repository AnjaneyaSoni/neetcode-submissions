class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       
        n=len(nums)
        counts={}
        for x in nums:
            counts[x]=counts.get(x,0)+1

        counts=Counter(nums)
        set1=set(nums)
        for x in set1:
            if counts[x]>(n/2):
                return x
        