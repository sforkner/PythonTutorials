import datetime


class Employee():

    numb_of_employees = 0  # class variable
    raise_amount = 1.04   # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.numb_of_employees += 1

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname)


# my_date = datetime.date(2019, 10, 28)
# print(Employee.is_workday(my_date))

dev_1 = Developer('Samuel', 'Forkner', 100000, 'fortran')

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(Employee.numb_of_employees)
print(new_emp_1.fullname)
print(new_emp_1.email)
print(new_emp_2.fullname)
print(new_emp_2.email)
print(new_emp_3.fullname)
print(new_emp_3.email)

mgr_1 = Manager('Joan', 'Forkner', 150000, [dev_1, new_emp_1, new_emp_2])
print(Employee.numb_of_employees)
print(dev_1.fullname)
print(dev_1.email)
print(dev_1.prog_lang)
print(mgr_1.fullname)
print(mgr_1.email)
mgr_1.print_emp()
print(mgr_1.fullname)
mgr_1.add_emp(new_emp_3)
mgr_1.remove_emp(new_emp_2)
mgr_1.print_emp()

print(new_emp_1)
print(dev_1)
