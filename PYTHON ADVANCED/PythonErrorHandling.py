try:
    print("10" + 10) #Visit a URL
except IOError:
    print("You have an input/output error")
    print("Did you check th file permissions?")
except:
    print("An error occurred") #Report back to user
finally:
    print("This will always execute") #Take them to another page
