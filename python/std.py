'''
class Std:
    rno=7
    name="REX"
    branch="MCA"
    def read(self):
        rno=550
        print('Roll no is=' ,rno)
        print('instance variable=' ,self.rno)
        print("welcome to my class")
obj=Std()
print("rno=",obj.rno)
print("name=",obj.name)
print("branch=",obj.branch)
obj.read()
'''

class parent:
    def display(self):
        print('parent class')
class child(parent):
    def show(self):
        print('child class')
c=child()
c.display()
c.show()