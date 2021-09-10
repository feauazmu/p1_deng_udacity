# DROP TABLES

songplay_table_drop = "drop table songplays;"
user_table_drop = "drop table users;"
song_table_drop = "drop table songs;"
artist_table_drop = "drop table artists;"
time_table_drop = "drop table time;"

# CREATE TABLES

songplay_table_create = """
create table if not exists songplays (songplay_id int primary key,
                                      start_time timestamp,
                                      user_id int,
                                      level varchar(4),
                                      song_id varchar(18),
                                      artist_id varchar(18),
                                      session_id int,
                                      location varchar,
                                      user_agent text);
"""

user_table_create = """
create table if not exists users (user_id int primary key,
                                  first_name varchar,
                                  last_name varchar,
                                  gender varchar(1),
                                  level varchar(4));
"""

song_table_create = """
create table if not exists songs (song_id varchar(18) primary key,
                                  title varchar,
                                  artist_id varchar,
                                  year int,
                                  duration numeric);
"""

artist_table_create = """
create table if not exists artists (artist_id varchar(18) primary key,
                                    name varchar,
                                    location varchar,
                                    latitude numeric,
                                    longitude numeric);
"""

time_table_create = """
create table if not exists time (start_time timestamp primary key,
                                 hour int,
                                 day int,
                                 week int,
                                 month int,
                                 year int,
                                 weekday int);
"""

# INSERT RECORDS

songplay_table_insert = """
insert into songplays (songplay_id, start_time, user_id, level, song_id,
                       artist_id, session_id, location, user_agent)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

user_table_insert = """
insert into users (user_id, first_name, last_name, gender, level)
values (%s, %s, %s, %s, %s)
"""

song_table_insert = """
insert into songs (song_id, title, artist_id, year, duration)
values (%s, %s, %s, %s, %s)
"""

artist_table_insert = """
insert into artists (artist_id, name, location, latitude, longitude)
values (%s, %s, %s, %s, %s)
"""

time_table_insert = """
insert into time (start_time, hour, day, week, month, year, weekday)
values (%s, %s, %s, %s, %s, %s, %s)
"""

# FIND SONGS

song_select = """
select songs.song_id, artists.artist_id
  from songs join artists
    on (artists.artist_id=songs.artist_id)
where songs.title = %s
  and artists.name = %s
  and songs.duration = %s
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
