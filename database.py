import sqlite3

connection =sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE entries(content TEXT, date TEXT);")

# entries=[
#     {
#         "content":"Today I deployed lab station box at Teshie-Lekma",
#         "date":"01/01/2023"
#     },
#     {
#         "content":"Station Automation with Golang",
#         "date":"02/01/2023"
#     },
#     {
#         "content":"REST API development with Gin-Gonic and Gorilla Mux Web Framework",
#         "date":"03/01/2023"
#     },
#     {
#         "content":"Writing Test for codes and desing of architecture",
#         "date":"04/01/2023"
#     },
# ]

def add_entry(entry_content,entry_date):
    with connection:
        connection.execute("INSERT INTO entries VALUES('Automation Test Scripts','04/05/2021');")
    # entries.append({
    #     "content":entry_content,
    #     "date":entry_date
    # })
    
    
def get_entries():
    return entries

# def view_entry():
#     for entry in entries:
#         print(f"{entry['date']}\n {entry['content']}\n\n") 

