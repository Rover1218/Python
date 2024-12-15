data = [
    {'name': 'Alice', 'age': 25, 'score': 85},
    {'name': 'Bob', 'age': 30, 'score': 92},
    {'name': 'Charlie', 'age': 22, 'score': 78},
    {'name': 'David', 'age': 28, 'score': 95}
]
high_scorers = [person for person in data if person['score'] >= 90]
young_people = [person for person in data if person['age'] < 25]
print("People with high scores (>= 90):")
for person in high_scorers:
    print(f"{person['name']}: {person['score']}")
print("\nYoung people (< 25 years):")
for person in young_people:
    print(f"{person['name']}: {person['age']} years")