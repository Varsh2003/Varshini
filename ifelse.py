def lesser_of_three_numbers(c,d,e):
    if c<d and c<e:
        return c
    elif d<e and d<c:
        return d
    else:
        return c

lof3=lesser_of_three_numbers(2,2,2)
print("Greater_of_three_numbers : " + str(lof3))



            

