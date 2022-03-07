# __eq__
# It is a comparison expression for objects.
# "__eq__"  is called when you compare it using "==" symbol
# __lt__ less than "<"
# __le__ less or equal "<="
# ...

class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):  # It is called when you compare it.
        print("Called")
        if isinstance(other, Student):  # Boolean, in this case, Whether other is Student or not.
            if other.name == self.name:
                return True
        return False

    def __le__(self, other):
        print(2)
        return False


divyansh = Student("Divyansh")
shivansh = Student("Divyansh")

print(divyansh == shivansh)
print(divyansh is shivansh)
print(divyansh <= shivansh)  # it works : Cause you defined __le__
print(divyansh < shivansh)  # error : Cause it is impossible know which one is greater
