from database import add_entry, get_entries, create_table

menu = """Please select one of the following options:
1) Add new entry for today
2) View entries
3) Exit

Your selection: """

welcome = "Welcome to the tea-code developers"

def propmt_new_entry():
    entry_content=input("What have you learned today?   ")
    entry_date=input("Enter the date: (eg:01/01/2023)")
    add_entry(entry_content,entry_date) 
    
def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n {entry['content']}\n\n")
    
   
print(welcome)
create_table()

# user_input = input(menu)
while (user_input := input(menu)) !=3:
    if user_input =="1":   
        propmt_new_entry()
    elif user_input =="2":
        view_entries(get_entries())
    else:
        print("Invalid Option, please try again")