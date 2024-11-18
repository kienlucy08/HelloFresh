"""Module for user interaction with the database."""
import os
import pandas as pd
import database_management as dbm

def user_interaction_fun():
    """Function to handle user interaction"""
    #if the database doesn't exist, create it
    db_name = 'pasta_recipes.db'

    if not os.path.exists(db_name):
        dbm.create_database(db_name)

        #make a pandas df with the scraped data
        filename = 'recipe_scraping/scraped_pasta_recipes.csv'
        df = pd.read_csv(filename)
        dbm.pandas_df_to_sqlite(df, db_name, 'pasta_recipes')
    
    #if the database exists, import it to a pandas df
    if os.path.exists(db_name):
        df = dbm.import_table_from_database_to_pandas(db_name, 'pasta_recipes')
    
    #print the names of the recipes
    for i, row in enumerate(df['name']):
        print(f"{i+1}. {row}")

    marker = 1
    while marker == 1:
        print("Hello, please enter a number associated with the recipe you want to make:")
        recipe_num = int(input())

        if recipe_num <= 80:
            marker += 1
        else:
            print("Invalid recipe number. Please enter a another recipe number.")
    
    print(f"Recipe: {df['name'][recipe_num-1]}")
    print(f"Ingredients: {df['ingredients'][recipe_num-1]}")
    print(f"Recipe: {df['instructions'][recipe_num-1]}")


if __name__ == "__main__":
    """Main function"""
    user_interaction_fun()
