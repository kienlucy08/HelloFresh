import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def separate(instructions):
    new_instructions = []
    for instruction in instructions:
        # tokenize the instruction into words
        words = word_tokenize(instruction)

        # tag the words with their part of speech
        tagged_words = pos_tag(words)

        # create separate instructions for each verb
        verbs = []
        current_instruction = ''
        for word, tag in tagged_words:
            if tag.startswith('VB'):
                verbs.append(word)
                if current_instruction:
                    new_instructions.append(current_instruction)
                current_instruction = word
            elif current_instruction:
                current_instruction += ' ' + word
        if current_instruction:
            new_instructions.append(current_instruction)

    return new_instructions
