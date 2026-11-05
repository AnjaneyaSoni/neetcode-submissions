class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        res=[]
        for operation in operations:
            if operation=="+":
                res.append(res[-1]+res[-2])
                
            elif operation=="C":
                del res[-1]
            elif operation=="D":
                res.append(res[-1]*2)
                
            else:
                res.append(int(operation))
            
        return sum(res)