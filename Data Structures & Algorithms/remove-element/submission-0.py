class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:     
        dup=0
        for i,x in enumerate(nums):
            if x!=val:
                nums[i-dup]=x
            else:
                dup+=1
        return len(nums)-dup
