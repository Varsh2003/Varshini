n=5
s=0
for index in range (0,n,2):
    
    for i in range(s):
        print(" ",end="")
    s=s+1
    for index_1 in range(n-index ):
        print("*",end="")
    print() 
       