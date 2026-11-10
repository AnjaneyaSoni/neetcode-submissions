class StockSpanner:

    def __init__(self):
        self.temp=[]

    def next(self, price: int) -> int:
        if not self.temp:
            self.temp.append(price)
            return 1
        else:
            if self.temp[-1]<=price:
                for x in range(-1,-len(self.temp)-1,-1):
                    if self.temp[x]>price:
                        self.temp.append(price)
                        return abs(x)                   
                    
                self.temp.append(price)
                return len(self.temp)
                
            else:
                self.temp.append(price)
                return 1
                

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)