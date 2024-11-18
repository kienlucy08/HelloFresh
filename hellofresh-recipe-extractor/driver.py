import spacy
import freq_dist_classifier


action_functions = {
    "assemble" : ["turn on", "turn off", "serve", "arrange", "turn"],
    "basic" : ["move", "remove", "mix", "add", "reduce", "lower", "drain", "repeat"],
    "cook" : ["cook in pot", "cook in pan", "toast", "cook with lid", "cook in oven", "cook in microwave", "cook"],
    "cut" : ["cut", "grate"],
    "prep" : ["wash", "dry", "preheat", "squeeze", "pick", "discard", "shape", "core"],
}

tag_consolidation = {
    "move" : ["arrange", "place", "return", "move", "pour", "take", "reserve", "scoop", "put", "set aside", "transfer"],
    "mix" : ["stir", "whisk", "toss", "combine"],
    "add" : ["sprinkle", "season", "increase", "scatter", "spread", "put", "garnish", "top", "drizzle", "fill",
             "lay", "brush"],
    "add utensil" : ["line", "put"],
    "add lid" : ["cover"],
    "cook in pot" : ["boil", "simmer", "melt", "sear"],
    "cook in pan" : ["heat", "grill", "simmer", "melt", "sear"],
    "cook in oven" : ["broil", "bake", "roast"],
    "cook with lid" : ["steam"],
    "cut" : ["trim", "cut", "mince", "chop", "break", "dice", "slice", "halve", "break up", "tear"],
    "divide" : ["divide"],
    "grate" : ["zest", "shave"],
    "wash" : ["rinse"],
    "dry" : ["pat"],
    "squeeze" : ["cinch"],
    "move (prep)" : ["discard"],
    "shape" : ["form"]
}

actions_not_requiring_nouns = ["cook with lid", "add lid", "serve", "mix"]
nouns_not_dobj = ["seconds", "minutes"]
last_used_dobj = "unknown"
last_used_pobj = "unknown"
classifier = freq_dist_classifier.returnClassifier()
nlp = spacy.load("en_core_web_sm")
def parse_instruction(instruction):
    global last_used_dobj
    global last_used_pobj
    instruction = instruction.lower()
    doc = nlp(instruction)
    num_action_verbs = count_action_verbs(doc)
    ##print(instruction + " " + str(num_action_verbs))
    ##for token in doc:
        ##print(token.text + " " + token.pos_ + " " + token.dep_)
    action_verb = "unknown"
    action_verbs = []
    pobj = find_preposition_object(doc)
    dobj = find_direct_object(doc)


    # if instruction has 1 action verb
    if num_action_verbs == 1:
        for token in doc:
            if is_action_verb(token):
                action_verb = consolidate_tag(token.text)

    # if instruction has more than one action verb
    if num_action_verbs > 1:
        for token in doc:
            if is_action_verb(token):
                action_verbs.append(consolidate_tag(token.text))

    # convert action_verbs to set while preserving order
    action_verbs = unique(action_verbs)

    # if spacy couldn't find an action verb use classifier to guess
    if action_verb == "unknown" and num_action_verbs < 1:
        action_verb = classifier.classify(freq_dist_classifier.to_freq_dist(instruction)).lower()
        action_verb = consolidate_tag(action_verb)

    # special case for add that adds all of the nouns
    if action_verb == "add":
        nouns = ""
        for token in doc:
            if token.pos_ == "NOUN":
                nouns = nouns + " " + token.text
        print("--- " + action_verb + nouns)

    elif "add" in action_verbs:
        ##print(str(action_verbs) + "HERE!")
        nouns = ""
        for token in doc:
            if token.pos_ == "NOUN":
                if token.text not in nouns_not_dobj:
                    nouns = nouns + " " + token.text
        for verb in action_verbs:
            if verb == "add": ##do the add instruction first for readability
                print("--- " + verb + nouns)
        for verb in action_verbs:
            if verb != "add":
                if verb_not_requiring_noun(verb):
                    print("--- " + verb + " ")
                else:
                    if pobj == "unknown" and dobj == "unknown":
                        print("--- " + verb)
                    elif pobj == dobj:
                        print("--- " + verb + " " + dobj)
                    elif pobj == "unknown":
                        print("--- " + verb + " " + dobj)
                    elif dobj == "unknown":
                        print("--- " + verb + " " + pobj)
                    else:
                        print("--- " + verb + " " + pobj + " " + dobj)

    # if number of action verbs is less than 1 (spacy couldn't find any) or 1
    elif num_action_verbs <= 1:
        if verb_not_requiring_noun(action_verb):
            print("--- " + action_verb + " ")
        else:
            if verb_not_requiring_noun(action_verb):
                print("--- " + action_verb + " ")
            else:
                if pobj == "unknown" and dobj == "unknown":
                    print("--- " + action_verb)
                elif pobj == dobj:
                    print("--- " + action_verb + " " + dobj)
                elif pobj == "unknown":
                    print("--- " + action_verb + " " + dobj)
                elif dobj == "unknown":
                    print("--- " + action_verb + " " + pobj)
                else:
                    print("--- " + action_verb + " " + pobj + " " + dobj)

    elif num_action_verbs > 1:
        for verb in action_verbs:
            if verb_not_requiring_noun(verb):
                print("--- " + verb + " ")
            else:
                if pobj == "unknown" and dobj == "unknown":
                    print("--- " + verb)
                elif pobj == dobj:
                    print("--- " + verb + " " + dobj)
                elif pobj == "unknown":
                    print("--- " + verb + " " + dobj)
                elif dobj == "unknown":
                    print("--- " + verb + " " + pobj)
                else:
                    print("--- " + verb + " " + pobj + " " + dobj)
def count_action_verbs(doc):
    verbs = []
    for token in doc:
        if is_action_verb(token):
            verbs.append(token.text)
    # action verbs are not counted twice
    return len(set(verbs))

# Chooses the last direct object
def find_direct_object(doc):
    dobj = "unknown"
    dobjs = []
    for token in doc:
        if token.dep_ == "dobj":
            dobjs.append(token.text)
    for word in reversed(dobjs):
        if word not in nouns_not_dobj:
            return word
    return dobj

def verb_not_requiring_noun(verb):
    return verb in actions_not_requiring_nouns

def count_direct_objects(doc):
    count = 0
    for token in doc:
        if token.dep_ == "dobj":
            count = count + 1
    return count

# find the first preposition object
def find_preposition_object(doc):
    for token in doc:
        if token.dep_ == "pobj":
            if token.text not in nouns_not_dobj:
                return token.text
    return "unknown"

def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

def count_nouns(doc):
    nouns = 0
    for token in doc:
        if token.pos_ == "NOUN":
            nouns = nouns + 1
    return nouns
def is_action_verb(token):
    return consolidate_tag(token.text) != "not found"
def consolidate_tag(tag):
    for key in tag_consolidation:
        if tag == key:
            return key
        for word in tag_consolidation[key]:
            if tag == word:
                return key
    for key in action_functions:
        for word in action_functions[key]:
            if tag == word:
                return tag
    return "not found"


def main():
    parse_instruction('Remove sausage from casings.')



if __name__ == '__main__':
    main()