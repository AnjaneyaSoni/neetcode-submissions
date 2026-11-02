class Solution:

    def encode(self, strs: List[str]) -> str:
       
            return "Ω".join(strs) if strs else "empty"
    def decode(self, s: str) -> List[str]:
        
        return s.split("Ω") if s!="empty" else []
