# __str__ is called when you call it.
# __str__ has "return"
# __str__ has a higher priority than __repr__
class A:
    def __str__(self):  # Overriding
        print("You called it")
        return 'str method is called'

    def __repr__(self): # It doesn't work.
        print("repr!!")
        return "!!!!!!!!"

class B:
    def __repr__(self):
        print("repr!!")
        return "!!!!!!!!"


a = A()
print(a)

a2 = a.__str__() # return

b = B()
print(B)
print(b)
