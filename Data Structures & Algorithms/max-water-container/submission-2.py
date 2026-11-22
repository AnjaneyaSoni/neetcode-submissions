class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxi=0
        maxi=max(maxi,min(heights[l],heights[r])*(r-l))
        while r>l:
            if heights[l]<heights[r]:   
                maxi=max(maxi,heights[l]*(r-l))            
                l+=1               
            elif heights[l]>heights[r]:
                maxi=max(maxi,heights[r]*(r-l))
                r-=1                
            else:
                maxi=max(maxi,heights[r]*(r-l))
                l+=1
                r-=1
                
            

                

        return maxi
