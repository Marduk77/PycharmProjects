__author__ = 'jason'
password = ""
attempt = 0
print("You have 3 attempts to enter password:")
while password != "187" and attempt<3:
    password = input("password: ")
    attempt = attempt + 1
if password != "187":#
    print("fail")
else:
    print("not fail")