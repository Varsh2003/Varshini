import patient
print("welcome Patient Details application !!")
 
while True:
    print("You can perform the below operations : ")
    print("1.Register")
    choice=input("Enter your choice[1] : ")

    if choice=="1":
        print("Welcome to patient registeration form")
        patient.reg()
    else:
        print("invalid choice")
    option=input("Do you want to continue (ok/not) : ")
    if option=="ok":
        continue
    elif option=="not":
        break
    else:
        print("invalid choice")
        break
print("Thanks for using the application")
      