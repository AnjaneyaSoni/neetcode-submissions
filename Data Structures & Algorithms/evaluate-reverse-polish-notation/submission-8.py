class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        newlist=[]
       
   
        for token in tokens:
            
            if token in {"+", "-", "*", "/"}:
                b=newlist.pop()
                a=newlist.pop()
                if token=="+":
                    newlist.append(a+b)
                elif token=="*":
                    newlist.append(a*b)
                elif token=="-":
                    newlist.append(a-b)
                else:
                    newlist.append(int(a/b))                 
            else:
                newlist.append(int(token))
        
        return newlist[0]