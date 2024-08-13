#-------------------------------------------------------------------------
myvar = "hello i am advaith r pai"

print(myvar.upper())
print(myvar.lower())
print(myvar.title())
print(myvar.capitalize())
print(myvar.count("a"))
print(myvar.find("i"))
print(myvar.split())

firstname = "advaith"
lastname = "r pai"
print(f"Hello my name is {firstname} {lastname}")
# ------------------------------------------------------------------------

myvar = 10
mylist = [1, 2, 3, myvar]

print(mylist)
print(mylist[3])
print(mylist[1:3])
print(mylist[1:])
print(mylist[:3])

yourvar = "NEW"

mylist.append(yourvar)
print(mylist)

mylist.insert(2, "inserted")
print(mylist)

itemremoved = mylist.pop()
print(mylist)
print(itemremoved)

reversedmylist = mylist.reverse()
print(reversedmylist)

someoneslist = [22, 55, 44, 3, 88, 33]
sortedlist = sorted(someoneslist)
print(sortedlist)
print(someoneslist.sort())
print(someoneslist.count(3))
#-------------------------------------------------------------------------

employees = {"Chef":"Amy", "Manager":"Bob", "Secretary":"Sue", "Accountant":"Tom"}
employees["Waiter"] = "Sally"
print(employees)
print(employees["ceo"])

employees["CEO"] = "Joe"
print(employees)

stockprices = {"GOOGL": [200,210,220], "AAPL": [200,100,30], "FB": [10,20,300] }
history = stockprices["GOOGL"]
print(f"First day price is : {history[0]}")

mydict = {"key1": 100, "key2":200, "key3":300}
print(mydict.keys())
print(mydict.values())
print(mydict.items())
#-------------------------------------------------------------------------

mytuple = (1, 2, 3, 4, 5)
print(mytuple)
print(mytuple[1])
print(mytuple[1:3])
#-------------------------------------------------------------------------

a = True
b = False

print(a)
print(b)
print(a and b)
print(a or b)
print(not a)
print(not b)

print(1 == 1)
print(1 != 1)
print(1 > 1)
print(1 < 2)
print(1 >= 1)
#-------------------------------------------------------------------------
#Comparison operators

record = "Joseph"
match = "Joseph"

print(record == match)
print(record != match)
print(record > match)
print(record < match)
print(record >= match)

#Logical Operators

a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(not b)
#-------------------------------------------------------------------------