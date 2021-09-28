# Project: Data Modeling with Postgres.

In this repository you can find the code for the project: *Data Modeling with Postgres* of [udacity's nanodegree in data engineering](https://www.udacity.com/course/data-engineer-nanodegree--nd027).

The introduction to the project states the following:

>*A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.*

## Project Description

The idea of the project is to create an ETL pipeline using Python and SQL to transfer data from a set of JSON files located in two different directories to a collection of tables in a Postgres database. This way the analysts working in the company will be able to do their work more efficiently.

## Database schema design

The schema used for this database is a [*star schema*](https://en.wikipedia.org/wiki/Star_schema).  It consists of a fact table and four dimension tables and is structured as shown below.

![Schema](https://github.com/feauazmu/p1_deng_udacity/blob/main/static/schema.png)
