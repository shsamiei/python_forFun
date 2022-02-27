class Reverse:
    # TO DO
    x = 0 
    def __init__(self ,list):
        self.list = list
        
        
    pass

    def __iter__(self):
        # self.itr = self.list[len(self.list)-1]
        self.x = len(self.list)
        return self 

    def __next__(self):
        self.x = self.x - 1 
        if self.x != -1 : 
            return self.list[self.x]
        else :
            raise StopIteration
        

ls = [10, 20, 30]


for it in Reverse(ls):
    print(it)
print(ls)