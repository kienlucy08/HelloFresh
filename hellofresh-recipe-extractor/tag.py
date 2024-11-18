import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


def tag(instructions):
    sia = SentimentIntensityAnalyzer()
    tags = []
    for instruction in instructions:
        # tokenize the instruction into words
        words = word_tokenize(instruction)

        # tag the words with their part of speech
        tagged_words = pos_tag(words)

        # calculate sentiment score for each verb and select the most important one
        verb_scores = {}
        for word, tag in tagged_words:
            if tag.startswith('VB'):
                score = sia.polarity_scores(word)['compound']
                verb_scores[word] = score

        if verb_scores:
            most_important_verb = max(verb_scores, key=verb_scores.get)
        else:
            most_important_verb = ''

        tags.append(most_important_verb)

    return tags
