"""Module for user interaction with the database."""
import os
import pandas as pd
import database_management as dbm
import re
from nltk.tokenize import regexp_tokenize
import driver
def user_interaction_fun():
    """Function to handle user interaction"""
    # if the database doesn't exist, create it
    db_name = 'pasta_recipes.db'

    if not os.path.exists(db_name):
        dbm.create_database(db_name)

        # make a pandas df with the scraped data
        filename = 'recipe_scraping/scraped_pasta_recipes.csv'
        df = pd.read_csv(filename)
        dbm.pandas_df_to_sqlite(df, db_name, 'pasta_recipes')

    # if the database exists, import it to a pandas df
    if os.path.exists(db_name):
        df = dbm.import_table_from_database_to_pandas(db_name, 'pasta_recipes')


    running = True
    while running:
        choosing = True
        # print the names of the recipes
        for i, row in enumerate(df['name']):
            print(f"{i + 1}. {row}")
        while choosing:
            print("Please enter a number associated with the recipe you want to make:")
            recipe_num = int(input())
            if not int(recipe_num) or recipe_num > 80:
                print("Invalid recipe number.")
            else:
                choosing = False

        print(f"Recipe: {df['name'][recipe_num - 1]}")
        print(f"Ingredients: {df['ingredients'][recipe_num - 1]}")
        instructions = df['instructions'][recipe_num - 1]
        tokens = instructions_to_list(instructions)
        for instruction in tokens:
            instruction = re.sub(r'[\[\]\']', '', instruction)
            driver.parse_instruction(instruction)
        #print(f"Recipe: {df['instructions'][recipe_num - 1]}")
        choosing = True
        while choosing:
            print("Would you like to choose another recipe? Type 'y' for yes, 'n' for no")
            y_or_n = str(input())
            if y_or_n == "n":
                choosing = False
                running = False
            elif y_or_n != "y":
                print("invalid input.")
            else:
                choosing = False


def instructions_to_list(instructions):
    modified = re.sub(r',', '', instructions)
    sentences = re.findall(r'[^.!?]+[.!?]', modified)
    return sentences

if __name__ == "__main__":
    """Main function"""
    user_interaction_fun()