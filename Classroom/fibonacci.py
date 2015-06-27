__author__ = 'jason'
a = 1
b = 1
count = int(input("How many Fibonnacci Nummbers? "))
for i in range (1, count + 1):
    print(a, end = " ")
    n = a + b
    a = b
    b = n
