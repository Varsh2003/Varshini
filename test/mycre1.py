import mycre

print("\tHii welcome to my python calculater\t")

print("we can perform the operations")
print("""1.Area of rectangle\n2.Area of square\n3.Perimeter of rectangle
4.Perimeter of square""")

choice=input("Enter your choice[1,2,3,4] : ")

if choice in["1","2","3","4"]:
    if choice=="1":
        print("you can chosen area of rec")
        l=int(input("Enter the number of length : "))
        w=int(input("Enter the number of width : "))
        print("Result = "+str(mycre.rect(l,w)))

    elif choice=="2":
        print("you can chosen area of sqr")
        a=int(input("Enter the number of a : "))
        print("Result = "+str(mycre.sqr(a)))

    elif choice=="3": 
        print("you can chosen the perimeter of rec")
        l=int(input("Enter the number of length : "))
        w=int(input("Enter the number of width : "))
        print("Result = "+str(mycre.pr(l,w)))

    elif choice=="4":
        print("you can chosen perimeter of sqr")
        a=int(input("Enter the number of a : "))
        print("Result = "+str(mycre.sq(a)))  

else:
        print("Invalid choice!!")          