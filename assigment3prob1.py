class Employee:
    total_employees=0;
    def __init__(self,name,family,salary,department):
        self.name = name;
        self.family = family;
        self.salary= salary;
        self.department =department;
        Employee.total_employees+= 1
    def display_employee_info(self):
        print(f"Name :{self.name}")
        print(f"Family :{self.family}")
        print(f"Salary :${self.salary}")
        print(f"Department :{self.department}")
    @staticmethod
    def average_salary(employees):
        total_salary = sum(emp.salary for emp in employees)
        return total_salary / len(employees)
class FulltimeEmployee(Employee):
     def __init__(self,name,family,salary,department,benefits):
         super().__init__(name,family,salary,department)
         self.benefits= benefits

     def display_fulltime_employee_info(self):
         self.display_employee_info()
         print(f"Benefits: {self.benefits}")

employee1 = Employee("navya chanamolu", "mounika chanamolu" ,80000, 'IT enginner')
employee2 = Employee("srisha chanamolu", "radhika chanamolu" ,70000, 'architect')

fulltime_employee1 = FulltimeEmployee("navys", "chamaolufamily" ,66000, "finance" ,"technology")
fulltime_employee2 = FulltimeEmployee("bandaru", "bandarufamily" ,86000, "digital_marketing" ,"marketing")

 
print("Employee 1: ")
employee1.display_employee_info()
print("\nEmployee 2: ")
employee2.display_employee_info()

print("\n Fulltime Employee 1: ")
fulltime_employee1.display_fulltime_employee_info()
print("\n Fulltime Employee 2: ")
fulltime_employee2.display_fulltime_employee_info()

employees =[employee1,employee2,fulltime_employee1,fulltime_employee2]
average_salary= Employee.average_salary(employees)
print(f"\n average salary : ${average_salary:.2f}")

