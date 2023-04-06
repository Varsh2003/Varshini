n=int(input("Enter the value of a : "))

a=0
s=n//2
if n%2==0:
       j=2
else:
       j=1     
while a<n:
    k=0
    while k<s:
        print(" ",end="")
        k=k+1
    s-=1
    m=0      
    while m<j:
        print("*",end="")
        m+=1
    j=j+2
    a+=2

    print("")
    






















