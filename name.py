username=input("Enter the name")
if(len(username)>=3 and len(username)<=50):
    print("Welcome "+username)
else:
    print("Invalid username")