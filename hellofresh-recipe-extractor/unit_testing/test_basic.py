import unittest
from unittest.mock import patch
from io import StringIO
import sys
import json
from action_functions.basic import Basic


class TestBasic(unittest.TestCase):

    def setUp(self):
        self.basic = Basic()

    def test_add(self):
        instruction_sentence = "Add salt to the pot"
        expected_output = {
            'action': 'add',
            'ingredients': ['salt'],
            'location': 'pot'
        }
        self.assertEqual(self.basic.add(instruction_sentence), expected_output)

    def test_add_unable_to_parse(self):
        instruction = "Invalid instruction"
        expected_output = None
        self.assertEqual(self.basic.add(instruction), expected_output)

    def test_add_utensil(self):
        instruction_sentence = "Cover the dish with aluminum foil"
        expected_output = {
            'action': 'cover',
            'ingredient': 'dish',
            'location': 'foil'
        }
        self.assertEqual(self.basic.add_utensil(instruction_sentence), expected_output)

    def test_top(self):
        instruction_sentence = "Top with salt and pepper"
        expected_output = {
            'action': 'top',
            'ingredients': ['salt', 'and', 'pepper'],
            'location': None
        }
        self.assertEqual(self.basic.top(instruction_sentence), expected_output)

    def test_scatter(self):
        instruction_sentence = "Scatter mixture over pasta"
        expected_output = {
            'action': 'scatter',
            'ingredients': ['mixture'],
            'location': 'pasta'
        }
        self.assertEqual(self.basic.scatter(instruction_sentence), expected_output)

    def test_fill(self):
        instruction_sentence = "Fill tortillas with mixture"
        expected_output = {
            'action': 'fill',
            'ingredients': ['tortillas'],
            'location': 'mixture'
        }
        self.assertEqual(self.basic.fill(instruction_sentence), expected_output)

    def test_remove(self):
        instruction_sentence = "Remove chicken from heat"
        expected_output = {
            'action': 'remove',
            'ingredients': ['chicken'],
            'location': 'aside'
        }
        self.assertEqual(self.basic.remove(instruction_sentence), expected_output)

    def test_move(self):
        instruction_sentence = "Move chicken from the plate to the stove"
        expected_output = {
            'action': 'move',
            'ingredients': ['chicken'],
            'location': 'plate'
        }
        self.assertEqual(self.basic.move(instruction_sentence), expected_output)

    def test_reserve(self):
        instruction_sentence = "Reserve 1 cup of pasta cooking water"
        expected_output = {
            'action': 'reserve',
            'ingredients': ['water'],
            'location': 'aside'
        }
        self.assertEqual(self.basic.reserve(instruction_sentence), expected_output)

    def test_drain(self):
        instruction_sentence = "Drain pasta in the sink"
        expected_output = {
            'action': 'drain',
            'ingredients': ['pasta'],
            'location': 'sink'
        }
        self.assertEqual(self.basic.drain(instruction_sentence), expected_output)

    def test_scoop(self):
        instruction_sentence = "Scoop 1 cup of pasta cooking water"
        expected_output = {
            'action': 'scoop',
            'ingredients': 'water',
            'location': 'aside'
        }
        self.assertEqual(self.basic.scoop(instruction_sentence), expected_output)

    def test_reduce(self):
        instruction_sentence = "Reduce heat to medium low"
        expected_output = {
            'action': 'reduce',
            'ingredients': 'heat',
            'location': 'stove'
        }
        self.assertEqual(self.basic.reduce(instruction_sentence), expected_output)

    def test_stir(self):
        instruction_sentence = "Stir mixture to combine in a bowl"
        expected_output = {
            'action': 'stir',
            'ingredients': ['mixture'],
            'location': 'bowl'
        }
        self.assertEqual(self.basic.stir(instruction_sentence), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_repeat_no_previous_action(self, mock_stdout):
        self.basic.repeat()
        self.assertEqual(mock_stdout.getvalue().strip(), "No previous action to repeat.")
