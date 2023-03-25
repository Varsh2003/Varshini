list=["aba","kjk","jkj","aba"]
count=0
if len(list[0])>2:
    if (list[0][0]==list[0][-1]):
        count=count+1
if len(list[1])>2:
    if (list[1][0]==list[1][-1]):
        count=count+1
if len(list[2])>2:
    if (list[2][0]==list[2][-1]):
        count=count+1
if len(list[3])>2:
    if (list[3][0]==list[3][-1]):
        count=count+1 
print(count)
        