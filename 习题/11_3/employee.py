class Employee():
    def __init__(self, last_name, first_name, dollar):
        self.last_name = last_name
        self.first_name = first_name
        self.dollar = dollar

    def give_raise(self, rise = 5000):
        self.rise = rise + self.dollar

