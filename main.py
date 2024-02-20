from ctypes import *

class Vec():
    """MyVector"""
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.arr = (c_int * self.capacity)()

    def RemoveOnIndex(self, indx):
        for i in range(indx, self.size - 1):
            self.arr[i] = self.arr[i + 1]

        self.size -= 1
        
    def Insert(self, indx, element):
        if self.size == self.capacity:
            self.ChangeCapacity()

        for i in range(self.size, indx, -1):
            self.arr[i] = self.arr[i - 1]

        self.arr[indx] = element
        self.size += 1

    def Print(self):
        for i in range(self.size - 1):
            print(self.arr[i])

    def Add(self, value):
        if self.size == self.capacity:
            self.ChangeCapacity()
        self.arr[self.size] = value
        self.size += 1
    
    def ChangeCapacity(self):
        new_capcity = self.capacity * 10
        new_arr = (c_int * new_capcity)()

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.capacity = new_capcity
        self.arr = new_arr

    def __setitem__(self, indx, value):
        self.arr[indx] = value
    
    def __getitem__(self, indx):
        return self.arr[indx]
    
    def __len__(self):
        return self.size


vec = Vec()

for i in range(14):
    vec.Add(i)

vec.Insert(2, 99)
vec.Print()
print()
vec.RemoveOnIndex(5)
vec.Print()
print()

print(vec[5])
print()

vec[7] = 1

vec.Print()        