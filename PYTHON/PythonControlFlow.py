password = "mypassword"
storedpassword = "mypassword"
admin = True

if password == storedpassword:
    print("Access Granted")
elif admin:
    print("Wrong Password but Admin Access Granted")
else:
    print("Access Denied")
    