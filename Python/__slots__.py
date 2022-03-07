class D:
    __slots__ = {'x', 'y'}


d = D()
# print(d.__dict__)  #It is an error code,
print(d.__slots__)

d.x = 1
print(d.x)

d.a = 1  # It is also an error code, there is no slot for 'a'
