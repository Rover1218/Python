import random
import string
def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password_length = 10
random_password = generate_password(password_length)
print(f"Generated random password: {random_password}")