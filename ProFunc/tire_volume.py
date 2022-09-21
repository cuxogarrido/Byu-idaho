import math


wid = int(input("Enter the width of the tire in mm(ex 205)"))
asp = int(input("Enter the aspect ratioof the tire mm(ex 50)"))
dia = int(input("Enter the diameter of the wheel in inches(ex 15)"))


computation = (math.pi * wid**2 * asp*(wid * asp + 2540 * dia))  / 10000000000 

print(f"the aproximate volume is {computation:.2f} liters ")