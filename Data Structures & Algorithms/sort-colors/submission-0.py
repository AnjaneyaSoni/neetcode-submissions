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
        nums[:dict1[0]]=[0]*dict1[0]
        nums[dict1[0]:dict1[1]+dict1[0]]=[1]*dict1[1]
        nums[dict1[1]+dict1[0]:]=[2]*dict1[2]
