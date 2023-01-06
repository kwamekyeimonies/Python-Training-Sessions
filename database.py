import sqlite3

connection =sqlite3.connect("data.db")
connection.row_factory=sqlite3.Row

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries(content TEXT, date TEXT);")


def add_entry(entry_content,entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES(?,?);",(entry_content,entry_date)
        )
        # connection.execute(f"INSERT INTO entries VALUES('{entry_content}','{entry_date}');")
    # entries.append({
    #     "content":entry_content,
    #     "date":entry_date
    # })
    
    
def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor

# def view_entry():
#     for entry in entries:
#         print(f"{entry['date']}\n {entry['content']}\n\n") 

