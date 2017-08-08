length=False
while length == False:
    ans=input("Please enter username:" )
    if len(ans) >0:
        length=True
        print("Thank you for entering your username")
    else:
        print("You must enter a username")
