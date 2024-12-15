import mysql.connector
import pandas as pd
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='yourpassword',
        database='yourdatabase'
    )
    if connection.is_connected():
        print("Connected to MySQL database.")
        query = "SELECT * FROM STUDENT;"
        student_df = pd.read_sql(query, connection)
        student_df.to_csv('student_table.csv', index=False)
        print("STUDENT table exported successfully to 'student_table.csv'.")
        query = "SELECT * FROM INSTRUCTOR;"
        instructor_df = pd.read_sql(query, connection)
        instructor_df.to_csv('instructor_table.csv', index=False)
        print("INSTRUCTOR table exported successfully to 'instructor_table.csv'.")
        query = "SELECT * FROM COURSE;"
        course_df = pd.read_sql(query, connection)
        course_df.to_csv('course_table.csv', index=False)
        print("COURSE table exported successfully to 'course_table.csv'.")
        query = "SELECT * FROM TAKE;"
        take_df = pd.read_sql(query, connection)
        take_df.to_csv('take_table.csv', index=False)
        print("TAKE table exported successfully to 'take_table.csv'.")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed.")