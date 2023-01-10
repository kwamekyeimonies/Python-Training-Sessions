from typing import List, Tuple

import psycopg2
from psycopg2.extras import execute_values


# db_connection = psycopg2.connect(
#     dbname=os.environ["DB_NAME"],
#     dbuser=os.envron["DB_USER"],
#     db_password=os.envron["DB_PASSWORD"],
#     db_host=os.envron["DB_HOST"],
#     db_port=os.envron["DB_PORT"],
# )

CREATE_POLLS = """
CREATE TABLE IF NOT EXISTS polls(
    id SERIAL PRIMARY KEY,
    title TEXT,
    owner_username TEXT
);
"""

CREATE_OPTIONS="""
CREATE TABLE IF NOT EXISTS options(
    id SERIAL PRIMARY KEY,
    option_text TEXT,
    poll_id FOREIGN KEY(poll_id) REFERENCES (id)
);
"""

CREATE_VOTES="""
CREATE TABLE IF NOT EXISTS votes(
    username TEXT,
    option_id INTEGER,
    FOREIGN KEY(option_id) REFERENCES (id)
);
"""

SELECT_ALL_POLLS ="""
SELECT * FROM polls;
"""

SELECT_POLLS_WITH_OPTIONS="""
SELECT * FROM polls
JOIN options ON polls.id = options.poll_id
WHERE polls.id = %s;" 
"""

INSERT_OPTION="""
INSERT INTO options(
    option_text, poll_id
) VALUES(%s);
"""

INSERT_VOTE="""
INSERT INTO VOTES(
    username, option_id
) VALUES(%s, %s);
"""


def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_POLLS)
            cursor.execute(CREATE_OPTIONS)
            cursor.execute(CREATE_VOTES)
            
def get_polls(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_POLLS)
            return cursor.fetchall()
        
def get_latest_polls(connection):
    with connection:
        with connection.cursor() as cursor:
            pass
        
        
def get_poll_details(connection,poll_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLLS_WITH_OPTIONS, (poll_id,))
            return cursor.fetchall()
        
        
def create_poll(connection, title, owner, options):
    with connection:
        with connection.cursor() as cursor:
            pass
        
def add_poll_vote(connection,username,option_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_VOTE, (username, option_id))