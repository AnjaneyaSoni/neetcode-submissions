class MyHashMap:

    def __init__(self):
        self.list1=[]
        self.list2=[]

    def put(self, key: int, value: int) -> None:
        if key in self.list1:
            self.list2[self.list1.index(key)]=value
        else:
            self.list1.append(key)
            self.list2.append(value)
    def get(self, key: int) -> int:
        if key in self.list1:
            return self.list2[self.list1.index(key)]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.list1:
            del self.list2[self.list1.index(key)]
            self.list1.remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)