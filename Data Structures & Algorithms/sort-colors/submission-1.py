class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict1={0:0,
                1:0,
                2:0}
        for x in nums:
            dict1[x]+=1
        a=dict1[0]
        b=dict1[1]+dict1[0]
        c=dict1[2]
        nums[:a]=[0]*a
        nums[a:b]=[1]*dict1[1]
        nums[b:]=[2]*c
