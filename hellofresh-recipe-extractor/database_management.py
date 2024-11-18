"""Module: database_management.py
This module contains functions for managing the database. Import these into files where they are needed."""

import sqlite3
import os
import sys
import pandas as pd


def create_database(database_name):
    """Creates a database with the given name."""
    try:
        conn = sqlite3.connect(database_name)
        conn.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def pandas_df_to_sqlite(df, database_name, table_name):
    """Saves a pandas dataframe to a sqlite database."""
    try:
        conn = sqlite3.connect(database_name)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        # display the table
        conn.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def print_table_from_database(database_name, table_name):
    """Prints the contents of the database.
    Used for debugging."""
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def import_table_from_database_to_pandas(database_name, table_name):
    """Imports the contents of the database into a pandas dataframe."""
    try:
        conn = sqlite3.connect(database_name)
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        conn.close()
        return df
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
        return None


if __name__ == "__main__":
    """Main function"""
    filename = 'recipe_scraping/scraped_pasta_recipes.csv'
    df = pd.read_csv(filename)

    database_name = 'pasta_recipes.db'
    table_name = 'pasta_recipes'
    create_database(database_name)

    pandas_df_to_sqlite(df, database_name, table_name)

    print_table_from_database(database_name, table_name)

    df = import_table_from_database_to_pandas(database_name, table_name)
    print(df)
