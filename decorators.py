users={
    "username":"Monies",
    "access_level":"guest"
}



def make_secure(func):
    def secure_function():
        if users["access_level"]=="admin":
            return func()
        else:
            return f"No admin permissions for {users['username']}"
    return secure_function 


@make_secure
def get_admin_password():
    return "dexoangle@001"

get_admin_password=make_secure(get_admin_password)

print(get_admin_password())