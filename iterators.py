class TopTen:

    def __init__(self) -> None:
        self.num=1
    def __iter__(self): #initializes and return thr iterator object
        print(self)
        return self
    def __next__(self):
        if (self.num<=10):
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration


itera=iter(TopTen())

# print(next(itera))
# print(next(itera))
# print(next(itera))

for i in itera:
    print(i)