# hellofresh-recipe-extractor
Parsing HelloFresh Recipes for a Cooking Robot.

## Client

Max Conway, CS Graduate Student, max.conway@du.edu

## Description

The objective of this project is to develop a software system that can parse HelloFresh recipes and convert them into a machine-readable plan for a hypothetical cooking robot. The system will utilize web scraping, natural language processing, and planning techniques to extract relevant information from the recipes and transform them into a format that can be executed by the cooking robot.

The project will be implemented in the Python3 programming language. The system will use web scraping techniques to extract relevant data such as ingredients, quantities, cooking times, and steps from HelloFresh recipes. Natural language processing techniques will be used to process the extracted data and identify and categorize different elements of the recipe, such as ingredients, cooking methods, and cooking times. The system will then use this processed data to generate a machine-readable plan that can be executed by a cooking robot. Finally, the system will be tested thoroughly to ensure that it is accurate, reliable, and produces the expected results.

## Use

Run the user_interface program and follow the instructions in the console in order to start processing recipes into cooking instructions!

Known issues: please input an integer number when choosing your recipe, anything other than an integer will cause the program to crash. Some of the recipes are translated better than others, so have fun and use your imagination. This is partially due to us deciding to use a smaller NLP model that doesn't classify words as accurately as a larger NLP model, but we didn't want to make you download the large one as it's over 500MB. 

## Installation

For installation:

Clone the repo using GitHub link and terminal however you feel comfortable cloning a repository.
In order to install needed dependencies run the following command:

    pip install -r requirements.txt

To install the english model used in recipe parsing use this command:

    python -m spacy download en_core_web_sm

OR:
    
    python3 -m spacy download en_core_web_sm

Once downloaded to run the main driver run this command:

    python user_interface.py

OR:
    
    python3 user_interface.py

## Action Hierarchy 

In order to complete action parsing there is a hierarchy of actions for the robot to understand. For example, the robot would not know the difference between 'Top the pasta with sauce' and 'Season with salt and pepper' so both verbs fall under the category of 'Top'. Different verbs will fall under larger actions such as Prep, Cook, Assemble, Cut, and Basic (which contains actions that could be used in any step of cooking). This action hierarchy is specific to pasta recipe parsing but can be expanded based on the classes already made.

![Screenshot 2023-05-31 at 10 17 34 AM](https://github.com/dussec/hellofresh-recipe-extractor/assets/107137381/f20af946-4369-4d8c-839a-5435cddcdaea)


## Kitchen State

In order to understand the state of the kitchen, the location of all ingredients needs to be known and kept in a dictionary where their key is their location. As ingredients are added together they become a new unused ingreident for the next step of the recipe. Once the ingredient has reached its finished state it is moved into the finished ingredient category. By tracking the location of ingredients and changing them for unused to in-use to used ingredients it will be easier to track the state of the kitchen for the user.
