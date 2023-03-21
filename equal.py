def equal_of_three_numbers(a,b,c):
    if a==b and b==c:
        return a
    elif b==c and b==a:
        return b
    else:
        return c

lof3=equal_of_three_numbers(2,2,2)
print("equal_of_three_numbers : " + str(lof3))
