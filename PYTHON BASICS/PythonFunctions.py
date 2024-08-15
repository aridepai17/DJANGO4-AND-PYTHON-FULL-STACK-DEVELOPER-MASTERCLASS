def sayhello(name):
    return f"Hello {name}"

myvar = sayhello("Advaith")
print(myvar)

def checker(num):
    if num > 100:
        return "Greater than 100"
    else:
        return "Less than 100"
    
print(checker(200))

mylist = [1,2,5,3,1,6,7,2,8,10,3,6]

def checking(listtocheck):
    for num in listtocheck:
        if num == 10:
            return True
        
    return False

print(checking(mylist))