class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for x in range(len(nums)):
            num1=nums[x]
            t1=target-num1
            if t1 in dict1:
                return [dict1[t1],x]
            else:
                dict1[num1]=x