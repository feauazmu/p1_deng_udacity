# Project: Data Modeling with Postgres.

In this repository you can find the code for the project: *Data Modeling with Postgres* of [udacity's nanodegree in data engineering](https://www.udacity.com/course/data-engineer-nanodegree--nd027).

The introduction to the project states the following:

>*A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.*

## Project Description

The idea of the project is to create an ETL pipeline using Python and SQL to transfer data from a set of JSON files located in two different directories to a collection of tables in a Postgres database. This way the analysts working in the company will be able to do their work more efficiently.

## Database schema design

The schema used for this database is a [*star schema*](https://en.wikipedia.org/wiki/Star_schema).  It consists of a fact table and four dimension tables and is structured as shown below.

![Schema](https://github.com/feauazmu/p1_deng_udacity/blob/main/static/schema.png?)

## Prerequisites

To run the project locally successfully it is necessary to have a PostgreSQL database named `studentdb` and a user named `student` with writing permissions.  This database was created as an exercise in the course.

It is also required to have `Python` installed, along with the `pandas`, `psycopg2` and `sql_queries` packages.

## Running the project.

The functions used in building the database can be found in `create_tables.py`.  To create the database and the tables described above it is necessary to run this script.

```bash
python create_tables.py
```

Then you can fill in the data by running the script `etl.py`

```bash
python etl.py
```

In order to test if the data was added correctly you can follow the notebook `test.ipynb`.
