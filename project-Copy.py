from logging import root
import random 
from random import randint
import datetime

slist = []


class Department:

    dept_list = []

    def __init__(self, name):
        Department.dept_list.append(self)
        self.name = name
        self.empl_query = []

    def add_employee(self, empl):
        self.empl_query.append(empl)

    #finance.remove_employee(id, emplist) #id of personel to remove
    def remove_employee(self, id):

        # REMOVING EMPLOYEE FROM DEPARTMENT EMPLOYEE LIST

        id_list = [empl.empid for empl in self.empl_query]
        q_index = id_list.index(id)
        name = self.empl_query[q_index].first + " " + self.empl_query[q_index].last
        del self.empl_query[q_index]
    
        print(f"{name} has been removed from {self.name}")
        # SHOULD ALSO REMOVE EMPLOYEE FROM ALL EMPLOYEE LIST AS WELL
        
    def list_employee(self):
        for employee in self.empl_query:
            print(f"{employee.first} {employee.last}, id: {employee.empid}, hire_date: {employee.hiredate}")

    def remove_department(self, del_index):
        print(f"{self.name} has been removed from Department list")
        del Department.dept_list[del_index]

    def list_departments():
        for i in range(len(Department.dept_list)):
            print(f"{i + 1}) {Department.dept_list[i].name}")

    def query_hiredate(self):
        sorted_dates = [empl.hiredate for empl in self.empl_query]
        sorted_dates.sort()

        sorted_dates_with_names = []
        for date in sorted_dates:
            for empl in self.empl_query:
                if date == empl.hiredate:
                    sorted_dates_with_names.append(f"{empl.first} {empl.last}, hire date: {date}")
        
        print(sorted_dates_with_names)
    
    def sal(e):
        return e.salary

    def sorted_sal(self):
        def sal(e):
            return e.salary

        slist = self.empl_query
        finlist =[]

        slist.sort(key=sal)
        for employee in slist:
             finlist.append([employee.first,employee.last,employee.empid,employee.salary])

        slist.sort(reverse=True,key=sal)
        print(finlist)

class Employee:     
    emplist = []

    def __init__(self, first: str, last: str, salary: int, department: str, manager:bool):
        Employee.emplist.append(self)
        self.first = first
        self.last = last
        self.empid = self.gen_randomid()
        self.salary = salary
        self.department = department
        self.manager = manager
        self.hiredate = self.random_hiredate()

    def is_manager(self):
        pass
        #if self.manager == True:
            
    def update_first(self, first: str):
        self.first = first
    def update_last(self, last):
        self.last = last
    def update_salary(self, salary):
        self.salary = salary
    def update_dept(self, department):
        self.department = department
    def update_manager(self, manager):
        self.manager = manager
    #def update_hiredate(self, hiredate):
   #     self.hiredate = hiredate
    def gen_randomid(self):
        return random.randrange(10000, 99999)
    def random_hiredate(self):
        date = str(randint(2015,2022)) + str(randint(1,12)) + str(randint(1,28))
        return date
    def remove_employee(self, id):

        # REMOVE EMPLOYEE FROM ALL EMPLOYEE LIST AS WELL

        id_list = [empl.empid for empl in Employee.emplist]
        q_index = id_list.index(id)
        name = Employee.emplist[q_index].first + " " + Employee.emplist[q_index].last
        del Employee.emplist[q_index]
    
        print(f"{name} has been removed from All Employees List")
  
        
# class SalaryException (Exception): pass
# try:
#     salary = int(input("Please enter your yearly salary"))
#     if salary < 40000:
#         raise SalaryException("This salary is too low")
# except SalaryException as e:
#     print(e)
    

employee1 = Employee('kenny', 'yang', 50000, 'Finance', False)
employee2 = Employee('steven', 'chan', 20000, 'Finance', False)
employee3 = Employee('caleb ', 'prince', 45000, 'Finance', False)
employee4 = Employee('biff', 'busick', 47500, 'Sales', False)
employee5 = Employee('jenny', 'fromdabloc', 52000, 'Sales', False)
employee6 = Employee('john', 'everyman', 48000, 'Finance', False)
employee7 = Employee('lisa', 'simpson', 80000, 'Finance', True)
employee8 = Employee('montgomery', 'burns', 100000, 'Sales', True)
employee9 = Employee('Smain', 'Benloukil', 49000, 'Sales', False)


# print(employee1.empid, employee2.empid)

finance = Department("Finance")
sales = Department("Sales")

finance.add_employee(employee1)
finance.add_employee(employee2)
finance.add_employee(employee3)
finance.add_employee(employee6)
finance.add_employee(employee7)

sales.add_employee(employee4)
sales.add_employee(employee5)
sales.add_employee(employee8)
sales.add_employee(employee9)

# finance.list_employee()
# for employee in Employee.emplist:
#     print(f"{employee.first} {employee.last}")

# remove_id = int(input("Which employee would you like to remove? (id): "))
# finance.remove_employee(remove_id)
# finance.list_employee()


root = int(input("Hello, Welcome to 3Corp.\n1) View Departments\n2) Add Departments\nChooose (1/2): "))
while True:
    if root == 1:
        print(f"Here are the departments:")
        Department.list_departments()

        select_dept = int(input("Enter digit for which department: ")) - 1
        viewCurrent = int(input(f"{Department.dept_list[select_dept].name} Department\n1) View employees\n2) Add employees\n3) Delete Department\n--- Enter other key to go back --- : "))
        while True:
            if viewCurrent == 1:
                print(f"Here are all the Employees") 
                Department.dept_list[select_dept-1].list_employee()
                print("Here are the employees sorted by hire date")
                Department.dept_list[select_dept-1].query_hiredate()

                print("-----------------------------------------------------------------------------------------")
                Department.dept_list[select_dept-1].sorted_sal()
                break
            elif viewCurrent == 2:
                while True:
                    class SalaryException (Exception): pass
                    try:
                        emp_first = input("Enter Employee First Name: ")
                        emp_last= input("Enter Employee Last Name: ")
                        emp_salary = int(input("Please enter employee yearly salary: "))
                        if emp_salary < 40000:
                            raise SalaryException
                        emp_dept = Department.dept_list[select_dept-1].name
                        emp_manager = False if input("Is employee manager? (yes/no) ") != "yes" else True
                        new_empl = Employee(emp_first, emp_last, emp_salary, emp_dept, emp_manager)
                        # new_empl.gen_randomid()
                        # new_empl.random_hiredate()
                        Department.dept_list[select_dept-1].add_employee(new_empl)
                        Department.dept_list[select_dept-1].list_employee()
                        break
                    except SalaryException:
                        print("This salary is too low")

            elif viewCurrent == 3:
                print(select_dept)
                Department.dept_list[select_dept].remove_department(select_dept)
                break
            elif viewCurrent == 4:
                Department.dept_list[0].sorted_sal()
                Department.dept_list[1].sorted_sal()
                break

            else:
                break
        else:
            print("Please choose a valid option")
            
        # viewfinance = input("SALES DEPARTMENT\n1) View employees\n2) Add employees\n3) Return to previous menu.")
        # if viewfinance == 1:
        #     print("Here are all the Employees {Employee.emplist}")
        # elif viewfinance == 2:
        #     emp_input = input("New Employee input: ")
        #     Department.add_employee(emp_input)
        # elif viewfinance == 3:
        #     pass
        # else:
        #     print("Please choose a valid option")
    elif root == 2:
        dept_name = input("Department Name: ")
        new_dept = Department(dept_name)
    # else: 
    #     print("Please input ")