!apt-get update
!apt-get install mysql-server -y
!service mysql start
!mysqladmin -u root password 'your_password'
!echo -e "y\n2\nyour_password\nyour_password\ny\ny\ny\ny" | mysql_secure_installation
!service mysql status
import mysql.connector
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )
    print("MySQL connection successful!")
    connection.close()
except Exception as e:
    print(f"Error connecting to MySQL: {e}")