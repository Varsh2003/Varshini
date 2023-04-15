


























print("Welcome to the interested puzzle game !!")
print("Start the game : Im the mental in my class who am I")

count=0

while count<4:
    ans=input("Enter your ans : ")
    if ans=="varshini":
        print("HAHA!! YOU WON")
        exit()
    else:
        count+=1
    if count==1:
        print("clue 1 : I am wear red colour dress !")
    elif count==2:
        print("I am brownish in colour !")
    elif count==3:
        print("I am smart girl in my class!")
if count==4:
    print("Sorry!! you lose")

       