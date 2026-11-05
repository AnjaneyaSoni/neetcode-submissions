class Solution:
    def calPoints(self, operations: List[str]) -> int:
        mysum=0
        res=[]
        for operation in operations:
            if operation=="+":
                res.append(res[-1]+res[-2])
                mysum+=res[-1]
            elif operation=="C":
                mysum-=res.pop()
            elif operation=="D":
                res.append(res[-1]*2)
                mysum+=res[-1]
            else:
                res.append(int(operation))
                mysum+=res[-1]
        return mysum