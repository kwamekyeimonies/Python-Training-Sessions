# users =[
#     (
#         0,
#         "Dexoangle",
#         "password1"
#     ),
#     (
#         1,
#         "Daniel",
#         "passwordx"
#     ),
#     (
#         2,
#         "Monies",
#         "passwordxy"
#     ),
#     (
#         3,
#         "Kwame",
#         "passwordxxyy"
#     ),
#     (
#         4,
#         "Jeffrey",
#         "passwordxyxyx"
#     )
# ]


# username_mapping = {user[1]:user for user in users}

# print(username_mapping)

# username_input = input("Enter username: ")
# userpassword_input = input("Enter your password: ")

# _,username,password = username_mapping[username_input]

# if userpassword_input == password:
#     print("Login Successful")
# else:
#     print("Credentials Incorrect")
    
    
#Unpacking Arguments

def multiply(*args):
    print(args)
    total =1
    for arg in args:
        total = total *arg
        
    return total

arg_mult= multiply(3,5,6,5,3,6,2,7,2,6)
print(arg_mult)


def args_operator(*args,operator):
    if operator =="+":
        return sum(args)
    elif operator=="*":
        return multiply(args)
    else:
        return "Operators cannot be handled for this operation"

print(args_operator(1,2,5,3,7,9,8, operator="+"))

#Unpacking Keyword Arguments
#kwargs is a dictionary

def named(**kwargs):
    print(kwargs)
    
# named(name="Daniel",age=25)

friend = {"name":"Tenkorang Daniel","email":"tenkorangd5@gmail.com"}
# named(**friend)    

def print_nicely(**kwargs):
    named(**kwargs)
    for x,y in kwargs.items():
        print(f"{x}: {y}")

print_nicely(name="Qwarmhe Daniel",email="danieldexoangle@gmail.com")

def both(*args, **kwargs):
    print(args)
    print(kwargs)

