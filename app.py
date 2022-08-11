from logging import root
import random 
from random import randrange, randint
from time import time
from re import X
from select import select
from tracemalloc import start
from turtle import end_fill
from unicodedata import name
from dateutil import parser
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
            print(f"{employee.name}, id: {employee.empid}, hire_date: {employee.hiredate}")

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
                    sorted_dates_with_names.append(f"{empl.name}, hire date: {date}")
        
        print(sorted_dates_with_names)
    
    def query_salary(self):
        sorted_salary = [empl.salary for empl in self.empl_query]
        sorted_salary.sort()

        sorted_salary_with_names = []
        for salary in sorted_salary:
            for empl in self.empl_query:
                if salary == empl.salary:
                    sorted_salary_with_names.append(f"{empl.name}, salary :{salary}")

        print(sorted_salary_with_names)


class Employee: 
    emplist = []

    def __init__(self, name: str, salary: int, department: str, manager:bool):
        Employee.emplist.append(self)
        self.name = name
        self.empid = self.gen_randomid()
        self.salary = salary
        self.department = department
        self.manager = manager
        self.hiredate = self.random_hiredate()

    def is_manager(self):
        pass
        #if self.manager == True:
            
    def update_name(self, name: str):
        self.name = name
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
        date = str(randint(2015,2022)) + " " + str(randint(1,12)) + " " + str(randint(1,28))
        return parser.parse(date)

    def remove_employee(self, id):

        # REMOVE EMPLOYEE FROM ALL EMPLOYEE LIST AS WELL

        id_list = [empl.empid for empl in Employee.emplist]
        q_index = id_list.index(id)
        name = Employee.emplist[q_index].name
        del Employee.emplist[q_index]
    
        print(f"{name} has been removed from All Employees List")

    def list_names():
        for i in range(len(Employee.emplist)):
            print(f"{i+1}) {Employee.emplist[i].name}")
    
    def list_all(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.empid}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
        isManager = "Yes" if self.manager else "No"
        print(f"Manager: {isManager}")
        date_time_obj = self.hiredate
        #date_time_obj = datetime.striptime(self.hiredate, '%y/%m/%d')
        print(f"Hire Date: {date_time_obj}")
    
    def query_name(name):
        name_list = [empl.name for empl in Employee.emplist]
        name_index = name_list.index(name)
        Employee.emplist[name_index].list_all()

    #  def query_empid(empid):
    #     empid_list = [empl.empid for empl in Employee.emplist]
    #     empid_index = empid_list.index(empid)
    #     Employee.emplist[empid_index].list_all()

    def query_hiredate():
        sorted_dates = [empl.hiredate for empl in Employee.emplist]
        sorted_dates.sort()

        sorted_dates_with_names = []
        for date in sorted_dates:
            for empl in Employee.emplist:
                if date == empl.hiredate:
                    sorted_dates_with_names.append(f"{empl.name}, hire date: {date}")
        
        print(sorted_dates_with_names)
    
    def query_salary():
        sorted_salary = [empl.salary for empl in Employee.emplist]
        sorted_salary.sort()

        sorted_salary_with_names = []
        for salary in sorted_salary:
            for empl in Employee.emplist:
                if salary == empl.salary:
                    sorted_salary_with_names.append(f"{empl.name}, salary :{salary}")

        print(sorted_salary_with_names)
  
        
# class SalaryException (Exception): pass
# try:
#     salary = int(input("Please enter your yearly salary"))
#     if salary < 40000:
#         raise SalaryException("This salary is too low")
# except SalaryException as e:
#     print(e)
    

employee1 = Employee('kenny yang', 50000, 'Finance', False)
employee2 = Employee('steven chan', 20000, 'Finance', False)
employee3 = Employee('caleb prince', 45000, 'Finance', False)
employee4 = Employee('biff busick', 47500, 'Sales', False)
employee5 = Employee('jenny fromdabloc', 52000, 'Sales', False)
employee6 = Employee('john everyman', 48000, 'Finance', False)
employee7 = Employee('lisa simpson', 80000, 'Finance', True)
employee8 = Employee('montgomery burns', 100000, 'Sales', True)
employee9 = Employee('Smain Benloukil', 49000, 'Sales', False)


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


root = int(input("Hello, Welcome to 3Corp.\n1) View Departments\n2) Add Departments\n3) See All Employees and Queries\nChooose (1/2/3): "))
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
                print("Here are the employees sorted by salary")
                Department.dept_list[select_dept-1].query_salary()
                break
            elif viewCurrent == 2:
                while True:
                    class SalaryException (Exception): pass
                    try:
                        emp_name = input("Enter Employee Full Name: ")
                        emp_salary = int(input("Please enter employee yearly salary: "))
                        if emp_salary < 40000:
                            raise SalaryException
                        emp_dept = Department.dept_list[select_dept-1].name
                        emp_manager = False if input("Is employee manager? (yes/no) ") != "yes" else True
                        new_empl = Employee(emp_name, emp_salary, emp_dept, emp_manager)
                        # new_empl.gen_randomid()
                        # new_empl.random_hiredate()
                        Department.dept_list[select_dept-1].add_employee(new_empl)
                        Department.dept_list[select_dept-1].list_names()
                        break
                    except SalaryException:
                        print("This salary is too low")

            elif viewCurrent == 3:
                print(select_dept)
                Department.dept_list[select_dept].remove_department(select_dept)
                break
            else:
                break
        else:
            print("Please choose a valid option")
            
    elif root == 2:
        dept_name = input("Department Name: ")
        new_dept = Department(dept_name)
    elif root == 3:
        print(f"\nHere are all the Employees") 
        Employee.list_names()

        print("\nPlease choose from the menu of options below\n")
        print("1) Search Employees by Name")
        print("2) Search Employees by ID")
        print("3) See Sorted by Hire Date")
        print("4) See Sorted by Salary")
        print("5) See all Managers\n")
        print("Enter any other key to go back")
        select = int(input("Enter your selection: "))

        match select:
            case 1:
                while True:
                    try:
                        search = input("Enter full name of employee you would like to search: ")
                        Employee.query_name(search)
                        break
                    except:
                        print("Name doesn't exist in database")
            case 2:
                while True:
                    try:
                        search = input("Enter ID of employee you would like to search: ")
                        # Employee.query_empid(search)
                        # NEED WAY TO SEE IDs
                        # break
                    except:
                        print("ID doesn't exist in database")
            case 3:
                print("Here are the employees sorted by hire date")
                Employee.query_hiredate()
            case 4:
                print("Here are the employees sorted by salary")
                Employee.query_salary()
            case 5:
                print("Here are all managers")
                # METHOD NOT YET CREATED
        break
    else: 
        print("Please input ")