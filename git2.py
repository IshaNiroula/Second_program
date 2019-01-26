a = input("Name: ")
b = input("Age: ")
c = input("College: ")

a = str (a)
b = int (b)
c= str(c)

CA= float(input("Enter the total marks in \ni.Computer Architecture: "))
CG = float(input("ii.Computer Graphics: "))
NM = float(input("iii.Numerical Method: "))
DSA = float(input("iv.Data Structure and Algorithm: "))
ST = float(input("v.Statistics II: "))
total = float(CA+CG+NM+DSA+ST)
per = float(total/5)

print("My name is %s .\nMy age is %s .\nMy college is %s ." %(a,b,c))
print("The total marks is ",total, " and the total percentage is " ,per, ".")
