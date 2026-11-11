class a:
    def __init__(self,a):
        self.a=a
    def __sub__(self,o):
        return self.a+o.a

ob1=a(1)
ob2=a(2)
ob3=a("geeks")
ob4=a("for")

print(ob1 - ob2)
# print(ob3 + ob4)