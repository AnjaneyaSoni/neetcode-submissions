class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        y=0
        for x in range(1,len(nums)):
            if nums[y]!=nums[x]:
                if x-y>1:
                    nums[y+1]=nums[x]
                y+=1


        return y+1