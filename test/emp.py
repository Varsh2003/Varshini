class Emp:
    def __init__ (self,emp_id,emp_salary,emp_dob,emp_experience):
        self.emp_id=emp_id
        self.emp_salary=emp_salary
        self.emp_dob=emp_dob
        self.emp_experience=emp_experience
    

    def bon(self):
        if self.emp_experience>=5:
             self.final_salary=(20/100)*self.emp_salary+self.emp_salary
        elif self.emp_experience<5:
            self.final_salary=(5/100)*self.emp_salary+self.emp_salary
        print(self.final_salary)
