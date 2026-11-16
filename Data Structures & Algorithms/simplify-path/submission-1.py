class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path=[]
        low=0
        x=1
        path=path+"/"
        n=len(path)
        while x<n:
            if path[x]=="/":
                if (x-low)==1:
                    low=x
                else:
                    word=path[low+1:x]
                    if word=="..":
                        if new_path:
                            new_path.pop()
                    elif word!=".":
                        new_path.append(word)
                    low=x
            x+=1
            

        return "/"+"/".join(new_path)
              