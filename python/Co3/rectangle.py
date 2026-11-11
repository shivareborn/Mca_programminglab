#Create a class Rectangle with private attributes length and width .Overload'<' operator compare the area of 2 rectangle.

class rect:
    def __init__(self):
        self.__l = int(input("Enter length of the rectangle :"))
        self.__b = int(input("Enter breadth of the rectangle:"))
    def __lt__(ob1,ob2):
        area1 = ob1 = ob1.__l*ob1.__b
        area2 = ob1 = ob2.__l*ob2.__b
        print("area of r1",area1)
        print("area of r2",area2)
        return area1<area2
print("enter the length and breadth of first object ")
ob1 = rect()
print("enter the length and breadth of second object ")
ob2=rect()
if ob1>ob2:
    print("rectangle1 is greater than rectangle2")
else:
    print("rerctangle1 is less than or equal to rectangle2")