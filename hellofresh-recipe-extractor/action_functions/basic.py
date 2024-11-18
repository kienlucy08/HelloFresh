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


class Basic:

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

    """
    Adding function that adds ingredients based on the instruction
    input: instruction sentence, ex: Add salt to the pot
    return: machine readable instruction, ex: {'action': add, 'ingredients': salt, 'location': pot}
    """

    def add(self, instruction_sentence):
        self.set_current_action("add")
        # Process the sentence using the NLP model
        doc = self.nlp(instruction_sentence)

        # Extract the relevant information from the parsed sentence
        current_ingredients, current_location = self.extract_add_info(doc)

        if current_ingredients and current_location:
            # handle added ingredients in their locations
            self.handle_added_ingredients(current_ingredients, current_location)
            self.set_previous_action("add", instruction_sentence)

            # Prepare the machine-readable instruction
            instruction = {
                'action': 'add',
                'ingredients': current_ingredients,
                'location': current_location
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    """
     Adding alternative instructions
     """

    def spread(self, instruction_sentence):
        self.add(instruction_sentence)

    def lay(self, instruction_sentence):
        self.add(instruction_sentence)

    def add_utensil(self, instruction_sentence):
        self.set_current_action("cover")
        # Process the sentence using the NLP model
        doc = self.nlp(instruction_sentence)

        utensil = None
        utensil_base = None

        for token in doc:
            if token.dep_ == "dobj" or token.dep_ == "conj":
                utensil_base = token.text
            if token.dep_ == "ROOT" and token.pos_ == 'NOUN':
                utensil_base = token.text
            if token.head.text.lower() == 'with' and token.dep_ == 'pobj':
                utensil = token.text
            if token.head.text.lower() == 'on' and token.dep_ == 'pobj':
                utensil = token.text

        if utensil:
            print(f"Covering {utensil_base} with {utensil}")
            self.set_previous_action("cover", instruction_sentence)

            # machine-readable instruction
            instruction = {
                'action': 'cover',
                'ingredient': utensil_base,
                'location': utensil
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    def put(self, instruction):
        self.add_utensil(instruction)

    """
    Top function that adds ingredients based on the instruction
    input: instruction sentence, ex: Top with salt and pepper
    return: machine readable instruction, ex: {'action': top, 'ingredients': ['salt, 'pepper'], 'location': pasta}
    """

    def top(self, instruction_sentence):
        self.set_current_action("top")

        nlp = spacy.load("en_core_web_sm")
        doc = nlp(instruction_sentence)

        # Extract the seasoning ingredients from the instruction
        with_token = False
        current_ingredients = []
        for token in doc:
            if with_token:
                current_ingredients.append(token.text)
            if token.text.lower() == "with":
                with_token = True

        if current_ingredients:
            print(f"Top with {' '.join(current_ingredients)}")
            # finished mix
            finished_mix = ' '.join(current_ingredients)
            self.fin_ingredients.append(finished_mix)
            self.update_ingredient_location(finished_mix, 'mixture')
            self.set_previous_action("top", instruction_sentence)

            # Prepare the machine-readable instruction
            instruction = {
                'action': 'top',
                'ingredients': current_ingredients,
                'location': None
            }
            return instruction

        else:
            print("Unable to parse the instruction.")
            return None

    """
    Top alternative instructions
    """

    def season(self, instruction):
        self.top(instruction)

    def brush(self, instruction_sentence):
        self.top(instruction_sentence)

    """
    Scatter function that scatter ingredients on a previous finished mix
    input: instruction sentence, ex: Scatter mixture over pasta
    return: machine readable instruction, ex: {'action': scatter, 'ingredients': mixture, 'location': pasta}
    """

    def scatter(self, instruction):
        self.set_current_action("scatter")

        doc = self.nlp(instruction)
        current_ingredients, current_location = self.extract_fill_scatter_info(doc)

        if not current_ingredients:
            current_ingredients = 'previous mixture'

        if current_ingredients and current_location:
            print(f"Scattering {current_ingredients} over {current_location}")
            # finished mix
            finished_mix = f"{current_ingredients}"
            self.fin_ingredients.append(finished_mix)
            # update location information
            self.update_ingredient_location(finished_mix, current_location)

            self.set_previous_action("scatter", instruction)

            # Prepare the machine-readable instruction
            instruction = {
                'action': 'scatter',
                'ingredients': current_ingredients,
                'location': current_location
            }
            return instruction

        else:
            print("Unable to parse the instruction.")
            return None

    """
    Fill function that fills ingredients with other ingredients
    input: instruction sentence, ex: Fill tortillas with mixture
    return: machine readable instruction, ex: {'action': fill, 'ingredients': mixture, 'location': tortillas}
    """

    def fill(self, instruction_sentence):
        self.set_current_action("fill")

        doc = self.nlp(instruction_sentence)
        current_ingredients, current_location = self.extract_fill_scatter_info(doc)

        if current_ingredients and current_location:
            print(f"Filling {current_location} with {' and '.join(current_ingredients)}")
            # finished mix
            finished_mix = f"{current_ingredients}"
            self.fin_ingredients.append(finished_mix)
            # update location information
            self.update_ingredient_location(finished_mix, current_location)

            self.set_previous_action("fill", instruction_sentence)

            # machine-readable instruction
            instruction = {
                'action': 'fill',
                'ingredients': current_ingredients,
                'location': current_location
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    """
    Remove function that removes ingredients from locations and puts them aside
    input: instruction sentence, ex: Remove chicken from heat
    return: machine readable instruction, ex: {'action': remove, 'ingredients': chicken, 'location': aside}
    """

    def remove(self, instruction_sentence):
        self.set_current_action("remove")

        doc = self.nlp(instruction_sentence)
        removed_ingredients = []
        current_location = None
        new_location = "and set aside"

        for token in doc:
            # Check for direct object or conjunction
            if token.dep_ == 'dobj' or token.dep_ == 'conj':
                removed_ingredients.append(token.text)
                self.inuse_ingredients.append(token.text)

            # Check for object location
            if token.head.text.lower() == 'from' and token.dep_ == 'pobj':
                current_location = token.text

        if current_location is None:
            current_location = "object and set aside"

        if removed_ingredients and current_location:
            for ingredient in removed_ingredients:
                print(f"Removing {ingredient} from {current_location}")
                self.update_ingredient_location(ingredient, new_location)
            finished_mix = f"{removed_ingredients}"
            self.fin_ingredients.append(finished_mix)

            self.set_previous_action("remove", instruction_sentence)

            # Prepare the machine-readable instruction
            instruction = {
                'action': 'remove',
                'ingredients': removed_ingredients,
                'location': 'aside'
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    """
    Move function that moves ingredients from an old location to a new location
    input: instruction sentence, ex: Move chicken from the plate to the stove
    return: machine readable instruction, ex: {'action': move, 'ingredients': chicken, 'location': stove}
    """

    def move(self, ingredient_sentence):
        self.set_current_action("move")
        doc = self.nlp(ingredient_sentence)
        removed_ingredients, current_location, new_location = self.extract_remove_info(doc)

        if not current_location:
            current_location = "object"

        if removed_ingredients and current_location and new_location:
            ingredient = " and ".join(removed_ingredients)
            self.update_ingredient_location(ingredient, current_location)
            self.perform_move(ingredient, current_location, new_location)
            finished_mix = f"{ingredient} from {current_location} to {new_location}"
            self.fin_ingredients.append(finished_mix)
            self.set_previous_action("move", ingredient_sentence)

            # Prepare the machine-readable instruction
            instruction = {
                'action': 'move',
                'ingredients': removed_ingredients,
                'location': current_location
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    """Alternative forms of move
    """

    def transfer(self, instruction):
        self.move(instruction)
        # output machine-readable? JSON? Luc

    def place(self, instruction):
        self.move(instruction)

    def pour(self, instruction):
        self.move(instruction)

    """
    Reserve function that reserves ingredients for later
    input: instruction sentence, ex: Reserve 1 cup of pasta cooking water
    return: machine readable instruction, ex: {'action': reserve, 'ingredients': water, 'location': aside}
    """

    def reserve(self, instruction_sentence):
        self.set_current_action("reserve")

        doc = self.nlp(instruction_sentence)

        amount = None
        current_location = "aside"
        current_ingredients = []

        for token in doc:
            if token.text.isdigit() and token.head.text == 'cup':
                amount = token.text
            if token.dep_ == 'compound' and token.head.text == 'cup':
                amount = token.text
            if token.dep_ == 'prep' and token.head.text.lower() in ['cup', 'reserve']:
                amount = token.text

            if token.dep_ == 'dobj' or token.dep_ == 'pobj' or token.dep_ == 'nsubj':
                current_ingredients.append(token.text)
                self.inuse_ingredients.append(current_ingredients)

        if amount is not None:
            for ingridient in current_ingredients:
                print(f"Reserving {amount} cup(s) of {ingridient}")
                # update location
                self.update_ingredient_location(ingridient, current_location)
            # append the new mix
            finished_mix = f"{current_ingredients}"
            self.fin_ingredients.append(finished_mix)

            self.set_previous_action("reserve", instruction_sentence)

            # Prepare the machine-readable instruction
            instruction = {
                'action': 'reserve',
                'ingredients': current_ingredients,
                'location': current_location
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    def drain(self, instruction_sentence):
        self.set_current_action("drain")
        doc = self.nlp(instruction_sentence)

        current_ingredients = []
        current_location = 'sink'

        for token in doc:
            # Check for ingredients or objects
            if token.dep_ == 'dobj' or token.dep_ == 'conj' or token.dep_ == 'ROOT':
                current_ingredients.append(token.text)

            # Check for location
            if token.dep_ == 'prep' and token.head.text.lower() == 'in':
                current_location = token.text
            if token.dep_ == 'pobj' and token.head.text.lower() == 'in':
                current_location = token.text

        if current_ingredients and current_location:
            # Perform the draining action
            for ingredient in current_ingredients:
                self.update_ingredient_location(ingredient, current_location)
                print(f"Drain {ingredient} in {current_location}")

            self.set_previous_action("drain", instruction_sentence)
            instruction = {
                'action': 'drain',
                'ingredients': current_ingredients,
                'location': current_location
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    """
    Scoop function that scoops water and sets aside for later
    input: instruction sentence, ex: Scoop 1 cup of pasta cooking water
    return: machine readable instruction, ex: {'action': scoop, 'ingredients': water, 'location': aside}
    """

    def scoop(self, instruction_sentence):
        self.set_current_action("scoop")

        doc = self.nlp(instruction_sentence)

        amount = None
        current_location = "aside"
        current_ingredient = "water"
        self.inuse_ingredients.append(current_ingredient)

        for token in doc:
            if token.head.text == 'cup':
                amount = token.text

        if amount is not None:
            print(f"Scooping out {amount} cup(s) of cooking water")
            # set location
            self.update_ingredient_location(current_ingredient, current_location)
            # set finished ingredients
            finished_mix = f"{current_ingredient}"
            self.fin_ingredients.append(finished_mix)
            self.set_previous_action("scoop", instruction_sentence)

            # Prepare the machine-readable instruction
            instruction = {
                'action': 'scoop',
                'ingredients': current_ingredient,
                'location': current_location
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    """
    Repeat function will repeat any action
    calls any action that is called previous to repeat call
    """

    def repeat(self):
        if self.previous_actions:
            last_action, last_args = self.previous_actions[-1]
            if last_action == "add":
                self.add(*last_args)
            if last_action == "remove":
                self.remove(*last_args)
            if last_action == "move":
                self.move(*last_args)
            if last_action == "scoop":
                self.scoop(*last_args)
            if last_action == "reserve":
                self.reserve(*last_args)
            if last_action == "top":
                self.reserve(*last_args)
            if last_action == "scatter":
                self.scatter(*last_args)
            if last_action == "fill":
                self.fill(*last_args)
        else:
            print("No previous action to repeat.")

    """
    Stir function that stirs a mixture
    input: instruction sentence, ex: Stir mixture to combine in a bowl
    return: machine readable instruction, ex: {'action': stir, 'ingredients': ['chicken, 'lettuce'], 'location': bowl}
    """

    def stir(self, instruction_sentence):
        self.set_current_action("stir")
        doc = self.nlp(instruction_sentence)

        # extract the ingredients and location information
        current_ingredients, current_location = self.extract_stir_info(doc)

        if current_ingredients and current_location:
            # perform the stirring action
            for ingredient in current_ingredients:
                # update locations
                self.update_ingredient_location(ingredient, current_location)
                print(f"Stir {ingredient} in {current_location}")
            # finished mix
            finished_mix = f"{current_ingredients}"
            self.fin_ingredients.append(finished_mix)

            self.set_previous_action("stir", instruction_sentence)

            instruction = {
                'action': 'stir',
                'ingredients': current_ingredients,
                'location': current_location
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    """
    Other stir functions
    """

    def whisk(self, instruction_sentence):
        self.stir(instruction_sentence)

    def toss(self, instruction_sentence):
        self.stir(instruction_sentence)

    """
    Reduce function that reduces heat of ingredients
    input: instruction sentence, ex: Reduce heat to medium low
    return: machine readable instruction, ex: {'action': reduce, 'ingredients': heat, 'duration': medium}
    """

    def reduce(self, instruction_sentence):
        self.set_current_action("reduce")
        doc = self.nlp(instruction_sentence)

        current_ingredient = None
        current_duration = None

        for token in doc:
            # Check for ingredient
            if token.dep_ == 'dobj' or token.dep_ == 'ROOT':
                current_ingredient = token.text

            # Check for duration
            if token.dep_ == 'pobj' and token.head.text.lower() == 'to':
                current_duration = token.text

        if current_ingredient and current_duration:
            # Perform the reducing action
            self.update_ingredient_location(current_ingredient, None)
            print(f"Reduce {current_ingredient} to {current_duration}")

            self.set_previous_action("reduce", instruction_sentence)
            instruction = {
                'action': 'reduce',
                'ingredients': current_ingredient,
                'location': 'stove'
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    """
    Alternative reduce function
    """

    def lower(self, instruction_sentence):
        self.reduce(instruction_sentence)

    """
    Helper methods for add, fill and scatter
    """

    def extract_fill_scatter_info(self, doc):
        current_ingredients = []
        current_location = None

        for token in doc:
            if token.dep_ == 'dobj' or token.dep_ == 'conj':
                current_ingredients.append(token.text)
                self.inuse_ingredients.append(token.text)
            if token.dep_ == 'ROOT' and token.head.text.lower() in ['buns', 'baguettes', 'mixture']:
                current_ingredients.append(token.text)
                self.inuse_ingredients.append(token.text)

            if token.head.text.lower() in ['to', 'over', 'with'] and token.dep_ == 'pobj':
                current_location = token.text

        if not current_ingredients and not current_location:
            # If the original pattern didn't match, try to extract ingredients and location separately
            for token in doc:
                if token.dep_ == 'dobj' or token.dep_ == 'conj':
                    current_ingredients.append(token.text)
                    self.inuse_ingredients.append(token.text)

                if token.head.text.lower() == 'over' and token.dep_ == 'pobj':
                    current_location = token.text

                if token.head.text.lower() == 'in' and token.dep_ == 'pobj':
                    current_location = token.text

        return current_ingredients, current_location

    def extract_stir_info(self, doc):
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

    def extract_add_info(self, doc):
        current_ingredients = []
        current_location = None

        for token in doc:
            # Check for direct object or conjunction
            if token.dep_ == 'dobj' or token.dep_ == 'conj':
                current_ingredients.append(token.text)
                self.inuse_ingredients.append(token.text)
            if token.dep_ == 'compound':
                current_ingredients.append(token.text)
                self.inuse_ingredients.append(token.text)

            # Check for object location
            if token.head.text.lower() == 'to' and token.dep_ == 'pobj':
                current_location = token.text
            if token.head.text.lower() == 'over' and token.dep_ == 'pobj':
                current_location = token.text
            if token.head.text.lower() == 'onto' and token.dep_ == 'pobj':
                current_location = token.text
            if token.head.text.lower() == 'of' and token.dep_ == 'pobj':
                current_location = token.text

        return current_ingredients, current_location

    def handle_added_ingredients(self, ingredients, location):
        ingredient = " and ".join(ingredients)
        self.update_ingredient_location(ingredient, location)

        print(f"Adding {ingredient} to {location}")
        finished_mix = f"{ingredient}"
        self.fin_ingredients.append(finished_mix)

    def add_ingredient(self, ingredient, location):
        print(f"Adding {ingredient} to {location}")
        finished_mix = f"{ingredient}"
        self.fin_ingredients.append(finished_mix)

    """
    Helper methods for remove
    """

    def extract_remove_info(self, doc):
        removed_ingredients = []
        current_location = None
        new_location = None

        for token in doc:
            if token.dep_ == 'dobj' or token.dep_ == 'conj':
                removed_ingredients.append(token.text)
                self.inuse_ingredients.append(token.text)

            if token.head.text.lower() == 'from' and token.dep_ == 'pobj':
                current_location = token.text
            if token.head.text.lower() == 'to' and token.dep_ == 'pobj':
                new_location = token.text
            if token.head.text.lower() == 'into' and token.dep_ == 'pobj':
                new_location = token.text
            if token.head.text.lower() == 'in' and token.dep_ == 'pobj':
                new_location = token.text
            if token.head.text.lower() == 'on' and token.dep_ == 'pobj':
                new_location = token.text

        return removed_ingredients, current_location, new_location

    """
    Helper methods for moving
    """

    def perform_move(self, ingredient, current_location, new_location):
        if ingredient in self.inuse_ingredients and current_location:
            self.inuse_ingredients.remove(ingredient)
            self.inuse_ingredients.append(ingredient)
            # update locations
            self.update_ingredient_location(ingredient, new_location)
            print(f"Moving {ingredient} from {current_location} to {new_location}")
            # finished mix
            finished_mix = f"{ingredient}"
            self.fin_ingredients.append(finished_mix)
        else:
            print("Unable to perform the action.")

    def update_ingredient_location(self, ingredient, location):
        if ingredient not in self.ingredient_locations:
            self.ingredient_locations[ingredient] = location
        if ingredient in self.ingredient_locations:
            existing_location = self.ingredient_locations.pop(ingredient)
            self.ingredient_locations[ingredient] = location

    """
    Setters and getters
    """

    def set_current_action(self, action):
        self.current_action = action

    def set_previous_action(self, action, *args):
        self.previous_actions.append((action, args))


if __name__ == "__main__":
    obj = Basic()
    # Example usage:
    obj.add("Add salt to the pot")
    obj.repeat()
    obj.add("Add salt and pepper to the pot")
    # Test 1: Add single ingredient to a location
    obj.add("Add salt to the pot")
    # Test 2: Add multiple ingredients to a location
    obj.add("Add salt and pepper to the pot")
    # Test 3: Add ingredients with a different location
    obj.add("Add cheese to the mixing bowl")
    # Test 6: Test a sentence with complex structure
    obj.add("Please add salt, garlic, and onion to the skillet on medium heat")
    # Test 7: Test a sentence with conjunctions and complex location
    obj.add("Add salt, pepper, and paprika to the large pot on the back burner")
    # Test 8: Test a sentence with additional modifiers
    obj.add("Carefully add lemon juice to the saucepan")
    # Test 9: Test a sentence with different prepositions
    obj.season("Season with salt, pepper, and paprika.")
    obj.scatter("Scatter tomato mixture over top")
    obj.scatter("Scatter over pasta in pan")
    obj.spread("Spread herb butter onto cut side of baguettes")
    obj.spread("Spread butter mixture onto cut sides of baguette")
    obj.top("Top with reserved ¼ cup marinara sauce")
    obj.brush("brush with half the sauce")
    obj.brush("brush chicken with remaining sauce")
    obj.fill("Fill tortillas with sausage mixture.")
    obj.fill("Fill buns with patties")
    obj.fill("Fill baguettes with chicken, arugula, and tomato, making sandwiches.")
    obj.pour("Immediately pour reserved cooking water into bowl with reserved 2 TBSP lemon juice")
    obj.reserve("Reserve 1 cup pasta cooking water (2 cups for 4 servings), then drain.")
    obj.scoop("Scoop out 1 cup cooking water, then drain")
    obj.scoop("scoop out and reserve ⅓ cup pasta cooking water")
    obj.lay("Lay a mozzarella slice on each piece of chicken")
    obj.place("Place broccoli and 1 TBSP water in a medium, microwave-safe bowl")
    obj.transfer("Transfer pasta to top rack")
    obj.remove("Remove chicken from the plate")
    obj.remove("Remove from pan and set aside.")
    obj.remove("Remove chicken from heat")
    obj.remove("remove skewers from water")
    obj.remove("Remove baby broccoli.")
    obj.scoop("Carefully scoop out ½ cup pasta cooking water, then drain.")
    obj.reserve("Reserve ¼ cup cooking water, then drain")
    obj.reserve("Reserve Â½ cup pasta cooking water, then drain.")
    obj.add_utensil("Cover pot with lid")
    obj.put("put lids on container")
    obj.stir("Stir mixture to combine in a bowl")
    obj.whisk("Slowly whisk milk in bowl")
    obj.toss("Toss salad until everything is well-coated and a thick sauce has formed in a bowl")
    obj.reduce("Reduce heat to medium low")
    obj.lower("Lower heat to medium low")
    obj.move("Move chicken to the plate")
    print(obj.ingredient_locations)
