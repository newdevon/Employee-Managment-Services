import random 

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
        self.empl_query.pop(q_index)
    
        print(f"{name} has been removed from {self.name}")
        # SHOULD ALSO REMOVE EMPLOYEE FROM ALL EMPLOYEE LIST AS WELL
        
    def list_employee(self):
        for employee in self.empl_query:
            print(f"{employee.first} {employee.last}, id: {employee.empid}")

        # return self.empl_query

    def list_departments():
        print("I am here!")
        for dept in Department.dept_list:
            print(f"{dept.name}")

class Employee:
    emplist = []

    def __init__(self, first: str, last: str, salary: int, department: str, manager:bool):
        Employee.emplist.append(self)
        self.first = first
        self.last = last
        self.empid = None
        self.salary = salary
        self.department = department
        self.manager = manager

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
    def gen_randomid(self):
        self.empid = random.randrange(10000, 99999)
        
    def remove_employee(self, id):

        # REMOVE EMPLOYEE FROM ALL EMPLOYEE LIST AS WELL

        id_list = [empl.empid for empl in Employee.emplist]
        q_index = id_list.index(id)
        name = Employee.emplist[q_index].first + " " + Employee.emplist[q_index].last
        Employee.emplist.pop(q_index)
    
        print(f"{name} has been removed from All Employees List")
        
class SalaryException (Exception): pass
try:
    salary = int(input("Please enter your yearly salary"))
    if salary < 40000:
        raise SalaryException("This salary is too low")
except SalaryException as e:
    print(e)
    

employee1 = Employee('kenny', 'yang', 50000, 'Finance', False)
employee2 = Employee('steven', 'chan', 20000, 'Finance', False)
employee3 = Employee('caleb ', 'prince', 45000, 'Finance', False)
employee4 = Employee('biff', 'busick', 47500, 'Sales', False)
employee5 = Employee('jenny', 'fromdabloc', 52000, 'Sales', False)
employee6 = Employee('john', 'everyman', 48000, 'Finance', False)
employee7 = Employee('lisa', 'simpson', 80000, 'Finance', True)
employee8 = Employee('montgomery', 'burns', 100000, 'Sales', True)
employee9 = Employee('Smain', 'Benloukil', 49000, 'Sales', False)

employee1.gen_randomid()
employee2.gen_randomid()
print(employee1.empid, employee2.empid)

finance = Department("finance")
sales = Department("sales")

finance.add_employee(employee1)
finance.add_employee(employee2)
finance.add_employee(employee3)
finance.add_employee(employee6)
finance.add_employee(employee7)

finance.list_employee()
# for employee in Employee.emplist:
#     print(f"{employee.first} {employee.last}")

# remove_id = int(input("Which employee would you like to remove? (id): "))
# finance.remove_employee(remove_id)
# finance.list_employee()


start = int(input("1) View Departments\n2) Add Departments\nChooose (1/2): "))
while True:
    if start == 1:
        print(f"Here are the departments:\n")
        Department.list_departments()
        select_dept = input("1) Finance\n2) Sales\n")
        if select_dept == 1:
            viewsales = input("SALES DEPARTMENT\n1) View employees\n3) Add employees\n4) Return to previous menu.")
            if viewsales == 1:
                print("Here are all the Employees {Employee.emplist}")
            elif viewsales == 2:
                pass
            elif viewsales == 3:
                pass
        else:
            print("Please choose a valid option")
            
        viewfinance = input("FINANCE DEPARTMENT\n1) View employees\n2) Add employees\n3) Return to previous menu.")
        if viewfinance == 1:
            print("Here are all the Employees {Employee.emplist}")
        elif viewfinance == 2:
            pass
        elif viewfinance == 3:
            pass
        else:
            print("Please choose a valid option")
    elif start == 2:
        dept_input = input("New Department: ")
        new_dept = Department(dept_input)
    else: 
        start = int(input("1) View Departments\n2) to add Departments(1/2): "))