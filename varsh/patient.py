import json
from tabulate import tabulate

def reg():
    # name=input("Enter patient name : ")
    # age=input("Enter patient age : ")
    # pro=input("Enter patient problem : ")
    # days=input("Enter how many days or week : ")
    temp_dic={
        "name":input("Enter patient name : "),
        "age":input("Enter patient age :"),
        "pro":input("Enter patient problem : "),
        "days":input("Enter how many daysor week : ")   
    }   
    f=open("reg.json","r")
    data=json.load(f)
    f.close()
    data["patient"].append(temp_dic)
    fw=open("reg.json","w")
    json.dump(data,fw,indent=4)
    fw.close()
    print("Patient register successfully!!")

def view():
    f=open("reg.json","r")
    data=json.load(f)
    f.close()    
    heading=["s.no","name","age","pro"]
    table=[]
    s_no=1
    for patient in data["patient"]:
      temp_list=[s_no,patient["name"],patient["age"],patient["pro"]]
      table.append(temp_list)
      s_no+=1
    print(tabulate(table,headers=heading))  

def update():
   view()
   f=open("reg.json","r")
   data=json.load(f)
   f.close()
   pat_choice=input("Enter the serial number of the patient you want to update : ")
   print("you can update \n1.Name\n2.Age\n3.pro\nAll")
   update_choice=input("Please enter your choice : ")
   s_no=1
   for patient in data["patient"]:
      if str(s_no)==pat_choice:
         if update_choice=="1":
            name=input("Enter updated name : ")
            patient["name"]=name
            print("Student data updated successfully!!")
         elif update_choice=="2":
            age=input("Enter update age :")   
            patient["age"]=age
            print("Student data is updated successfully")
         elif update_choice=="3":
            pro=input("Enter update pro : ")
            patient["pro"]=pro
         elif update_choice=="All":
             patient["name"]=("Enter update name : ")
             patient["age"]=("Enter update age : ")
             patient["pro"]=("Enter update pro : ")
             print("patient data is updated successfully")
         else:
             print("Invalid choice!!!!!!!")         
             break
             
      s_no+=1

   f=open("reg.json","w")
   json.dump(data,f,indent=3)
   f.close()  

def delete():
   view()
   f=open("reg.json","r")
   data=json.load(f)
   f.close()
   pat_choice=input("Enter the serial number of the patient you want to delete : ")
  
   s_no=1
   for patient in data["patient"]:   
     if str(s_no)==pat_choice:       
       data["patient"].remove(patient)
       print("Patient data is deleted successfully")

     s_no+=1

   f=open("reg.json","w")
   json.dump(data,f,indent=3)
   f.close()       