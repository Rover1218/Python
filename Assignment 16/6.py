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
take_data = {
    "Student#": [1, 1, 2, 2, 3, 3],
    "Course#": [101, 102, 101, 103, 103, 102],
    "Grade": ["A", "B", "B", "A", "B", "A"],
}
student_df = pd.DataFrame(student_data)
take_df = pd.DataFrame(take_data)
student_df = student_df[student_df["Student#"] != 3]
take_df = take_df[take_df["Grade"] != "B"]
student_df.loc[student_df["Student#"] == 2, "LastName"] = "Smithson"
take_df.loc[(take_df["Student#"] == 1) & (take_df["Course#"] == 102), "Grade"] = "A+"
print("Updated STUDENT Table:")
print(student_df.to_markdown(index=False))
print("\nUpdated TAKE Table:")
print(take_df.to_markdown(index=False))