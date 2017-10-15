class Employee:
    def __init__(self, first_name, middle_name, pay):
        self.first_name = first_name
        self.middle_name = middle_name
        self.pay = pay
        self.email = first_name + '.' + middle_name + '@company.company'
emp_1 = Employee('Tsofa', 'Julius', 50000)

print (emp_1.email)
