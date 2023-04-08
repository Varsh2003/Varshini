import json
f=open("file.json","r")

data=json.load(f)
 
print(data["stu_details"][1])
f.close()




# stu_details={
#                  "stu_name":input("Enter the name : "),
#                  "stu_age":input("Enter the age : "),
#                  "stu_mark":input("Enter the mark : ")
#              }
# data["stu_details"].append(stu_details)
# print(data)

# f.close()

# fg=open("file.json","w")
# json.dump(data,fg,indent=2)
# fg.close()
