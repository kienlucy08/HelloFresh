import pos
import separate
import spacy
import basic


class Prep(basic.Basic):
    def extract_verbs(self, sentence):
        """
        This function takes a sentence as input and returns a list of verbs in the sentence.
        """
        # Load the English language model
        nlp = spacy.load("en_core_web_sm")
        # Parse the sentence using the language model
        doc = nlp(sentence)
        # Extract the verbs from the parsed sentence
        verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
        return verbs

    def preheat(self, instruction):
        """
            Preheat action function which takes an instruction, finds preheat verb and outputs preheating actions
        """
        # set temp and unit to none
        temperature = None
        unit = None
        # extract the verbs from the given instruction
        verbs = self.extract_verbs(instruction)
        # go through all verbs and if preheat is found set temp and index
        for verb in verbs:
            if verb == "preheat":
                words = pos.word_tokenize(instruction)
                index = words.index("to")
                temperature = words[index + 1]
                # set the unit to degrees
                if "degree" in words[index + 2]:
                    unit = "degrees"
                elif "°" in words[index + 2]:
                    unit = "°"
                break
        # if a temp and unit is found preheat the oven to that temp and unit
        if temperature and unit:
            print(f"Preheat oven to {temperature} {unit}.")
            # Prepare the machine-readable instruction
            instruction = {
                'action': 'preheat',
                'temperature': temperature,
                'location': 'oven'
            }
            return instruction
        else:
            print("Could not extract oven temperature from instruction.")
            return None

    def wash_and_dry(self, instruction):
        """
            Wash action function which takes an instruction, finds wash verb and outputs wash actions
        """
        # extract the verbs from the given instruction
        verbs = self.extract_verbs(instruction)
        nouns = pos.extract_nouns(instruction)
        wash = None
        dry = None
        # go through all verbs find wash and dry
        for verb in verbs:
            if verb == "wash".lower():
                wash = "Wash"
            if verb == "dry".lower():
                dry = "Dry"
            if verb == "rinse".lower():
                for noun in nouns:
                    if noun == "shrimp".lower():
                        rinse_noun = "shrimp"
                    if noun == "pan".lower():
                        rinse_noun = "pan"
                rinse = "Rinse"
        # if wash and dry were found print out the recipe
        if wash:
            print(f"{wash} all produce.")
            # Prepare the machine-readable instruction
            instruction = {
                'action': 'wash',
                'ingredients': 'produce',
                'location': 'sink'
            }
            return instruction
        if dry:
            print(f"{dry} all produce")
            # Prepare the machine-readable instruction
            instruction = {
                'action': 'dry',
                'ingredients': 'produce',
                'location': 'sink'
            }
            return instruction
        if wash is None and dry is None:
            print("Could not extract wash and dry from instruction.")
            return None

    def squeeze(self, instruction):
        """
            Squeeze action function which takes an instruction, finds squeeze verb and outputs squeezing actions
        """
        squeeze = None
        squeeze_noun = None
        # extract the verbs & nouns from the given instruction
        verbs = self.extract_verbs(instruction)
        nouns = pos.extract_nouns(instruction)
        # go through all verbs find squeeze verb
        for verb in verbs:
            if verb == "squeeze".lower():
                for noun in nouns:
                    if noun == "of lemon".lower():
                        squeeze_noun = "lemon"
                    if noun == "juice".lower():
                        squeeze_noun = "lemon"
                    if noun == "or two".lower():
                        squeeze_noun = "lemon"
                    if noun == "1 TBSP".lower():
                        squeeze_noun = "lemon"
                squeeze = "Squeeze"
        # if squeeze is found print out the recipe
        if squeeze:
            print(f"{squeeze} {squeeze_noun}")
            # Prepare the machine-readable instruction
            instruction = {
                'action': 'squeeze',
                'ingredients': squeeze_noun,
                'location': ''
            }
            return instruction
        if squeeze is None:
            print("Could not extract squeeze from instruction.")
            return None

    def pick(self, instruction):
        """
            Pick action function which takes an instruction, finds pick verb and outputs picking actions
        """
        pick = None
        pick_noun = None
        # extract the verbs & nouns from the given instruction
        verbs = self.extract_verbs(instruction)
        nouns = pos.extract_nouns(instruction)
        # go through all verbs find pick verb
        for verb in verbs:
            if verb == "pick".lower():
                for noun in nouns:
                    if noun == "leaves".lower():
                        pick_noun = "leaves"
                    if noun == "oregano".lower():
                        pick_noun = "oregano leaves"
                    if noun == "parsley leaves".lower():
                        pick_noun = "parsley leaves"
                    if noun == "mint leaves".lower():
                        pick_noun = "mint leaves"
                pick = "Pick"
        # if pick is found print out the recipe
        if pick:
            print(f"{pick} {pick_noun}")
            # Prepare the machine-readable instruction
            instruction = {
                'action': 'pick',
                'ingredients': pick_noun,
                'location': ''
            }
            return instruction
        if pick is None:
            print("Could not extract pick from instruction.")
            return None

    def pat(self, instruction):
        """
            Pat action function which takes an instruction, finds pat verb and outputs patting actions
        """
        pat = None
        pat_noun = None
        # extract the verbs & nouns from the given instruction
        verbs = self.extract_verbs(instruction)
        nouns = pos.extract_nouns(instruction)
        # go through all verbs find pat verb
        for verb in verbs:
            if verb == "pat".lower():
                for noun in nouns:
                    if noun == "chicken".lower():
                        pat_noun = "chicken"
                    if noun == "steak".lower():
                        pat_noun = "steak"
                pat = "Pat"
        # if pat is found print out the recipe
        if pat:
            print(f"{pat} {pat_noun} dry")
            # Prepare the machine-readable instruction
            instruction = {
                'action': 'pat',
                'ingredients': pat_noun,
                'location': ''
            }
            return instruction
        if pat is None:
            print("Could not extract pat from instruction.")
            return None

    def increase(self, instruction_sentence):
        self.add(instruction_sentence)

    def discard(self, instruction):
        """
            Discard action function which takes an instruction, finds discard verb and outputs discarding actions
        """
        discard = None
        discard_noun = None
        # extract the verbs & nouns from the given instruction
        verbs = self.extract_verbs(instruction)
        nouns = pos.extract_nouns(instruction)
        # go through all verbs find discard verb
        for verb in verbs:
            if verb == "discard".lower():
                for noun in nouns:
                    if noun == "stems".lower():
                        discard_noun = "stems"
                    if noun == "casings".lower():
                        discard_noun = "casings"
                    if noun == "cores".lower():
                        discard_noun = "cores & stems"
                    if noun == "ends".lower():
                        discard_noun = "the ends"
                discard = "Discard"
            # if discard is found print out the recipe
            if discard:
                print(f"{discard} {discard_noun}")
                # Prepare the machine-readable instruction
                instruction = {
                    'action': 'discard',
                    'ingredients': discard_noun,
                    'location': 'trash'
                }
                return instruction
            if discard is None:
                print("Could not extract discard from instruction.")
                return None

    # def adjust(self, instruction):
    #     """
    #         Adjust action function which takes an instruction, finds adjust verb and outputs adjusting actions
    #     """
    #     adjust = None
    #     # extract the verbs & nouns from the given instruction
    #     verbs = self.extract_verbs(instruction)
    #     # go through all verbs find adjust verb
    #     for verb in verbs:
    #         if verb == "adjust".lower():
    #             adjust = "adjust"
    #     # if adjust is found print out the recipe
    #     if adjust:
    #         print(f"{adjust} oven rack")
    #     if adjust is None:
    #         print("Could not extract adjust from instruction")

    def core(self, instruction):
        """
            Core action function which takes an instruction, finds core verb and outputs coring actions
        """
        core = None
        core_noun = None
        # extract the verbs & nouns from the given instruction
        verbs = self.extract_verbs(instruction)
        nouns = pos.extract_nouns(instruction)
        # go through all verbs find core verb
        for verb in verbs:
            if verb == "core".lower():
                for noun in nouns:
                    if noun == "pepper".lower():
                        core_noun = "pepper"
                    if noun == "tomato".lower():
                        core_noun = "tomato"
                core = "core"
        # if core is found print out the recipe
        if core:
            print(f"{core} {core_noun}")
            # Prepare the machine-readable instruction
            instruction = {
                'action': 'core',
                'ingredients': core_noun,
                'location': ''
            }
            return instruction
        if core is None:
            print("Could not extract core from instruction")
            return None

    # def peel(self, instruction):
    #     """
    #         Peel action function which takes an instruction, finds peel verb and outputs peeling actions
    #     """
    #     peel = None
    #     # extract the verbs & nouns from the given instruction
    #     verbs = self.extract_verbs(instruction)
    #     # go through all verbs find peel verb
    #     for verb in verbs:
    #         if verb == "peel".lower():
    #             peel = "peel"
    #     # if peel is found print out the recipe
    #     if peel:
    #         print(f"{peel}")
    #         # Prepare the machine-readable instruction
    #     if peel is None:
    #         print("Could not extract peel from instruction")

    def line_baking_sheet(self, instruction_sentence):
        self.set_current_action("line")

        # Process the sentence using the NLP model
        doc = self.nlp(instruction_sentence)

        utensil = None
        material = None

        # Iterate over the tokens in the parsed sentence
        for token in doc:
            if token.dep_ == "dobj":
                utensil = token.text
            elif token.dep_ == "prep":
                material = token.text

        if utensil and material:
            print(f"Line {utensil} with {material}")
            self.set_previous_action("line", instruction_sentence)

            # Prepare the machine-readable instruction
            instruction = {
                'action': 'line',
                'utensil': utensil,
                'material': material
            }
            return instruction
        else:
            print("Unable to parse the instruction.")
            return None

    # cut?
    def tear(self, instruction):
        """
            Tear action function which takes an instruction, finds tear verb and outputs tearing actions
        """
        tear = None
        tear_noun = None
        # extract the verbs & nouns from the given instruction
        verbs = self.extract_verbs(instruction)
        nouns = pos.extract_nouns(instruction)
        # go through all verbs find tear verb
        for verb in verbs:
            if verb == "tear".lower():
                for noun in nouns:
                    if noun == "leaves".lower():
                        tear_noun = "leaves"
                    if noun == "mozzarella".lower():
                        tear_noun = "mozzarella"
                tear = "tear"
        # if tear is found print out the recipe
        if tear:
            print(f"{tear} {tear_noun}")
            # Prepare the machine-readable instruction
            instruction = {
                'action': 'tear',
                'ingredients': tear_noun,
            }
            return instruction
        if tear is None:
            print("Could not extract tear from instruction")
            return None

    def wipe(self, instruction):
        """
            Wipe action function which takes an instruction, finds wipe verb and outputs wiping actions
        """
        wipe = None
        # extract the verbs & nouns from the given instruction
        verbs = self.extract_verbs(instruction)
        # go through all verbs find wipe verb
        for verb in verbs:
            if verb == "wipe".lower():
                wipe = "wipe"
        # if wipe is found print out the recipe
        if wipe:
            print(f"{wipe} out pan")
            # Prepare the machine-readable instruction
            instruction = {
                'action': 'wipe',
                'utensil': 'pan'
            }
            return instruction
        if wipe:
            print("Could not extract wipe from instruction")
            return None

    def shape(self, instruction):
        """
            Shape action function which takes an instruction, finds shape verb and outputs shaping actions
        """
        shape = None
        shape_noun = None
        # extract the verbs & nouns from the given instruction
        verbs = self.extract_verbs(instruction)
        nouns = pos.extract_nouns(instruction)
        # go through all verbs find shape verb
        for verb in verbs:
            if verb == "shape".lower():
                for noun in nouns:
                    if noun == "patties".lower():
                        shape_noun = "into patties"
                    if noun == "meatballs".lower():
                        shape_noun = "into meatballs"
                shape = "shape"
        # if shape is found print out the recipe
        if shape:
            print(f"{shape} {shape_noun}")
            # Prepare the machine-readable instruction
            instruction = {
                'action': 'shape',
                'ingredients': shape_noun,
            }
            return instruction
        if shape is None:
            print("Could not extract shape from instruction")

    def form(self, instruction):
        self.shape(instruction)

    def brush(self, instruction):
        """
            Brush action function which takes an instruction, finds brush verb and outputs brushing actions
        """
        brush = None
        # extract the verbs & nouns from the given instruction
        verbs = self.extract_verbs(instruction)
        # go through all verbs find shape verb
        for verb in verbs:
            if verb == "brush".lower():
                brush = "brush"
        # if brush is found print out the recipe
        if brush:
            print(f"{brush} with sauce ")
            # Prepare the machine-readable instruction
            instruction = {
                'action': 'brush',
                'ingredients': 'sauce',
            }
            return instruction
        if brush is None:
            print("Could not extract brush instruction")


if __name__ == "__main__":
    obj = Prep()
    obj.preheat('preheat oven to 425 degrees.')
    obj.preheat('Adjust the rack and preheat oven to 425 degrees')
    obj.wash_and_dry('Wash and dry all produce')
    obj.squeeze('Squeeze lemon')
    obj.pick('Pick leaves')
    obj.pat('Pat meat dry')
    obj.discard('Discard stems')
    obj.core('Core vegetable')
    obj.tear('Tear leaves')
    obj.wipe('Wipe out pan')
    obj.shape('Shape meat')
    obj.brush('Brush with sauce')
