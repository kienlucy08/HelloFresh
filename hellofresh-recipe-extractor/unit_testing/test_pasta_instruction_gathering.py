"""Testing for pasta_instruction_gathering.py"""
import unittest
from recipe_scraping import pasta_instruction_gathering
from constants import recipe_links, orzo_instuct, serloin_instuct, orzo_ingred, serloin_ingred
from recipe_scrapers import scrape_me
import pandas as pd


class TestPastaInstructionGathering(unittest.TestCase):
    """
       Test for get children links function with a valid pasta recipe link
       @returns true if the child links are correct
    """

    def test_get_children_links_valid_link(self):
        # Valid link
        link = "https://www.hellofresh.com/recipes/pasta-recipes/popular?page=8"
        children_links = pasta_instruction_gathering.get_children_links(link)
        # Assert that the returned value is a list
        self.assertIsInstance(children_links, list)

    """
       Test for get children links function with an invalid pasta recipe link
       @raises an exception if the link is invalid
    """

    def test_get_children_links_invalid_link(self):
        # Link that isn't hellofresh.com
        invalid_link = "https://www.invalidlink.com"
        with self.assertRaises(Exception):
            # raise an exception when there is an invalid link
            pasta_instruction_gathering.get_children_links(invalid_link)

    """
       Test for get children links function with an empty link
       @raises an exception when the link is empty
    """

    def test_get_children_links_empty_link(self):
        # Empty link
        empty_link = ""
        with self.assertRaises(Exception):
            # raise an exception when there is an empty link
            pasta_instruction_gathering.get_children_links(empty_link)

    """
       Test for get trim links function with an empty link
       @raises an exception when the link is empty
    """

    def test_trim_links(self):
        # Valid link
        link = "https://www.hellofresh.com/recipes/pasta-recipes/popular?page=8"
        accurate_trimmed_links = recipe_links
        children_links = pasta_instruction_gathering.get_children_links(link)
        trim_link = pasta_instruction_gathering.trim_links(children_links)
        # Assert that the two lists of links are equal
        self.assertEqual(trim_link, accurate_trimmed_links)

    """
       Test for make data frame function with a test frame
       Asserts equal to the dataframe made in the function
    """

    def test_make_data_frame_list(self):
        # dataframe build
        test_frame = ['link', 'name', 'ingredients', 'instructions']
        self.assertEqual(test_frame, list(pasta_instruction_gathering.make_data_frame()))

    """
       Test for get children links function with an empty link
       Assert true for an empty dataframe 
    """

    def test_empty_dataframe(self):
        test_frame = pasta_instruction_gathering.make_data_frame().empty
        self.assertTrue(test_frame, pasta_instruction_gathering.make_data_frame().empty)

    """
       Test for recipe names with from a link
       Assert equal with the function return and the mock return
    """

    def test_get_recipe_name_from_link(self):
        mock_scraper = scrape_me(
            "https://www.hellofresh.com/recipes/winner-winner-chicken-orzo-dinner-5aaabf7530006c52b54bd0c2")
        mock_scraper_title = mock_scraper.title()
        result = pasta_instruction_gathering.get_recipe_name(
            "https://www.hellofresh.com/recipes/winner-winner-chicken-orzo-dinner-5aaabf7530006c52b54bd0c2")
        self.assertEqual(result, mock_scraper_title)

    """
       Test for get ingredients from a link
       Assert equal with the function return and the mock return
    """

    def test_get_ingredients_from_link(self):
        mock_scraper = scrape_me(
            "https://www.hellofresh.com/recipes/winner-winner-chicken-orzo-dinner-5aaabf7530006c52b54bd0c2")
        mock_scraper_ingredients = mock_scraper.ingredients()
        result = pasta_instruction_gathering.get_ingredients(
            "https://www.hellofresh.com/recipes/winner-winner-chicken-orzo-dinner-5aaabf7530006c52b54bd0c2")
        self.assertEqual(result, mock_scraper_ingredients)

    """
       Test for get instructions from a link
       Assert equal with the function return and the mock return
    """

    def test_get_instructions_from_link(self):
        mock_scraper = scrape_me(
            "https://www.hellofresh.com/recipes/winner-winner-chicken-orzo-dinner-5aaabf7530006c52b54bd0c2")
        mock_scraper_instructions = mock_scraper.instructions_list()
        result = pasta_instruction_gathering.get_instructions(
            "https://www.hellofresh.com/recipes/winner-winner-chicken-orzo-dinner-5aaabf7530006c52b54bd0c2")
        self.assertEqual(result, mock_scraper_instructions)

    """
        Test for processing links which inherently tests all subordinate functions as well
        Assert equal with the processed links and the instructions, ingredients, and name
    """

    def test_process_links(self):
        # create a list of links for testing
        links = [
            'https://www.hellofresh.com/recipes/winner-winner-chicken-orzo-dinner-5aaabf7530006c52b54bd0c2',
            'https://www.hellofresh.com/recipes/herbed-sirloin-steak-594a7f5b4f78db042847ada2'
        ]
        # call the function to test
        result = pasta_instruction_gathering.process_links(links)
        # assert that the result is a pandas dataframe
        self.assertIsInstance(result, pd.DataFrame)
        # assert that the length of the result is equal to the length of links
        self.assertEqual(len(result), len(links))
        # assert that the dataframe has the correct columns
        self.assertListEqual(list(result.columns), ['link', 'name', 'ingredients', 'instructions'])
        # assert that the name of the first recipe is correct
        self.assertEqual(result.loc[0, 'name'], 'Winner Winner Chicken Orzo Dinner with Cheesy Roasted Zucchini and '
                                                'Tomato')
        # assert that the name of the second recipe is correct
        self.assertEqual(result.loc[1, 'name'], 'Herbed Sirloin Steak over Orzo Pasta Salad')
        # assert that the ingredients of the first recipe are correct
        self.assertEqual(result.loc[0, 'ingredients'], orzo_ingred)
        # assert that the instructions of the first recipe are correct
        self.assertEqual(result.loc[0, 'instructions'], orzo_instuct)
        # assert that the instructions of the second recipe are correct
        self.assertEqual(result.loc[1, 'instructions'], serloin_instuct)
        # assert that the ingredients of the second recipe are correct
        self.assertEqual(result.loc[0, 'ingredients'], serloin_ingred)
