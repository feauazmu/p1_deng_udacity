import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """Processes the song file information.

    Takes the filepath of a JSON file with metadata about the song and the
    artist of the song, and inserts the relevant information into the tables
    `songs` and `artists` of the `sparkifydb`.

    Args:
        cur (cursor): A cursor to the connection to the `sparkifydb`.
        filepath (string): The path of the JSON file.
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_cols = ["song_id", "title", "artist_id", "year", "duration"]

    song_data = df[song_cols].values.tolist()[0]
    cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_cols = [
        "artist_id",
        "artist_name",
        "artist_location",
        "artist_latitude",
        "artist_longitude",
    ]

    artist_data = df[artist_cols].values.tolist()[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """Processes the log file information.

    Takes the filepath of a JSON file with the activity logs from the music
    streaming app, process this information, and inserts the relevant
    information into the tables `users`, `time`, and `songplays` of the
    `sparkifydb`.

    Args:
        cur (cursor): A cursor to the connection to the `sparkifydb`.
        filepath (string): The path of the JSON file.
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df.query('page == "NextSong"')

    # convert timestamp column to datetime
    t = pd.to_datetime(df["ts"], unit="ms")

    # insert time data records
    time_data = (
        t,
        t.dt.hour,
        t.dt.day,
        t.dt.isocalendar().week,
        t.dt.month,
        t.dt.year,
        t.dt.weekday,
    )
    column_labels = ("start_time", "hour", "day", "week", "month", "year", "weekday")
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = pd.DataFrame(
        {
            "user_id": df["userId"],
            "first_name": df["firstName"],
            "last_name": df["lastName"],
            "gender": df["gender"],
            "level": df["level"],
        }
    ).drop_duplicates()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (
            pd.to_datetime(row.ts, unit="ms"),
            row.userId,
            row.level,
            songid,
            artistid,
            row.sessionId,
            row.location,
            row.userAgent,
        )
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """Processes the data depending on the function.

    It takes a global filepath and processes the JSON files one by one within
    that filepath according to the `func` function, then commits the changes to
    the database to which the connection is made.

    Args:
        cur (cursor): A cursor to the `conn` connection.
        conn (connection): A connection to a PostgreSQL database.
        filepath (string): Global path where the JSON files are located.
        func (function): Function to process each file.
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print("{} files found in {}".format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print("{}/{} files processed.".format(i, num_files))


def main():
    """Processes the log and song files."""
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student"
    )
    cur = conn.cursor()

    process_data(cur, conn, filepath="data/song_data", func=process_song_file)
    process_data(cur, conn, filepath="data/log_data", func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
