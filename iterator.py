class Reverse:
    # TO DO
    def __init__(self ,list):
        self.list = list
    pass

    def __iter__(self):
        return self.list[len(self.list)]

    def __next__(self):
        pass

ls = [10, 20, 30]

it = iter(ls)
print(type(it))
print(type(next(it)))

# for it in Reverse(ls):
#     print(it)
# print(ls)