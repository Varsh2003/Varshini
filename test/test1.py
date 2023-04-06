n=int(input("Enter the value of a : "))

a=0
while a<n:
    j=n
    while j>a:
         print("*",end="")
         j-=1
    print("")
    a+=1     