class MinStack:

    def __init__(self):
        self.mylist=[]

    def push(self, val: int) -> None:
        if not self.mylist:
            self.mylist.append((val,val))
        else:
            self.mylist.append((val,min(val,self.mylist[-1][1])))

    def pop(self) -> None:
        val,_=self.mylist.pop()
        return val

    def top(self) -> int:
        return self.mylist[-1][0]

    def getMin(self) -> int:
        return self.mylist[-1][1]
        
