class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        l=len(asteroids)
        x=0
        while x<l:
            if not res:
                res.append(asteroids[x])
                x+=1
            elif res[-1]<0:
                res.append(asteroids[x])
                x+=1
            elif res[-1]>0:
                if asteroids[x]>0:
                    res.append(asteroids[x])
                    x+=1
                elif asteroids[x]<0:
                    if abs(asteroids[x])>res[-1]:
                        res.pop()

                    elif abs(asteroids[x])<res[-1]:
                        x+=1

                    elif abs(asteroids[x])==res[-1]:
                        res.pop()
                        x+=1
                    
        return res