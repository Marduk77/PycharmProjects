__author__ = 'jason'
sum = 0
count = 0
while count < 3:
    t = float(input("Temperature: "))
    sum = sum + t
    count = count + 1
avg = sum/count
print("The Average is: %3.1f" %(avg))
