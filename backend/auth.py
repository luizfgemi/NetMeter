import bcrypt
from flask_httpauth import HTTPBasicAuth
from .db import cursor, conn

auth = HTTPBasicAuth()

def generate_random_password(length=12):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def setup_initial_user():
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    user = cursor.fetchone()
    if not user:
        password = generate_random_password()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', hashed_password))
        conn.commit()
        print(f"Initial admin password: {password}")

@auth.verify_password
def verify_password(username, password):
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user and bcrypt.checkpw(password.encode('utf-8'), user[0]):
        return username
    return None
