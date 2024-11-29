from datetime import datetime
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
    
    def calculate_age(self):
        today = datetime.now()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
if __name__ == "__main__":
    person = Person("Alice", "USA", "1990-05-15")
    print(f"Name: {person.name}")
    print(f"Country: {person.country}")
    print(f"Date of Birth: {person.date_of_birth.strftime('%Y-%m-%d')}")
    print(f"Age: {person.calculate_age()}")
