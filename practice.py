class Employee():
    def __init__(self, first, last, income):
        self.first = first
        self.last = last
        self.income = income

    def give_raise(self, increment = 5000):
        self.income += increment

