__author__ = 'jason'
p = True

def
n = int(input('enter an integer:'))
for i in range (2, n):
    if n % i == 0:
        print(n, "is a composite number:")
        p = False
        break
if p == True:
    print(n, "is a prime number")
    main()
main
