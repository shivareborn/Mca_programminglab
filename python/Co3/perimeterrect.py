class Rectangle:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth

    def area(self):
        return self.l * self.b

    def peri(self):
        return 2 * (self.l + self.b)
    def compare(self, obj2):
        if self.area() == obj2.area():
            print("Both areas are equal.")
        elif self.area() > obj2.area():
            print("Area of the 1st rectangle is greater.")
        else:
            print("Area of the 2nd rectangle is greater.")

l1 = int(input("Enter the length of first rectangle: "))
b1 = int(input("Enter the breadth of first rectangle: "))
l2 = int(input("Enter the length of second rectangle: "))
b2 = int(input("Enter the breadth of second rectangle: "))
obj1 = Rectangle(l1, b1)
obj2 = Rectangle(l2, b2)
print("Area of rectangle 1:", obj1.area())
print("Perimeter of rectangle 1:", obj1.peri())
print("Area of rectangle 2:", obj2.area())
print("Perimeter of rectangle 2:", obj2.peri())
obj1.compare(obj2)


----------------------OUTPUT------------------------


Enter the length of first rectangle: 3
Enter the breadth of first rectangle: 6
Enter the length of second rectangle: 4
Enter the breadth of second rectangle: 4
Area of rectangle 1: 18
Perimeter of rectangle 1: 18
Area of rectangle 2: 16
Perimeter of rectangle 2: 16
Area of the 1st rectangle is greater.
