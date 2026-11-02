class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prime_dict = {
    'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 
    'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 
    'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 
    'y': 97, 'z': 101
                     }
        nums=[]
        dict1={}
        for x in strs:
            temp=1
            for y in x:
                temp=temp*prime_dict[y]
            nums.append(temp)
        temp=0
        for x in nums:
            if x in dict1:
                dict1[x].append(strs[temp])
                
            else:
                dict1[x]=[strs[temp]]
            temp+=1
        return [v for v in dict1.values()]