"""Module for cut instructions."""
import pandas as pd
import spacy
import csv
import json
import sqlite3
import basic
#import database_management as dbm

class Cut(basic.Basic):
    """Class for cut instructions."""
    # df = None

    # #ingredient variables
    # inuse_ingredients = []
    # instructions = []
    # unused_ingredients = []
    # fin_ingredients = []
    # ingredient_locations = {}

    # # action variables
    # previous_actions = []
    # current_action = None

    # def __init__(self):
    #     self.df = self.df
    #     self.unused_ingredients = []
    #     self.instructions = []
    #     self.fin_ingredients = []
    #     self.inuse_ingredients = []
    #     self.ingredient_locations = {}
    #     self.previous_actions = []
    #     self.current_action = None

    #     #load the English language model for spaCy
    #     self.nlp = spacy.load("en_core_web_sm")

    #     #load the database
    #     self.df = import_table_from_database_to_pandas()

    def cut(self, instruction_sentence):
        """Function for cutting ingredients."""
        self.set_current_action("cut")
        #process the sentence using the NLP model
        doc = self.nlp(instruction_sentence)

        #extract the relavant info from the parsed sentence
        current_ingredient = self.extract_cut_info(doc)
        self.handle_cut_ingredients(current_ingredient)


    def trim(self, instruction_sentence):
        """Function for trimming ingredients."""
        self.set_current_action("trim")
        #process the sentence using the NLP model
        doc = self.nlp(instruction_sentence)

        #extract the relavant info from the parsed sentence
        current_ingredient = self.extract_trim_info(doc)
        self.handle_trim_ingredients(current_ingredient)


    def divide(self, instruction_sequence):
        """Function for dividing ingredients. This is often used in serving instructions.
        This is only used when moving ingredients from cooking locations to serving or storing locations"""
        self.set_current_action("divide")
        basic.Basic.move(self, instruction_sequence)


    def chop(self, instruction_sequence):
        """Function for chopping ingredients."""
        self.set_current_action("chop")
        doc = self.nlp(instruction_sequence)

        current_ingredient = self.extract_chop_info(doc)
        self.handle_chop_ingredients(current_ingredient)

    def dice(self, instruction_sequence):
        """Function for dicing ingredients."""
        self.set_current_action("dice")
        self.chop(instruction_sequence)
    

    def mince(self, instruction_sequence):
        """Function for mincing ingredients."""
        self.set_current_action("mince")
        self.chop(instruction_sequence)


    def slice(self, instruction_sequence):
        """Function for slicing ingredients."""
        self.set_current_action("slice")
        self.chop(instruction_sequence)


    def zest(self, instruction_sequence):
        """Function for zesting ingredients."""
        self.set_current_action("zest")
        doc = self.nlp(instruction_sequence)

        current_ingredient = self.extract_zest_info(doc)
        self.handle_zest_ingredients(current_ingredient)

    
    def grate(self, instruction_sequence):
        """Function for grating ingredients."""
        self.set_current_action("grate")
        self.zest(instruction_sequence) #probably close enough


    def shave(self, instruction_sequence):
        """Function for shaving ingredients."""
        self.set_current_action("shave")
        self.zest(instruction_sequence) #probably close enough

    
    def break_up(self, instruction_sequence):
        """Function for breaking up ingredients."""
        self.set_current_action("break up")
        self.cut(instruction_sequence)


    def break_fun(self, instruction_sequence):
        """Function for breaking up ingredients."""
        #NOTE: must be called break_fun because break is a reserved keyword
        self.set_current_action("break")
        self.cut(instruction_sequence)


    def halve(self, instruction_sequence):
        """Function for halving ingredients."""
        self.set_current_action("Halve")
        self.cut(instruction_sequence)
    

    def extract_cut_info(self, doc):
        """Extracts the ingredient to be cut from the sentence."""
        current_ingredients = []

        for token in doc:
            # Check for direct object or conjunction
            if token.dep_ == 'dobj' or token.dep_ == 'conj':
                current_ingredients.append(token.text)
                self.inuse_ingredients.append(token.text)

            # NOTE: Probably doesn't need location information. Just need to know what to cut.
            # This seems to be backed up by recipies I looked at

        return current_ingredients
    

    def extract_trim_info(self, doc):
        """Extracts the ingredient to be trimmed from the sentence."""
        current_ingredients = []

        for token in doc:
            # Check for direct object or conjunction
            if token.dep_ == 'dobj' or token.dep_ == 'conj':
                current_ingredients.append(token.text)
                self.inuse_ingredients.append(token.text)

            # NOTE: Probably doesn't need location information. Just need to know what to cut.
            # This seems to be backed up by recipies I looked at

        return current_ingredients
    

    def extract_chop_info(self, doc):
        """Extracts the ingredient to be chopped from the sentence."""
        current_ingredients = []

        for token in doc:
            # Check for direct object or conjunction
            if token.dep_ == 'dobj' or token.dep_ == 'conj':
                current_ingredients.append(token.text)
                self.inuse_ingredients.append(token.text)

            # NOTE: Probably doesn't need location information. Just need to know what to cut.
            # This seems to be backed up by recipies I looked at

            return current_ingredients
        
    def extract_zest_info(self, doc):
        """Extracts the ingredient to be zested from the sentence."""
        current_ingredients = []

        for token in doc:
            # Check for direct object or conjunction
            if token.dep_ == 'dobj' or token.dep_ == 'conj':
                current_ingredients.append(token.text)
                self.inuse_ingredients.append(token.text)

            # NOTE: Probably doesn't need location information. Just need to know what to cut.
            # This seems to be backed up by recipies I looked at
    
    
    def handle_cut_ingredients(self, current_ingredients):
        """Handles the cutting of the ingredients."""
        ingredient = " and ".join(current_ingredients)
        
        print("Cutting " + ingredient + ".")
        finished_cut = f"Cut {ingredient}"
        self.fin_ingredients.append(finished_cut)


    def handle_trim_ingredients(self, current_ingredients):
        """Handles the trimming of the ingredients."""
        ingredient = " and ".join(current_ingredients)
        
        print("Trimming " + ingredient + ".")
        finished_trim = f"Trimmed {ingredient}"
        self.unused_ingredients.append(finished_trim)

    
    def handle_chop_ingredients(self, current_ingredients):
        """Handles the chopping of the ingredients."""
        ingredient = " and ".join(current_ingredients)
        
        print("Chopping " + ingredient + ".")
        finished_chop = f"Chopped {ingredient}"
        self.fin_ingredients.append(finished_chop)

    
    def handle_zest_ingredients(self, current_ingredients):
        """Handles the zesting of the ingredients."""
        ingredient = " and ".join(current_ingredients)
        
        print("Zesting " + ingredient + ".")
        finished_zest = f"Zested {ingredient}"
        self.fin_ingredients.append(finished_zest)


if __name__ == "__main__":
    """Main function"""
    cut = Cut()
    print(cut.df)

    # cut.cut("Cut the carrots")
    # print(cut.fin_ingredients)
    # print(cut.inuse_ingredients)
    # cut.cut("Cut the chicken and the onions")
    # print(cut.fin_ingredients)
    # print(cut.inuse_ingredients)

    cut.trim("Trim the broccoli")
    print(cut.fin_ingredients)
    print(cut.inuse_ingredients)
    cut.trim("Trim the pineapple and the peppers")
    print(cut.fin_ingredients)
    print(cut.inuse_ingredients)
