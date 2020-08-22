class Employee:
    def __init__(self,id,name,role,salary):
        self.emp_id=id
        self.emp_name=name
        self.emp_role=role
        self.emp_salary=salary
 
    def increse_salary(self,no):
        self.emp_salary+=self.emp_salary*(no/100)
 
class Organisation:
    def __init__(self,oname,elist):
        self.org_name=name
        self.emp_list=elist
 
    def calculate_salary(self,role,percentage):
        result=[]
        for i in self.emp_list:
            if(i.emp_role==role):
                i.increse_salary(percetage)
                result.append(i)
        return result
 
if __name__ == '__main__':
    count=int(input())
    emp_l=[]
    for i in range(count):
        id=int(input())
        name=input()
        role=input()
        salary=int(input())
        emp_l.append(Employee(id,name,role,salary))
    o=Organisation("XYZ",emp_l)
    role=input()
    percentage=int(input())
    result=o.calculate_salary(role,percentage)
    for i in result:
        print(i.emp_name)
        print(i.emp_salary)
