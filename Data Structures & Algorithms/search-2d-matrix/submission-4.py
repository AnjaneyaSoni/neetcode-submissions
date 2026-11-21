class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)
        m=(l+r)//2
        while (r-l)>1:
            if matrix[m][0]<target:
                l=m
            elif matrix[m][0]>target:
                r=m
            else:
                return True
            m=(r+l)//2
        if target in matrix[l]:
            return True 
        else:
            return False