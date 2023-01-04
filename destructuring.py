x,y= (4,6)


student_attendance = {
    "Daniel":100,
    "Kwame":98,
    "James":32,
    "Asantewaa":89
}
    
# for x,y in student_attendance.items():
#     print(f"{x}: {y}")

# print(list(student_attendance.items()))        
    
# for dex in student_attendance():
#     print(dex)
    

people =[
    ("Bobby",23,"Technician"),
    ("Dexoangle",32,"Artist"),
    ("Kwame",45,"Engineer")
]

for name,age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession} ")
    
head, *tail = [1,3,5,6,7,8]
print(head)
print(tail)
