class C:
    pass

c = C()
print(c.__dict__)
c.a = 1
print(c.__dict__)