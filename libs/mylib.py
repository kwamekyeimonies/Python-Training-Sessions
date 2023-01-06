from codex import divider
    
    
students =[
    {
        "name":"Daniel",
        "grades":[98,88]
    },
    {
        "name":"Kwame",
        "grades":[48,78]
    },
    {
        "name":"Emmanuel",
        "grades":[88,68]
    },
    {
        "name":"Isaac",
        "grades":[78,48]
    }
]

try:
    for dex in students:
        name=students["name"]
        grades=students["grades"]
        average = divider(sum(grades)/len(grades))
        print(f"{name} Average {average} ")
except ZeroDivisionError:
    print(f"Error:{name} has no grades available ")
else:
    print("--All student averages calculated--")
finally:
    print("--End of student average Calculation--")