from datetime import datetime
from pathlib import Path
from db import users_db

def login(users_db, username, password):
    for user in users_db:
        if user["username"] == username and user["password"] == password:
            print("User logged in successfully:", user["username"])
            log_login(user)  #this function is for log.md file which tracks the log
            return user
        
    print("User login failed:", username)
    return None
      
def check_permission(user_role, allowed_roles):
    for role in allowed_roles:
        if user_role == role:
            print("Permission granted for role:", user_role)
            return True 
   
    print("Permission denied for role:", user_role)
    return False

#log file 

LOG_FILE = Path(__file__).with_name("log.md")

def log_login(user, status="success"):
    timestamp = datetime.now().isoformat(timespec="seconds")

    with LOG_FILE.open("a", encoding="utf-8") as log_file:
        log_file.write(
            f"- {timestamp} | "
            f"username: {user['username']} | "
            f"role: {user['role']} | "
            f"status: {status}\n"
        )

  
 
    



