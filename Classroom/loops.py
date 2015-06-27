__author__ = 'jason'
sum = 0
count = 0
for count in range(1, 4):
    t = float(input("Temperature:"))
    sum = sum + t
avg = sum / count
print("The Average is: %3.1f"%(avg))