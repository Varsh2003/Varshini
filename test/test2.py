n=int(input("Enter the value of a : "))

a=0
while a<n:
    s=0
    while s<a:
         print(" ",end="")
         s=s+1
    j=n
    while j>a:
         print("*",end="")
         j-=1
    print("")
    a+=1  