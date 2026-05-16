from schema.users import *
from core.database import get_connection
import bcrypt


def check_user_exists(email: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE Email = %s"
    cursor.execute(query, (email,))
    existing_user = cursor.fetchone()
    cursor.close()
    conn.close()
    return existing_user is not None

def create_user(user_data: CreateUser):
    if check_user_exists(user_data.Email):
        raise Exception("User with this email already exists")
    conn = get_connection()
    cursor = conn.cursor()
    hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt())
    query = "INSERT INTO users (Name, Email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_data.Name, user_data.Email, hashed_password))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Creating user: {user_data.Name}, Email: {user_data.Email}")

  
def login_user(user_data: LoginUser):
    if not check_user_exists(user_data.Email):
        raise Exception("User with this email does not exist")
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE Email = %s"
    cursor.execute(query, (user_data.Email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if not user:
        raise Exception("Invalid email or password")
        
    # Compare input password with stored hash
    if not bcrypt.checkpw(user_data.password.encode('utf-8'), user[3].encode('utf-8')):
        raise Exception("Invalid email or password")
        
    print(f"Logging in user with Email: {user_data.Email}")
    