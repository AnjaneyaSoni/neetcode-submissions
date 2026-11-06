class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        x=0
        while x<len(asteroids):
            asteroid=asteroids[x]
            if not res:
                res.append(asteroid)
                x+=1
                continue
            last=res[-1]
            if last<0:
                res.append(asteroid)
                x+=1
            elif last>0:
                if asteroid>0:
                    res.append(asteroid)
                    x+=1
                elif asteroid<0:
                    if abs(asteroid)>last:
                        res.pop()

                    elif abs(asteroid)<last:
                        x+=1

                    elif abs(asteroid)==last:
                        res.pop()
                        x+=1
                    
        return res