    # -*- coding:UTF-8 -*-
#! /usr/bin/python3
class myNumbers:
    def __iter__(self):
        self.a = 10
        return self
    def __next__(self):
        if self.a <20:
            x = self.a
            self.a += 3
            return x
        else:
            raise StopIteration

Number_1 = myNumbers()
iter_1 = iter(Number_1)

print(next(iter_1))
print(next(iter_1))
print( )
for x in iter_1:
    print(x)

print(type(iter_1))