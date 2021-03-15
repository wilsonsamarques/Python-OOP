# data -> attributes
# functions -> methods
# Let's create a class to represent an employee in a company.

# class -> blueprint for creating instances
# each unique employee will be an instances of that class




class Employee:
    def __init__(self, fisrt, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(emp_1)
print(emp_2)






