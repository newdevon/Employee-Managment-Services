from logging import root
import math
import random 
from random import randrange, randint
from time import time
from select import select
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
    def remove_employee(self, id, action):    
        # REMOVING EMPLOYEE FROM DEPARTMENT EMPLOYEE LIST

        empid_list = [empl.empid for empl in self.empl_query]
        empid_index = empid_list.index(id)
        name = self.empl_query[empid_index].name
        del self.empl_query[empid_index]
        
        if action == "delete":
            print(f"{name.title()} has been removed from {self.name}")
        # SHOULD ALSO REMOVE EMPLOYEE FROM ALL EMPLOYEE LIST AS WELL
        
    def list_employee(self):
        for employee in self.empl_query:
            print(f"{employee.name.title()}, id: {employee.empid}, hire_date: {employee.hiredate}")

    def remove_department(self, del_index):
        print(f"{self.name} has been removed from Department list")
        del Department.dept_list[del_index]

    def list_departments():
        for i in range(len(Department.dept_list)):
            print(f"{i + 1}) {Department.dept_list[i].name.title()}")

    def query_hiredate(self):
        sorted_dates = [empl.hiredate for empl in self.empl_query]
        sorted_dates.sort()

        sorted_dates_with_names = []
        for date in sorted_dates:
            for empl in self.empl_query:
                if date == empl.hiredate:
                    sorted_dates_with_names.append(f"{empl.name.title()}, hire date: {date}")
        
        print(sorted_dates_with_names)
    
    def query_salary(self):
        sorted_salary = [empl.salary for empl in self.empl_query]
        sorted_salary.sort()

        sorted_salary_with_names = []
        for salary in sorted_salary:
            for empl in self.empl_query:
                if salary == empl.salary:
                    sorted_salary_with_names.append(f"{empl.name.title()}, salary :{salary}")

        print(sorted_salary_with_names)

    #given id, find employee's department and return its object
    def find_department(id):
        for dept in Department.dept_list:
            for empl in dept.empl_query:
                if empl.empid == id:
                    return dept
        print("Couldn't find department")

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
    def update_empid(self, empid):
        self.hiredate = empid
    def gen_randomid(self):
        return random.randrange(10000, 99999)
    def random_hiredate(self):
        date = str(randint(2015,2022)) + " " + str(randint(1,12)) + " " + str(randint(1,28))
        return parser.parse(date)

    def remove_employee(self, id, action):
        # REMOVE EMPLOYEE FROM ALL EMPLOYEE LIST AS WELL

        empid_list = [empl.empid for empl in Employee.emplist]
        empid_index = empid_list.index(id)
        name = Employee.emplist[empid_index].name
        del Employee.emplist[empid_index]
    
        if action == "delete":
            print(f"{name.title()} has been removed from All Employees List")

    def list_names():
        for i in range(len(Employee.emplist)):
            print(f"{i+1}) {Employee.emplist[i].name.title()}")
    def list_names_and_id():
        for i in range(len(Employee.emplist)):
            print(f"{i+1}) {Employee.emplist[i].name.title()}, id: {Employee.emplist[i].empid}")

    def list_managers():
        count = 1
        for i in range(len(Employee.emplist)):
            if Employee.emplist[i].manager == True:
                print(f"{count}) {Employee.emplist[i].name.title()}")
                count += 1
    
    def list_all(self):
        print(f"\nName: {self.name.title()}")
        print(f"Employee ID: {self.empid}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department.title()}")
        isManager = "Yes" if self.manager else "No"
        print(f"Manager: {isManager}")
        print(f"Hire Date: {self.hiredate}")
    
    def query_name(name):
        name_list = [empl.name for empl in Employee.emplist]
        name_index = name_list.index(name)
        Employee.emplist[name_index].list_all()

    def query_empid(empid):
        empid_list = [empl.empid for empl in Employee.emplist]
        empid_index = empid_list.index(empid)
        Employee.emplist[empid_index].list_all()

    def query_hiredate(res):
        sorted_dates = [empl.hiredate for empl in Employee.emplist]
        sorted_dates.sort()

        sorted_dates_with_names = []
        for date in sorted_dates:
            for empl in Employee.emplist:
                if date == empl.hiredate:
                    sorted_dates_with_names.append(f"{empl.name.title()}, hire date: {date}")
        
        if res == "yes":
            print(sorted_dates_with_names)
        else:
            print(sorted_dates_with_names[::-1])
    
    def query_salary(res):
        sorted_salary = [empl.salary for empl in Employee.emplist]
        sorted_salary.sort()

        sorted_salary_with_names = []
        for salary in sorted_salary:
            for empl in Employee.emplist:
                if salary == empl.salary:
                    sorted_salary_with_names.append(f"{empl.name.title()}, salary :{salary}")

        if res == "yes":
            print(sorted_salary_with_names)
        else:
            print(sorted_salary_with_names[::-1])
    
    def find_employee(id):
        for empl in Employee.emplist:
            if empl.empid == id:
                return empl
        print("Couldn't find Employee")
    

