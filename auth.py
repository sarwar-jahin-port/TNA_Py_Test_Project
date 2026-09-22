from db import users_db
def login(users_db, username, password):
    for user in users_db:
        if user["username"] == username and user["password"] == password:
            print("User logged in successfully:", user["username"])
            return user
        else:
         print("User login failed:", username)
         return None
print(login(users_db, "admin", "123"))
print("kalpo")


       
def check_permission(user_role, allowed_roles):
    for role in allowed_roles:
        if user_role == role:
            print("Permission granted for role:", user_role)
            return True 
    else:
        print("Permission denied for role:", user_role)
        return False
print(check_permission("admin", {"admin", "customer"}))
print(check_permission("masum", {"admin", "customer"}))  
 
    



