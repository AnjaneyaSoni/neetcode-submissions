class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=1
        time = ((target-p)/s for p, s in sorted(zip(position, speed),reverse=True))        
        slowest=next(time)
        for t in time:
            if t>slowest:
                slowest=t
                fleet+=1
            
        return fleet
