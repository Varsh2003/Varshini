import emp

s1=emp.Emp("1234",25000,"09.05.2003",5)
s2=emp.Emp("234",2500,"24.01.2003",4)
print(s1.emp_id + "\t" +str(s1.emp_salary))
s1.bon()
print(s1.final_salary) 
s2.bon()
print(s1.final_salary)