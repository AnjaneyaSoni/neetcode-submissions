class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=0
        cars=list(zip(position, speed))
        cars.sort(reverse=True)      
        slowest=0.0
        for p,s in cars:
            t=(target-p)/s
            if t>slowest:
                slowest=t
                fleet+=1
            
        return fleet
