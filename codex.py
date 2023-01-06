from import_dev import root_determinants
# import sys

print(root_determinants(2,3,4)) 
# print(sys.path)

def divider(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")
    else:
        return dividend/divisor
    
# grades =[87,67,98,45,99]
grades=[]

print("Welcome to Results average calculator")
try:
    average = divider(sum(grades),len(grades))
except ZeroDivisionError:
    print("There are no grades available in your grades")
else:
    print(f"The average of grades is {average}")


("codex.py",__name__)