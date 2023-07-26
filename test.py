# class practice
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def employee_details(self):
        print(f'Full Name: {self.first} {self.last}')
        print(f'Email: {self.email}')

    def paye (self):
        return self.pay * .3

    def net_income(self):
        return int(self.pay - self.paye())

    def pay_slip (self):
        print('Gross income is {} '.format(self.pay))
        print(f'Net income is {Employee.net_income(self)}')

    def department (self, department):
        return (print(f'Current station: {department}'))



emp_1 = Employee('Robinson', 'Musau', 100000)
emp_2 = Employee('Mike', 'Munguti', 70000)
emp_3 = Employee('Ken', 'Maghul', 120000)


emp_3.department('Engineering')