import patient
print("welcome Patient Details application !!")
 
while True:
    print("You can perform the below operations : ")
    print("1.Register\n""2.View patient\n""3.Update patient\n""4.delete patient\n")
    choice=input("Enter your choice[1],[2],[3],[4] : ")

    if choice=="1":
        print("Welcome to patient registeration form")
        patient.reg()
    elif choice=="2": 
        print("welcome to the patient view form ")  
        patient.view()
    elif choice=="3":
        print("welcome to the update section")
        patient.update()  
    elif choice=="4":
        print("Welcome to delete section")
        patient.delete()  
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
      