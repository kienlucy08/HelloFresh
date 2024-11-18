# Cook class to define cooking-specific functions
import sqlite3
import spacy
import csv
import json
import pandas as pd


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

class Cook:
    # csv variables
    database_name = "scraped_pasta_recipes.csv"
    column_indices = [2, 3]

    # ingredient variables
    inuse_ingredients = []
    instructions = []
    unused_ingredients = []
    fin_ingredients = []
    ingredient_locations = {}

    # action variables
    previous_actions = []
    current_action = None

    def __init__(self):
        self.unused_ingredients = []
        self.instructions = []
        self.fin_ingredients = []
        self.inuse_ingredients = []
        self.ingredient_locations = {}
        self.previous_actions = []
        self.current_action = None

        # Load the English language model
        self.nlp = spacy.load('en_core_web_sm')

        self.df = import_table_from_database_to_pandas("pasta_recipes.db", "pasta_recipes")
        self.unused_ingredients = self.df['ingredients'].tolist()
        self.instructions = self.df['instructions'].tolist()

        # Parse the CSV file and extract instructions and ingredients
        # with open(self.database_name, "r") as csvfile:
        #     reader = csv.reader(csvfile)
        #     for row in reader:
        #         self.unused_ingredients.append(row[self.column_indices[0]])
        #         self.instructions.append(row[self.column_indices[1]])

    def cook(self, instruction_sentence, location, utensil="None", time=0.0):
        self.set_current_action("cook")

        # Process the sentence using the NLP model
        doc = self.nlp(instruction_sentence)

        # Extract the relevant information from the parsed sentence
        current_ingredients, current_location = self.extract_cook_info(doc)

        if current_ingredients and current_location:
            # perform cooking action
            for ingredient in current_ingredients:
                self.update_ingredient_location(current_ingredients, location)
                print(f"Cook {ingredient} in {current_location}")

            # if utensil is specified, use it
            if utensil() != "None":
                print(f"Use {utensil} for cooking.")

            # cooked ingredients
            cooked_ingredients = f"{current_ingredients}"
            self.fin_ingredients.append(cooked_ingredients)

            self.set_previous_action("cook", instruction_sentence)

            # Prepare the machine-readable instruction
            instruction = {
                'action': 'cook',
                'ingredients': current_ingredients,
                'location': current_location,
                'utensil': utensil,
                'time': time
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    # cook in pot: boil, simmer
    def boil(self, instruction_sentence):
        location = "pot"
        self.cook(instruction_sentence, location)

    def simmer(self, instruction_sentence):
        location = "pot"
        self.cook(instruction_sentence, location)

    # cook in pan: heat, grill, simmer, melt, sear
    def heat(self, instruction_sentence):
        location = "pan"
        self.cook(instruction_sentence, location)

    def grill(self, instruction_sentence):
        location = "pan"
        self.cook(instruction_sentence, location)

    def simmer(self, instruction_sentence):
        location = "pan"
        self.cook(instruction_sentence, location)

    def melt(self, instruction_sentence):
        location = "pan"
        self.cook(instruction_sentence, location)

    def sear(self, instruction_sentence):
        location = "pan"
        self.cook(instruction_sentence, location)

    # toast

    # cook with utensil: steam(pot lid)
    def steam(self, instruction_sentence):
        location = "pan"
        utensil = "lid"
        self.cook(instruction_sentence, location, utensil)

    # cook in oven: broil, bake, roast
    def broil(self, instruction_sentence):
        location = "oven"
        self.cook(instruction_sentence, location)

    def roast(self, instruction_sentence):
        location = "oven"
        self.cook(instruction_sentence, location)

    def bake(self, instruction_sentence):
        location = "oven"
        self.cook(instruction_sentence, location)

    # cook in microwave: microwave, melt
    def microwave(self, instruction_sentence):
        location = "microwave"
        self.cook(instruction_sentence, location)

    def melt_in_microwave(self, instruction_sentence):
        location = "microwave"
        self.cook(instruction_sentence, location)

    def extract_cook_info(self, doc):
        current_ingredients = []
        current_location = None

        for token in doc:
            # Check for ingredients or objects
            if token.dep_ == 'dobj' or token.dep_ == 'conj':
                current_ingredients.append(token.text)
                self.inuse_ingredients.append(token.text)

            # Check for location
            if token.dep_ == 'prep' and token.head.text.lower() == 'in':
                current_location = token.text
            if token.dep_ == 'pobj' and token.head.text.lower() == 'in':
                current_location = token.text

        return current_ingredients, current_location


    def handle_cooked_ingredients(self, ingredients, location):
        ingredient = " and ".join(ingredients)
        self.update_ingredient_location(ingredient, location)

        print(f"Cooking {ingredient} in {location}")
        finished_mix = f"{ingredient}"
        self.fin_ingredients.append(finished_mix)

    def update_ingredient_location(self, ingredient, location):
        if ingredient not in self.ingredient_locations:
            self.ingredient_locations[ingredient] = ""
        self.ingredient_locations[ingredient] = location

    """
    Setters and getters
    """

    def set_current_action(self, action):
        self.current_action = action

    def set_previous_action(self, action, *args):
        self.previous_actions.append((action, args))


if __name__ == "__main__":
    obj = Cook()
    # Test 1:
    obj.boil("Boil the pasta")
    # # Test 2:
    # obj.sear("Sear chicken in pan on high.")
