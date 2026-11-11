class parent:
    def fun1(self):
        print('this function is in parent class')
class child1(parent):
    def fun2(self):
        print("this function is in child 1")
class child2(parent):
    def fun3(self):
        print("this function is in child_2")

obj1=child1()
obj2=child2()
obj1.fun1()
obj1.fun2()
obj2.fun1()
obj2.fun3()


