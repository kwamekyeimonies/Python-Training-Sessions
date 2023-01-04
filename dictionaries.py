friends_ages={
    
    "name": "Tenkorang Daniel", "age":24,
    "name": "Akyaa Agnes", "age":20,
    "name": "Adobea Faustina", "age":10,
    "name": "Najat Julliet", "age":23,
    "name": "Fiadzo Matilda", "age":23
}

print(friends_ages)

student_attendance = {
    "Daniel":100,
    "Kwame":98,
    "James":32,
    "Asantewaa":89
}

for x in student_attendance:
    print(f"{student_attendance}: {student_attendance[x]} ")
    
for x,y in student_attendance.items():
    print(f"{x}: {y}")
    
