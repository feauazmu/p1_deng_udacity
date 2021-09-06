# DROP TABLES

songplay_table_drop = "drop table songplays;"
user_table_drop = "drop table users;"
song_table_drop = "drop table songs;"
artist_table_drop = "drop table artists;"
time_table_drop = "drop table times;"

# CREATE TABLES

songplay_table_create = """
create table songplays (songplay_id int primary key,
                        start_time int,
                        user_id int,
                        level varchar(4),
                        song_id varchar(18),
                        artist_id varchar(18),
                        session_id int,
                        location varchar,
                        user_agent text
                        );
"""

user_table_create = """
create table users (user_id int primary key,
                    first_name varchar,
                    last_name varchar,
                    gender varchar(1),
                    level varchar(4));
"""

song_table_create = """
create table songs (song_id varchar(18) primary key,
                    title varchar,
                    artist_id varchar,
                    year int,
                    duration number);
"""

artist_table_create = """
create table artists (artist_id varchar(18) primary key,
                      name varchar,
                      location varchar,
                      latitude number,
                      longitude number);
"""

time_table_create = """
create table times (start_time int primary key,
                    hour int,
                    day int,
                    week int,
                    month int,
                    year int,
                    weekday int);
"""

# INSERT RECORDS

songplay_table_insert = """
"""

user_table_insert = """
"""

song_table_insert = """
"""

artist_table_insert = """
"""


time_table_insert = """
"""

# FIND SONGS

song_select = """
"""

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
