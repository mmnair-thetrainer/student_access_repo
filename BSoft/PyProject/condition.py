a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))
if a > b and a > c:
    print("A is big")
elif b > a and b > c:
    print("B is big")
elif c > a and c > b:
    print("C is big")
else:
    print("None is big")
