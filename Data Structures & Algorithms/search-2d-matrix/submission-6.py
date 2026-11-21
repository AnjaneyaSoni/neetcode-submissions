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

        l2,r=0,len(matrix[l])-1
        m=(l2+r)//2

        while l2<=r:
            if matrix[l][m]>target:
                r=m-1  
            elif matrix[l][m]<target:
                l2=m+1
            else:
                return True
            m=(r+l2)//2
        return False