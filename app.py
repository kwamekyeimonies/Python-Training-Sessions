from dotenv import load_dotenv
import os
import psycopg2
from dotenv import load_dotenv
import database

DATABASE_PROMPT="""
Enter the DATABASE Credentials or URI in the .env file: 
"""

MENU_PROMPT=""" --- Menu ---
1)Create New Poll
2)List Open Polls
3)Vote On a Poll
4)Show all votes
5)Select a Random Winner from Poll Option
6)Exit

Enter your Choice:  
"""

NEW_OPTION_PROMPT="""
Enter New Option Text(or Leave empty to stop adding Options):   
"""

def prompt_create_poll(connection):
    poll_title = input("Enter poll title: ")
    poll_owner = input("Enter poll Owner: ")
    option =[]
    
    while new_option := input(NEW_OPTION_PROMPT):
        option.append(new_option)
        
    database.create_poll(connection, poll_title, poll_owner,option)
    
    

def list_open_polls(connection):
    polls = database.get_polls(connection)
    
    for _id, title, owner in polls:
        print(f"{_id}: {title} (created by {owner}) ")   
        
def prompt_vote_poll(connection):
    poll_id =int(input("Enter poll you would like to Vote: ")) 
    poll_options = database.get_poll_details(connection,poll_id)
    _print_
        