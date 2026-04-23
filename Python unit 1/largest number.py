#Program to find largest of three numbers

a=int(input("Enter First number:"))
b=int(input("Enter Second  number:"))
c=int(input("Enter Third number:"))
if a>b and a>c:
    print("Largest:",a)
elif b>c:
     print("Largest:",b)
else:
         print("Largest:",c)


