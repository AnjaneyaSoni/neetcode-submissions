class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        n=len(position)
        time = ((target-p)/s for p, s in sorted(zip(position, speed),reverse=True))
        for t in time:
            if not stack:
                stack.append(t)
            elif t>stack[-1]:
                stack.append(t)
        return len(stack)