employee1 = Employee('kenny yang', 50000, 'Finance', False)
employee2 = Employee('steven chan', 20000, 'Finance', False)
employee3 = Employee('caleb prince', 45000, 'Finance', False)
employee4 = Employee('biff busick', 47500, 'Sales', False)
employee5 = Employee('jenny fromdabloc', 52000, 'Sales', False)
employee6 = Employee('john everyman', 48000, 'Finance', False)
employee7 = Employee('lisa simpson', 80000, 'Finance', True)
employee8 = Employee('montgomery burns', 100000, 'Sales', True)
employee9 = Employee('Smain Benloukil', 49000, 'Sales', False)

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

print("Hello, Welcome to 3Corp.")
while True:
    root = None
    while True:
        try:
            root = int(input("\n1) View Departments\n2) Add Departments\n3) See All Employees and Queries\nChooose (1/2/3): "))
            break
        except:
            print("\nPlease enter a valid entry")
    if root == 1:
        select_dept = None
        while True:
            try:
                print(f"\nHere are the departments:")
                Department.list_departments()
                select_dept = int(input("Enter digit for which department: ")) - 1
                test = Department.dept_list[select_dept].name.title()
            except:
                print("\nPlease enter a valid department selection\n")

            viewCurrent = None
            while True:
                try:
                    viewCurrent = int(input(f"\n{Department.dept_list[select_dept].name.title()} Department\n1) View employees\n2) Add employees\n3) Delete Department\n4) Go Back\nChoose (1/2/3/4): "))
                except: print("Please enter a valid entry")
                if viewCurrent == 1:
                    print(f"\nThere are {len(Department.dept_list[select_dept].empl_query)} Employees in {Department.dept_list[select_dept].name.title()}") 
                    Department.dept_list[select_dept].list_employee()

                    while True:
                        class InvalidEntry (Exception): pass
                        dept_empl_select = None
                        try:
                            dept_empl_select = int(input(f"\n1) View {Department.dept_list[select_dept].name.title()} Employees by Hire Date\n2) View {Department.dept_list[select_dept].name.title()} Employees by Salary\nChoose (1/2): "))
                            if dept_empl_select != 1 and dept_empl_select != 2:
                                raise InvalidEntry
                        except:
                            print("Invalid Entry Try Again")
                        
                    
                        match dept_empl_select:
                            case 1:
                                print("\nHere are the employees sorted by hiredate")
                                Department.dept_list[select_dept].query_hiredate()
                            case 2:
                                print("\nHere are the employees sorted by salary")
                                Department.dept_list[select_dept].query_salary()
                        break
                        
                elif viewCurrent == 2:
                    while True:
                        class SalaryException (Exception): pass
                        try:
                            emp_name = input("Enter Employee Full Name: ").lower()
                            emp_salary = int(input("Please enter employee yearly salary: "))
                            if emp_salary < 40000:
                                raise SalaryException
                            emp_dept = Department.dept_list[select_dept].name
                            emp_manager = False if input("Is employee manager? (yes/no) ") != "yes" else True
                            new_empl = Employee(emp_name, emp_salary, emp_dept, emp_manager)
                            Department.dept_list[select_dept].add_employee(new_empl)
                            print(f"{new_empl.name.title()} has been added to Employee and {Department.dept_list[select_dept].name.title()} List")
                            break
                        except SalaryException:
                            print("This salary is too low")

                elif viewCurrent == 3:
                    print(select_dept)
                    Department.dept_list[select_dept].remove_department(select_dept)
                    break
                else:
                    break
            go_back = input("Go Back (yes/no)? ")
            if go_back == "yes":
                break
            
    elif root == 2:
        dept_name = input("\nDepartment Name: ").lower()
        new_dept = Department(dept_name)
    elif root == 3:
        print(f"\nHere are all the Employees") 
        Employee.list_names_and_id()
        while True:    
            print("\nPlease choose from the menu of options below\n")
            print("1) Search Employees by Name")
            print("2) Search Employees by ID")
            print("3) See Sorted by Hire Date")
            print("4) See Sorted by Salary")
            print("5) See all Managers")
            print("6) Update an Employee")
            print("7) Delete an Employee\n")
            print("Enter any other key to go back")
            select = int(input("Enter your selection: "))

            match select:
                case 1:
                    while True:
                        try:
                            search = input("Enter full name of employee you would like to search: ").lower()
                            Employee.query_name(search)
                            break
                        except:
                            print("Name doesn't exist in database\n")
                case 2:
                    while True:
                        try:
                            search = int(input("Enter ID of employee you would like to search: "))
                            Employee.query_empid(search)
                            break
                        except:
                            print("ID doesn't exist in database\n")
                case 3:
                    res = input("\nSort by Ascending? (yes/no): ")
                    Employee.query_hiredate(res)
                case 4:
                    res = input("\nSort by Ascending? (yes/no): ")
                    Employee.query_salary(res)
                case 5:
                    print("Here are all managers: \n")
                    Employee.list_managers()
                case 6:
                    while True:
                        try:
                            search = int(input("Input ID of employee you would like to update (digit): "))
                            fname = Employee.find_employee(search).name
                            Department.find_department(search).remove_employee(search, "update")
                            Employee.find_employee(search).remove_employee(search, "update")

                            while True:
                                class SalaryException (Exception): pass
                                try:
                                    emp_name = input("Enter Employee New Name: ").lower()
                                    emp_salary = int(input("Please enter employee new yearly salary: "))
                                    if emp_salary < 40000:
                                        raise SalaryException
                                    print(f"\nHere are the departments:")
                                    Department.list_departments()
                                    new_dept_index = int(input("Enter digit for which new department: ")) - 1
                                    emp_new_dept = Department.dept_list[new_dept_index].name
                                    emp_manager = False if input("\nIs employee manager? (yes/no) ") != "yes" else True
                                    new_empl = Employee(emp_name, emp_salary, emp_new_dept, emp_manager)
                                    new_empl.update_empid = search
                                    print(f"{Department.dept_list[new_dept_index].name}")
                                    Department.dept_list[new_dept_index].add_employee(new_empl)
                                    print(f"{fname} has been updated to {new_empl.name.title()} and {Department.dept_list[new_dept_index].name.title()} List")
                                    break
                                except SalaryException:
                                    print("This salary is too low")
                            
                            break
                        except:
                            print("ERROR ID doesn't exist in database\n")
                case 7:
                    while True:
                        try:
                            search = int(input("Enter ID of employee you would like to delete: "))
                            Department.find_department(search).remove_employee(search, "delete")
                            Employee.find_employee(search).remove_employee(search, "delete")
                            break
                        except:
                            print("ERROR ID doesn't exist in database\n")
                    
                case _:
                    break
    else: 
        break