class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        n=len(nums)
        counts=Counter(nums)
        set1=set(nums)
        for x in set1:
            if counts[x]>(n/2):
                return x
        