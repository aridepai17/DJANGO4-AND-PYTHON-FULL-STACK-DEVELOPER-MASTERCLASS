password = "mypassword"
storedpassword = "mypassword"
admin = True

if password == storedpassword:
    print("Access Granted")
elif admin:
    print("Wrong Password but Admin Access Granted")
else:
    print("Access Denied")
#-------------------------------------------------------------------------

mylist = [1, 2, 3, 4, 5]

for item in mylist:
    print(f"Numbers in the list: {item}")
    
workers = { 'CEO': 'John', 'CTO': 'Jane', 'CFO': 'Jim' }

for position in workers:
    print(f"The {position} is held by {workers[position]}")

print(workers.items())

mylist = [('a', 'b'), ('c', 'd'), (1, 2)]

for item in mylist:
    print(item)
    
for item1, item2 in mylist:
    print(item1)
    print(item2)
#-------------------------------------------------------------------------

n = 1

while n < 5:
    print(f"N is currently: {n}")
    n += 1

#-------------------------------------------------------------------------


    
