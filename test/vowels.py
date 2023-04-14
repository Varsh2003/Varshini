choice=input("Enter your name : ")
output=""
for letter in choice:
    if letter in["a","e","i","o","u"]:
        letter="t"
    elif letter in["A","E","I","O","U"]:
        letter="T"
    output=output+letter
print(output)
    #    if choice in letter=="a":
    #       print("t")
    #    elif choice in letter=="A":
    #       print("T")
    #    else:
    #         print("It is not a vowel!!")    