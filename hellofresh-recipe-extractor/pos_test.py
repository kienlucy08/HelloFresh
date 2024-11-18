import pandas as pd
import pos

df = pd.read_csv('recipe_scraping/scraped_pasta_recipes.csv')

all_verbs = []

if __name__ == "__main__":

    for index, row in df.iterrows():
        print(row[1])   # print title of recipe
        steps = row[3]  # isolate the row element defining the cooking instructions

        verbs = pos.extract_verbs(steps)       # get all verbs from the instructions
        all_verbs.append(verbs)
        verbs_fd = pos.verbs_freq_dist(verbs)  # add verbs to a frequency distribution

        v_len = len(verbs)

        print("Verbs: " + str(v_len))
        print(verbs_fd.most_common(v_len))

        print()
