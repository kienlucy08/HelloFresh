import unittest
import tag


class TestTag(unittest.TestCase):
    """
       Test for tag function to test the tag lengths are the same
       Asserts equal lengths
    """

    def test_tag_length(self):
        instructions = ["This is a test instruction", "Another test instruction"]
        tags = tag.tag(instructions)
        self.assertEqual(len(tags), len(instructions))

    """
       Test tag function with a single instruction
       Assert equal tagged words
    """

    def test_tag_single_instruction(self):
        instruction = "Wash all produce"
        tags = tag.tag([instruction])
        self.assertEqual(tags, ['Wash'])

    """
       Test tag function with multiple instructions
       Assert equal tagged words
    """

    def test_tag_multiple_instruction(self):
        instruction = "Wash and dry all produce"
        tags = tag.tag([instruction])
        self.assertEqual(tags, ['Wash', 'dry'])

    """
       Test tag function with no verbs active
       Assert equal with an empty string
    """

    def test_tag_no_verbs(self):
        instructions = ["Test instruction"]
        tags = tag.tag(instructions)
        self.assertEqual(tags, [''])
