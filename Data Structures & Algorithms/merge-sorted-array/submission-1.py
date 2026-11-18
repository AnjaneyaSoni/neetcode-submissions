class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j=0,0
        copy1=nums1[:m]
        
        while True:
            if i!=n and j!=m:
                if nums2[i]<copy1[j]:
                    nums1[i+j]=nums2[i]
                    i+=1
                else:
                    nums1[i+j]=copy1[j]
                    j+=1
            elif i==n and j!=m:
                nums1[i+j]=copy1[j]
                j+=1
            elif j==m and i!=n:
                nums1[i+j]=nums2[i]
                i+=1
            
            else:
                break
        
