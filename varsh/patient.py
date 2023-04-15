import json

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