class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        
        return type(class_name, bases, attrs)

        
        
class Dog(metaclass=Meta):
    x = 5
    y = 8


    def hello(self):
        print("hi")