class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        for i,c in enumerate(nums):
            if c in window:
                return True
            else:
                window.add(c)
            if len(window)>k:
                window.remove(nums[i-k])  
        return False