class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        new=[]
        new1=[]
        new2=[]
        while nums:
            max=-50000
            min=50000
            for x in range(len(nums)//2+(1 if len(nums)%2==1 else 0)):
                if nums[x]<min:
                    min=nums[x]
                if nums[-1-x]<min:
                    min=nums[-1-x]
                if nums[x]>max:
                    max=nums[x]
                if nums[-1-x]>max:
                    max=nums[-1-x]
                
            if max!=min:
                nums.remove(min)
                nums.remove(max)
                new1.append(min)
                new2.append(max)
            else:
                nums.remove(min)
                new1.append(min)
        new=new1+new2[::-1]
        return new