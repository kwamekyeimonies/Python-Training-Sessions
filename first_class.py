# def divider(dividend, divisor):
#     if divisor == 0 :
#         raise ZeroDivisionError("Divisor cannot be divided by 0")
#     return dividend/divisor

# def calculator(*values, operator):
#     return operator(*values)

# result = calculator(20,4, operator=divider)
# print(result)

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find element with  {expected} ")

friends =[
    {
        "name":"Tenkorang",
        "age":45
    },
    {
        "name":"Matilda",
        "age":12
    },
    {
        "name":"Anne",
        "age":45
    }
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends,"Matilda",get_friend_name))