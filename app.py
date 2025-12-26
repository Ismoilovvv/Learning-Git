class Person:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return f'Hello {self.name}, your age is {self.age}, and your phone number is {self.phone_number}'

