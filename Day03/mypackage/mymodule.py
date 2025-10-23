
gname = 'Rahul'
def greet(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event")

sports = ['cricket', 'football', 'hockey', 'tennis', 'table_tennis', "swimmng"]

scores= {'ODI': 8500, 'test': 6200, 'T20': 4500}

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary= salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

print(__name__)

if __name__ == '__main__':
    emp1 = Employee("Kevin", 150000)
    print(emp1)

    print("-" * 60)
    greet("Rahul")