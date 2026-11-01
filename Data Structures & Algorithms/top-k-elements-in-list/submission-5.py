class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        key1=0
        dict2={}
        max=1001
        

        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1

        for x in range(k):
            min=-1001
            for ki,v in dict1.items():
                if v>min and v<max:
                    min=v
                    key1=ki
                elif v==max:
                    if ki not in dict2:
                        dict2[ki]=v
                        continue
            max =min
            dict2[key1]=min
        return list(dict2.keys())[:k]