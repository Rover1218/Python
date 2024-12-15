import pandas as pd

student_data = {
    "Student#": [1, 2, 3],
    "LastName": ["Smith", "Doe", "Brown"],
    "FirstName": ["John", "Jane", "James"],
    "Address": ["123 Main St", "456 Elm St", "789 Pine St"],
    "City": ["Los Angeles", "San Francisco", "Seattle"],
    "State": ["CA", "CA", "WA"],
    "Zip": ["90001", "94102", "98101"],
    "Enroll_Date": ["2020-08-15", "2019-09-10", "2021-01-12"],
    "Undergrad": [True, False, True],
}

instructor_data = {
    "InstName": ["Dr. Johnson", "Dr. Lee", "Dr. Miller"],
    "InstOffice": ["Room 101", "Room 202", "Room 303"],
    "Rank": ["Professor", "Associate Professor", "Assistant Professor"],
}

course_data = {
    "Course#": [101, 102, 103],
    "Title": ["Database Systems", "Operating Systems", "Artificial Intelligence"],
    "CrHour": [3, 4, 3],
    "InstName": ["Dr. Johnson", "Dr. Lee", "Dr. Miller"],
}

take_data = {
    "Student#": [1, 1, 2, 2, 3, 3],
    "Course#": [101, 102, 101, 103, 103, 102],
    "Grade": ["A", "B", "B", "A", "B", "A"],
}

student_df = pd.DataFrame(student_data)
instructor_df = pd.DataFrame(instructor_data)
course_df = pd.DataFrame(course_data)
take_df = pd.DataFrame(take_data)

print("STUDENT Table:")
print(student_df.to_markdown(index=False))
print("\nINSTRUCTOR Table:")
print(instructor_df.to_markdown(index=False))
print("\nCOURSE Table:")
print(course_df.to_markdown(index=False))
print("\nTAKE Table:")
print(take_df.to_markdown(index=False))