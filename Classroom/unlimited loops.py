__author__ = 'jason'
sum = 0
count = 0
a = "Y"
while a == "Y" or a == "y" or a[0].lower()== "y":
    t = float(input("Temperature: "))
    sum = sum + t
    count = count + 1
    a = input("Enter another (y/n):")
avg = sum / count
print("The Average is: %3.1f" %(avg))

