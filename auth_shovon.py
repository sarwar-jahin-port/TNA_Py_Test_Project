from db import users_db
from db import ALLOWED_ROLES

def login(users_db, username, password):
    for user_id in users_db:
        if username == user_id["username"] and password == user_id["password"]:
            return f"You have logged in {username}"
    # Executed ONLY after checking every single user in users_db

    return "Invalid ID / Password"

#print(login(users_db,"admin", "123"))
#print(login(users_db,"customer1", "1234"))
#print(login(users_db,"customer2", "1234"))


def check_user_role(role, ALLOWED_ROLES):
    for user in ALLOWED_ROLES:
        if user == role:
            return "Allowed"
        return "Not Allowed"

print(check_user_role("admin1", ALLOWED_ROLES))