containvalue=False
while containvalue == False:
    ans=input("Please enter email address: " )
    for i in range(len(ans)): # Loops to check every (index)letter in the input
        if ans[i]=="@":# Checking each index (character) for the @
            containvalue=True # if it has the @ Print below. #if it doesn’t have the @ ask for the email again 
print("Thank you for entering an email address which includes an @ symbol") 
