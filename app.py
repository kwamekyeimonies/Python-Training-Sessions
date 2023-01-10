import database
import datetime

menu=""" 
 Please select an option:
 1)Add new movie
 2)View upcoming movies
 3)View all movies
 4)Watch a movie
 5)View watched movies
 6)Add User
 7)Exit
 
 Your selection: """
 
welcome="Welcome to Tea-Code Movie WatchList App"

print(welcome)
database.create_table()

def prompt_add_movie():
    title=input("Movie title: ")
    release_date= input("Release date (dd-mm-YY): ")
    parse_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parse_date.timestamp()
    
    database.add_movie(title,timestamp)
    
def print_movie_list(heading, movies):
    print(f"---{heading} movies--- ")
    for movie in movies:
        movie_date= datetime.datetime.fromtimestamp(movie[2])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]}: {movie[1]} (on {human_date})")
    print("----\n")
    
# def print_watched_movie_list(username,movies):
#     print(f"---{username}'s watched movies --- ")
#     for movie in movies:
#         print(f"{movie[1]} ")
#     print("----\n")        

def prompt_watch_movie():
    username = input("Username: ")
    movie_id= input("Enter movie ID youv'ed watched: ")
    database.watch_movie(username,movie_id)
    
def prompt_add_user():
    username = input("Enter Username: ")
    database.add_user(username)
    
def prompt_show_watched_movies():
    username = input("Username: ")
    movies=database.get_watched_movies(username)
    if movies:
        print_movie_list("Watched Movies", movies)
    else:
        print("No Movies watched by User")     
    

while(user_input := input(menu)) !="7" :
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies=database.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched_movies()                       
    elif user_input == "6":
        prompt_add_user()        
    else:
        print("Invalid input, try again!")