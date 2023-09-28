class User:
    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        self.salary = 15000

    def add_salary(self, increment):
        self.salary += increment


user_1 = User("001", "Maktum")
user_1.add_salary(2000)
print(user_1.salary)
