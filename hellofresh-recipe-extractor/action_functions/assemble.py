import basic


class Assemble(basic.Basic):

    def serve(self, instruction_sentence):
        self.set_current_action("serve")

        # Extract serving instructions from the instruction sentence
        serving_instructions = self.extract_serving_instructions(instruction_sentence)

        if serving_instructions:
            # Perform the serving action
            for serving_instruction in serving_instructions:
                print(f"Serve {serving_instruction}")

            self.set_previous_action("serve", instruction_sentence)
        else:
            print("Unable to parse the instruction.")

    def arrange(self, instruction):
        self.move(instruction)

    def drizzle(self, instruction_sentence):
        self.top(instruction_sentence)

    def combine(self, instruction_sentence):
        self.stir(instruction_sentence)

    def sprinkle(self, instruction_sentence):
        self.add(instruction_sentence)

    def garnish(self, instruction_sentence):
        self.top(instruction_sentence)

    def extract_serving_instructions(self, instruction_sentence):
        doc = self.nlp(instruction_sentence)
        serving_instructions = []

        for token in doc:
            # Check for serving-related keywords
            if token.text.lower() == 'serve' or token.text.lower() == 'top' or token.text.lower() == 'garnish':
                # Extract the serving instruction
                serving_instruction = self.single_instruction(doc, token)
                serving_instructions.append(serving_instruction)

        return serving_instructions

    def single_instruction(self, doc, keyword_token):
        serving_instruction = ''
        serving_keywords = ['with', 'over', 'on', 'alongside', 'beside']

        # Traverse the sentence from the keyword token
        for token in doc[keyword_token.i + 1:]:
            if token.text.lower() in serving_keywords:
                break
            serving_instruction += token.text_with_ws

        serving_instruction = serving_instruction.strip()

        return serving_instruction


if __name__ == "__main__":
    obj = Assemble()
    obj.serve("Serve meal")
    obj.sprinkle("Sprinkle cinnamon over the pancakes")
    obj.garnish("Garnish with basil (to taste) and remaining Parmesan")
    obj.arrange("arrange tomato wedges on it skin-side down")
    obj.drizzle("Drizzle pepper halves with oil, salt, and pepper")
    obj.combine("In a small bowl, combine panko, a drizzle of olive oil, and a pinch of salt.")
