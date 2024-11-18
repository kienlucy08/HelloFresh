import nltk

nltk.download('all')
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import pandas as pd


# verb list
def extract_verbs(doc):
    wrds = word_tokenize(doc)
    pos_tags = nltk.pos_tag(wrds)  # Part-of-Speech tags
    verbs = []
    for (word, pos) in pos_tags:
        if pos.startswith('VB'):
            verbs.append(word)
    return verbs


def verbs_freq_dist(verbs):
    freq_dist = FreqDist()
    for verb in verbs:
        verb = verb.lower()
        freq_dist[verb] += 1
    return freq_dist


# noun list
def extract_nouns(doc):
    wrds = word_tokenize(doc)
    pos_tags = nltk.pos_tag(wrds)  # Part-of-Speech tags
    nouns = []
    for (word, pos) in pos_tags:
        if pos.startswith('NN'):
            nouns.append(word)
    return nouns


def noun_freq_dist(nouns):
    freq_dist = FreqDist()
    for noun in nouns:
        noun = noun.lower()
        freq_dist[noun] += 1
    return freq_dist


# adjective list
def extract_adjectives(doc):
    wrds = word_tokenize(doc)
    pos_tags = nltk.pos_tag(wrds)  # Part-of-Speech tags
    adjectives = []
    for (word, pos) in pos_tags:
        if pos.startswith('JJ'):
            adjectives.append(word)
    return adjectives


def adj_freq_dist(adjectives):
    freq_dist = FreqDist()
    for adj in adjectives:
        adj = adj.lower()
        freq_dist[adj] += 1
    return freq_dist


