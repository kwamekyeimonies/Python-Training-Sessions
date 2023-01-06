menu=""" 
 Please select an option:
 1)Add new movie
 2)View upcoming movies
 3)View all movies
 4)Watch a movie
 5)View watched movies
 6)Exit
 
 Your selection: """
 
welcome="Welcome to Tea-Code Movie WatchList App"

print(welcome)
database.create_tables()

whiele(user_input := input(menu)) !="6":
    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("Invalid input, try again!")