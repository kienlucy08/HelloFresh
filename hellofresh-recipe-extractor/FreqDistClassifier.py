import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier
from nltk.probability import FreqDist
from nltk.tokenize import regexp_tokenize

tagged = {}
tagged1 = []
freqDistsWithTag = []


## manually tags every instruction with its action word
## stores in dictionary
def tagInstructions():
    # Note, the instructions start at 2 in order to match the csv file

    # 2
    tagged1.append([('Wash and dry all produce.', 'Wash'),
                    ('Bring a large pot of salted water to a boil.', 'Boil'),
                    ('Trim woody bottom ends from baby broccoli.', 'Trim'),
                    ('Cut stalks and florets into 1-inch pieces.', 'Cut'),
                    ('Remove sausage from casings.', 'Remove'),
                    ('Once water is boiling, add orecchiette to pot.', 'Add'),
                    ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
                    ('Carefully scoop out and reserve  ¼ cup pasta cooking water, then drain.', 'Scoop'),
                    ('Heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
                    ('Add baby broccoli and 2 tsp water.', 'Add'),
                    ('Cover and steam 3 minutes.', 'Steam'),
                    ('Uncover and increase heat to medium high.', 'Increase'),
                    ('Cook, tossing occasionally, until browned and tender, 3-6 minutes more.', 'Cook'),
                    ('Season with salt and pepper.', 'Season'),
                    ('Remove from pan and set aside.', 'Remove'),
                    ('Heat another drizzle of olive oil in same pan over medium-high heat.', 'Heat'),
                    ('Add sausage, breaking up meat into pieces.', 'Add'),
                    ('Cook until crisp at edges and no longer pink, 4-5 minutes.', 'Cook'),
                    ('Add a pinch of chili flakes (to taste) and cook another 30 seconds.', 'Add'),
                    (
                    'Add orecchiette, baby broccoli, pesto, pasta cooking water, and half the Parmesan to pan.', 'Add'),
                    ('Toss until everything is well-coated and a thick sauce has formed, 1-2 minutes.', 'Toss'),
                    ('Season with salt and pepper.', 'Season'),
                    ('Divide orecchiette mixture between plates.', 'Divide'),
                    ('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])

    # 3
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Preheat oven to 400 degrees or grill to high.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Cut tomatoes into quarters.', 'Cut'),
         ('Mince or grate garlic.', 'Mince'),
         ('Pick leaves from parsley; discard stems.', 'Pick'),
         ('Roughly chop leaves.', 'Chop'),
         ('Cut mozzarella into Â½-inch cubes.', 'Cut'),
         ('Pat steak dry with a paper towel.', 'Pat'),
         ('Once water is boiling, add orzo to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Drain.', 'Drain'),
         ('Heat a drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Season steak all over with herbs de Provence, salt, and pepper.', 'Season'),
         ('Sear in pan and cook until browned, 2-3 minutes per side.', 'Cook'),
         ('Transfer to a baking sheet.', 'Transfer'),
         ('Roast in oven to desired doneness, 7-10 minutes.', 'Roast'),
         ('If grilling, grill seasoned steak to desired doneness, 3-6 minutes per side.',
          'Grill'),
         ('Heat another drizzle of olive oil in same pan over medium heat.', 'Heat'),
         ('Add garlic and cook until fragrant, about 30 seconds.', 'Add'),
         ('Add tomatoes and cook until slightly softened, 1-2 minutes.', 'Add'),
         ('Add orzo, mozzarella, 1 TBSP balsamic vinegar (we sent more), a drizzle of olive oil, '
          'and Â¾ of the parsley to pan.', 'Add'),
         ('Stir to combine.', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Let steak rest a few minutes after removing from oven, then thinly slice against the grain.',
          'Let'),
         ('Divide pasta salad between plates and top with steak.', 'Divide'),
         ('Garnish with remaining parsley and serve.', 'Garnish')])

    # 4
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Trim woody bottom ends from baby broccoli.', 'Trim'),
         ('Cut stalks and florets into 1-inch pieces.', 'Cut'),
         ('Remove sausage from casings.', 'Remove'),
         ('Once water is boiling, add orecchiette to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-12 minutes.',
          'Cook'),
         ('Carefully scoop out and reserve Â½ cup pasta cooking water, then drain.',
          'Scoop'),
         ('Heat a large drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add baby broccoli and 4 tsp water.', 'Add'),
         ('Cover and steam 3 minutes.', 'Steam'),
         ('Uncover and increase heat to medium high.', 'Increase'),
         ('Cook, tossing occasionally, until browned and tender, 3-6 minutes more.',
          'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Heat another large drizzle of olive oil in same pan over medium-high heat.',
          'Heat'),
         ('Add sausage, breaking up meat into pieces.', 'Add'),
         ('Cook, tossing, until crisp at edges and no longer pink, 4-5 minutes.',
          'Cook'),
         ('Add a pinch of chili flakes (to taste) and cook another 30 seconds.',
          'Add'),
         ('Skip the chili flakes if anyone at your table isnâ€™t a fan of spicy heatâ€”you can always '
          'add them at the end.', 'Skip'),
         ('Add orecchiette, baby broccoli, pesto, pasta cooking water, and half the Parmesan to pan.',
          'Add'),
         ('Toss until everything is well-coated and a thick sauce has formed, 1-2 minutes.',
          'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide orecchiette mixture between plates.', 'Divide'),
         ('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])
    # 5
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Cut any large broccoli florets into bite-size pieces.', 'Cut'),
         ('Remove sausage from casings.', 'Remove'),
         ('Once water is boiling, add orecchiette to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-12 minutes.',
          'Cook'),
         ('Carefully scoop out and reserve Â¼ cup pasta cooking water, then drain.',
          'Scoop'),
         ('Heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add broccoli and 2 tsp water.', 'Add'),
         ('Cover and steam 3 minutes.', 'Steam'),
         ('Uncover and increase heat to medium high.', 'Increase'),
         ('Cook, tossing occasionally, until browned and tender, 3-6 minutes more.',
          'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Heat another drizzle of olive oil in same pan over medium-high heat.',
          'Heat'),
         ('Add sausage, breaking up meat into pieces.', 'Add'),
         ('Cook until crisp at edges and no longer pink, 4-5 minutes.', 'Cook'),
         ('Add a pinch of chili flakes (to taste) and cook another 30 seconds.',
          'Add'),
         ('Add orecchiette, broccoli, pesto, pasta cooking water, and half the Parmesan to pan.',
          'Add'),
         ('Toss until everything is well coated and a thick sauce has formed, 1-2 minutes.',
          'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide orecchiette mixture between plates.', 'Divide'),
         ('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])

    # 6
    tagged1.append(
        [('Heat broiler to high.', 'Heat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Core, deseed, and dice bell pepper.', 'Dice'),
         ('Halve, peel, and dice onion.', 'Dice'),
         ('Mince or grate garlic.', 'Mince'),
         ('Cut mozzarella into Â½-inch cubes.', 'Cut'),
         ('Once water is boiling, add penne to pot.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve Â½ cup pasta cooking water (Â¾ cup for 4 servings), then drain.',
          'Reserve'),
         ('Meanwhile, heat a large drizzle of olive oil in a large, preferably ovenproof, pan over medium-high heat.',
          'Heat'),
         ('Add bell pepper and cook, stirring, until just browned, 4-6 minutes.',
          'Cook'),
         ('Stir in onion, garlic, and half the Tuscan Heat Spice (youâ€™ll use the rest later).',
          'Stir'),
         ('Cook, stirring, until onion is softened, 3-5 minutes.', 'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Add marinara sauce, penne, remaining Tuscan Heat Spice, and reserved pasta cooking water to '
          'pan with veggies; stir to combine.', 'Add'),
         ('Let simmer until warmed through, 3-4 minutes.', 'Simmer'),
         ('Stir in half the Parmesan (youâ€™ll use the rest later).', 'Stir'),
         ('Season with plenty of salt and pepper.', 'Season'),
         ('TIP: If your pan is not ovenproof, transfer pasta now to a baking dish.',
          'Transfer'),
         ('In a small bowl, stir together panko, remaining Parmesan, and a drizzle of olive oil.',
          'Stir'),
         ('Top pasta with mozzarella, then panko mixture.', 'Top'),
         ('Transfer pasta to top rack and broil until panko is golden brown, sauce is bubbly, and cheese '
          'has melted, 5-7 minutes. (TIP: Watch carefully to avoid burning.)', 'Transfer'),
         ('Let cool slightly, then divide between plates or bowls.', 'Divide'),
         ('Drizzle with basil oil and serve.', 'Drizzle')])

    # 7
    tagged1.append(
        [('Adjust rack to top position and preheat broiler to 500 degrees).', 'Adjust'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Slice mozzarella into thin rounds.', 'Slice'),
         ('Pat chicken dry with paper towels, then season all over with salt, pepper, and half the '
          'Tuscan Heat Spice (youâ€™ll use the rest later).', 'Season'),
         ('Once water is boiling, add penne to pot.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve Â¼ cup pasta cooking water, then drain.', 'Reserve'),
         ('Meanwhile, heat a large drizzle of oil in a large, high-sided pan over medium-high heat '
          '(use an ovenproof pan if you have one).', 'Heat'),
         ('Add chicken and cook, stirring occasionally, until browned on all sides but not '
          'yet cooked through, 1-2 minutes. (TIP: Donâ€™t overcrowd the panâ€”you may want to work '
          'in batches so the pieces brown evenly.)', 'Cook'),
         ('Add crushed tomatoes, stock concentrates, penne, remaining Tuscan Heat Spice, '
          'and reserved pasta cooking water to pan; stir to combine.', 'Add'),
         ('Simmer until sauce has thickened slightly, 2-3 minutes.', 'Simmer'),
         ('Stir in 1 TBSP butter; season with salt and pepper.', 'Stir'),
         ('In a small bowl, combine panko, a drizzle of olive oil, and a pinch of salt.',
          'Combine'),
         ('Evenly top pasta mixture with mozzarella and panko mixture.', 'Top'),
         ('Season all over with pepper.', 'Season'),
         ('Broil (or bake) pasta until panko is golden brown and sauce is bubbly, 3-5 minutes.'
          ' (TIP: Keep an eye on dish while broiling.)', 'Broil'),
         ('Cool slightly, then divide between plates and serve.', 'Divide')])

    # 8

    tagged1.append(
        [('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Adjust broiler rack so that it is in position closest to flame and heat broiler to high.', 'Adjust'),
         ('Once water is boiling, add cavatappi to pot.', 'Add'),
         ('Cook, stirring occasionally, until just al dente, about 8 minutes.', 'Cook'),
         ('Drain.', 'Drain'),
         ('Meanwhile, pat chicken dry with paper towel.', 'Pat'),
         ('Season generously with salt and pepper.', 'Season'),
         ('Heat 2 TBSP olive oil in a large pan over medium-high heat (use an ovenproof pan if you have one).', 'Heat'),
         ('Add chicken and cook until browned and no longer pink in center, 5-6 minutes per side.', 'Cook'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Wash and dry all produce.', 'Wash'),
         ('Place broccoli and 1 TBSP water in a medium, microwave-safe bowl.', 'Place'),
         ('Cover with plastic wrap and poke a few holes in wrap.', 'Cover'),
         ('Microwave on high until tender, about 3 minutes.', 'Microwave'),
         ('Melt 2 TBSP butter in pan used for chicken over medium-high heat.', 'Melt'),
         ('Add flour and ranch spice.', 'Add'),
         ('Stir constantly until pasty and fragrant, 30 seconds to 1 minute.', 'Stir'),
         ('Slowly whisk in milk, scraping up any browned bits on bottom.', 'Whisk'),
         ('Bring to a simmer, then reduce heat to medium.', 'Bring'),
         ('Let bubble until sauce thickens slightly, about 3 minutes.', 'Let'),
         ('Remove pan from heat.', 'Remove'),
         ('Add cream cheese, cheddar, and Â½ cup mozzarella (1 pack) to pan and whisk until smooth '
          '(weâ€™ll use the rest of the mozzarella later).', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Thinly slice chicken.', 'Slice'),
         ('Drain broccoli.', 'Drain'),
         ('Stir chicken, broccoli, and cavatappi into pan.', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Place 1 TBSP butter in a small, microwave-safe bowl.', 'Place'),
         ('Microwave on high until it melts, about 45 seconds.', 'Microwave'),
         ('Add Â¼ cup panko (we sent more) and remaining mozzarella to bowl with butter and stir to combine.', 'Add'),
         ('Scatter over pasta in pan or dish.', 'Scatter'),
         ('Place pan under broiler and broil until cheese melts and panko is golden brown, about 3 minutes.', 'Broil'),
         ('Divide pasta between plates and serve.', 'Divide')])

    # 9

    tagged1.append(
        [("Wash and dry all produce.", "Wash, dry"), ("Bring a large pot of salted water to a boil.", "Boil"),
         ("Trim woody bottom ends from baby broccoli, then cut into 1-inch pieces.", "Trim, cut"),
         ("Roughly chop garlic.", "Chop"), ("Pick oregano leaves from stems; discard stems.", "Pick, discard"),
         ("Zest lemon until you have 1 tsp zest, then cut into halves.", "Zest, cut"),
         ("Remove sausage from casing.", "Remove"), ("Once water is boiling, add gemelli to pot.", "Add"),
         ("Cook, stirring occasionally, until al dente, 9-12 minutes total.", "Cook, stir"),
         ("About 4 minutes before gemelli is done, add baby broccoli to pot.", "Add"),
         ("(TIP: Gemelli should be chewy on the outside but dry in the center at this point.)", ""),
         ("Cook until baby broccoli is tender and gemelli is done, 3-4 minutes, then drain.", "Cook, drain"),
         ("While pasta cooks, place almonds, oregano, and garlic on your cutting board in a pile and finely "
          "chop until the mixture has a pesto-like texture.", "Place, chop"),
         ("TIP: It’s OK if the almonds are somewhat coarse.", ""),
         ("Heat a drizzle of olive oil in a large pan over medium-high heat.", "Heat"),
         ("Add sausage, breaking up meat into pieces.", "Add, break, cook"),
         ("Cook, tossing occasionally, until browned and cooked through, 4-5 minutes.", "Cook, toss"),
         ("Remove from pan and set aside.", "Remove"),
         ("Reduce heat under pan to medium low.", "Reduce"),
         ("(TIP: Add another drizzle of olive oil if there is no grease left.)", ""),
         ("Add gremolata.", "Add"),
         ("Cook, tossing, until almonds begin to turn golden brown, 3-4 minutes.", "Cook, toss"),
         ("Season with salt and pepper.", "Season"),
         ("Add sausage, baby broccoli, gemelli, lemon zest, and half the Parmesan to pan, tossing to combine.",
          "Add, toss, combine"),
         ("Season with salt and pepper.", "Season"),
         ("Stir in a drizzle of olive oil and a squeeze or two of lemon juice (to taste).", "Stir"),
         ("Divide between bowls, sprinkle with remaining Parmesan, and serve.", "Divide, sprinkle, serve")])

    # 10

    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Trim woody bottom ends from baby broccoli.', 'Trim'),
         ('Cut stalks and florets into 1-inch pieces.', 'Cut'),
         ('Remove sausage from casings.', 'Remove'),
         ('Once water is boiling, add orecchiette to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.',
          'Cook'),
         ('Carefully scoop out and reserve Â¼ cup pasta cooking water, then drain.',
          'Scoop'),
         ('Heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add baby broccoli and 2 tsp water.', 'Add'),
         ('Cover and steam 3 minutes.', 'Steam'),
         ('Uncover and increase heat to medium high.', 'Increase'),
         ('Cook, tossing occasionally, until browned and tender, 3-6 minutes more.',
          'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Heat another drizzle of olive oil in same pan over medium-high heat.',
          'Heat'),
         ('Add sausage, breaking up meat into pieces.', 'Add'),
         ('Cook until crisp at edges and no longer pink, 4-5 minutes.', 'Cook'),
         ('Add a pinch of chili flakes (to taste) and cook another 30 seconds.',
          'Add'),
         ('Add orecchiette, baby broccoli, pesto, pasta cooking water, and half the Parmesan to pan.',
          'Add'),
         ('Toss until everything is well-coated and a thick sauce has formed, 1-2 minutes.',
          'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide orecchiette mixture between plates.', 'Divide'),
         ('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])

    # 11
    tagged1.append([('Wash and dry all produce.', 'Wash'),
                    ('Bring a large pot of salted water to a boil.', 'Boil'),
                    ('Trim woody bottom ends from baby broccoli.', 'Trim'),
                    ('Cut stalks and florets into 1-inch pieces.', 'Cut'),
                    ('Remove sausage from casings.', 'Remove'),
                    ('Once water is boiling, add orecchiette to pot.', 'Add'),
                    ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
                    ('Carefully scoop out and reserve Â¼ cup pasta cooking water, then drain.', 'Scoop'),
                    ('Heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
                    ('Add baby broccoli and 2 tsp water.', 'Add'), ('Cover and steam 3 minutes.', 'Steam'),
                    ('Uncover and increase heat to medium high.', 'Increase'),
                    ('Cook, tossing occasionally, until browned and tender, 3-6 minutes more.', 'Cook'),
                    ('Season with salt and pepper.', 'Season'), ('Remove from pan and set aside.', 'Remove'),
                    ('Heat another drizzle of olive oil in same pan over medium-high heat.', 'Heat'),
                    ('Add sausage, breaking up meat into pieces.', 'Add'),
                    ('Cook until crisp at edges and no longer pink, 4-5 minutes.', 'Cook'),
                    ('Add a pinch of chili flakes (to taste) and cook another 30 seconds.', 'Add'), (
                        'Add orecchiette, baby broccoli, pesto, pasta cooking water, and half the Parmesan to pan.',
                        'Add'),
                    ('Toss until everything is well-coated and a thick sauce has formed, 1-2 minutes.', 'Toss'),
                    ('Season with salt and pepper.', 'Season'),
                    ('Divide orecchiette mixture between plates.', 'Divide'),
                    ('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])

    # 13
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil (TIP: Keep it covered to speed things up).', 'Boil'),
         ('Heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Halve, peel, and dice onion.', 'Dice'),
         ('Trim woody bottom ends from asparagus.', 'Trim'),
         ('Cut stalks into 1-inch pieces.', 'Cut'),
         ('Add onion and half the pancetta to pan once hot (use remaining pancetta as you like).', 'Add'),
         ('Season with salt, pepper, and Italian seasoning.', 'Season'),
         ('Cook, tossing, until onion is soft and pancetta is crisped, about 5 minutes.', 'Cook'),
         ('Place tomatoes in a medium bowl and break up with your hands into small pieces.', 'Place'),
         ('Once water is boiling, add tagliatelle to pot.', 'Add'),
         ('Cook, stirring occasionally, until chewy on the outside but still firm in the center, 6-7 minutes.', 'Cook'),
         ('Add asparagus to pot and cook until bright green and just tender, 3-5 minutes more '
          '(the tagliatelle should be al dente at this point).', 'Add'),
         ('Carefully scoop out and reserve 1 cup cooking water, then drain.', 'Scoop'),
         ('While tagliatelle cooks, heat another drizzle of olive oil in pan from pancetta over medium-high heat.',
          'Heat'),
         ('Once hot, add garlic and cook until fragrant, 30 seconds.', 'Add'),
         ('Add crushed tomatoes and cook until sauce is slightly reduced, 2-3 minutes.', 'Add'),
         ('Add reserved pasta cooking water, ½ tsp sugar, and a pinch of salt and pepper to pan with sauce.', 'Add'),
         ('Reduce heat to medium and let simmer until sauce is slightly thickened, 5-7 minutes.', 'Reduce'),
         ('Add tagliatelle, asparagus, and remaining pancetta to pan with sauce and toss to coat.', 'Add'),
         ('Divide among plates and sprinkle with Parmesan and basil, if desired.', 'Divide')])

    # 14
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Take out creamcheese from refrigerator and set aside.', 'Take'),
         ('Cut half the broccoli into small pieces (use the rest as you like).', 'Cut'),
         ('Mince or grate garlic.', 'Mince'),
         ('Zest lemon until you have 1 tsp zest, then cut into halves.', 'Zest'),
         ('Squeeze juice into a small bowl.', 'Squeeze'),
         ('Pick basil leaves from stems; discard stems.', 'Pick'),
         ('Roughly chop leaves.', 'Chop'),
         ('Pat chicken dry with a paper towel, then cut into 1Â½-inch pieces.', 'Pat'),
         ('Heat a drizzle of olive oil in a large pot over medium-high heat.', 'Heat'),
         ('Season chicken all over with salt and pepper.', 'Season'),
         ('Add to pot along with garlic.', 'Add'),
         ('Cook, tossing occasionally, until browned all over, 3-5 minutes.', 'Cook'),
         ('Remove from heat and transfer chicken to a large bowl.', 'Remove'),
         ('Add lemon juice to empty pot, scraping up any brown bits from bottom.', 'Add'),
         ('Pour over chicken in bowl and set aside.', 'Pour'),
         ('Add stock concentrates, 3 cups water, and gemelli to pot and give it a stir.', 'Add'),
         ('Bring to a boil over high heat, then lower heat to medium and reduce to a simmer.', 'Bring'),
         ('Cook, stirring frequently, for 8 minutes.', 'Cook'),
         ('Stir chicken and juices from bowl into pot.', 'Stir'),
         ('Add broccoli and continue to cook until pasta is al dente and broccoli is tender, 4-5 minutes more.', 'Add'),
         ('Reserve about 1 cup pasta cooking water, then drain pasta and broccoli.', 'Reserve'),
         ('Return pasta and broccoli to pot, along with cream cheese and ½ cup reserved pasta cooking'
          ' water.', 'Return'),
         ('Toss until cheese is melted and a smooth sauce has formed, 1-2 minutes. '
          '(Add more reserved pasta cooking water as needed if sauce is dry.)', 'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Serve chicken and pasta topped with basil and lemon zest.', 'Serve')])

    # 15
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Cut any large broccoli florets into bite-sized pieces.', 'Cut'),
         ('Remove sausage from casings.', 'Remove'),
         ('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Cut any large broccoli florets into bite-sized pieces.', 'Cut'),
         ('Remove sausage from casings.', 'Remove'),
         ('Heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add broccoli and 2 tsp water.', 'Add'),
         ('Cover and steam 3 minutes.', 'Steam'),
         ('Uncover and increase heat to medium high.', 'Increase'),
         ('Cook, tossing occasionally, until browned and tender, 3-6 minutes more.',
          'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Heat another drizzle of olive oil in same pan over medium-high heat.',
          'Heat'),
         ('Add sausage, breaking up into pieces with a spatula or wooden spoon.', 'Add'),
         ('Cook until crisp at edges and no longer pink, 4-5 minutes.', 'Cook'),
         ('Add a pinch of chili flakes (to taste) and cook another 30 seconds.',
          'Add'),
         ('Add orecchiette, broccoli, pesto, pasta cooking water, and half the Parmesan to pan.',
          'Add'),
         ('Toss until everything is well-coated and a thick sauce has formed, 1-2 minutes.',
          'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide orecchiette mixture between plates.', 'Divide'),
         ('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])

    # 16

    tagged1.append([
        ('Wash and dry all produce.', 'Wash'),
        ('Bring a large pot of salted water to a boil.', 'Boil'),
        ('Dice one tomato.', 'Dice'),
        ('Zest 1 tsp zest from lemon, then cut into quarters.', 'Zest'),
        ('Pat chicken dry with a paper towel.', 'Pat'),
        ('Season with salt, pepper, and Tuscan heat spice.', 'Season'),
        ('Once water is boiling, add cavatappi to pot.', 'Add'),
        ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
        ('Reserve Â¼ cup cooking water, then drain.', 'Reserve'),
        ('Meanwhile, heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
        ('Add chicken and cook until no longer pink in center, 4-5 minutes per side.', 'Cook'),
        ('(TIP: Work in batches if you canâ€™t fit all the chicken comfortably.)', 'Work'),
        ('Remove from pan and set aside to rest.', 'Remove'),
        ('Cut chicken into 1-inch pieces once cool enough to handle.', 'Cut'),
        ('Heat another drizzle of olive oil in same pan over medium heat.', 'Heat'),
        ('Add diced tomato.', 'Add'),
        ('Cook, tossing, until slightly softened, 1-2 minutes.', 'Cook'),
        ('Season with salt and pepper.', 'Season'),
        ('Add cavatappi, 1 TBSP butter, and Â¾ of the pesto and toss to combine...', 'Add'),
        ('Reserve Â¼ cup cooking water, then drain.', 'Reserve'),
        ('Divide into bowls and garnish with lemon zest, remaining pesto, and Parmesan (to taste).', 'Divide')])

    # 17
    tagged1.append(
        [('Bring a medium pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Trim and thinly slice scallions, separating whites from greens.', 'Trim'),
         ('Trim and thinly slice mushrooms into Â¼-inch-thick pieces.', 'Trim'),
         ('Heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add mushrooms; season with salt and pepper.', 'Add'),
         ('Cook, stirring occasionally, until browned and slightly crispy, 5-7 minutes.', 'Cook'),
         ('Turn off heat; transfer to a paper-towellined plate.', 'Transfer'),
         ('Rinse and wipe out pan.', 'Rinse'),
         ('Once water is boiling, add gemelli to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve 1 cup pasta cooking water, then drain.', 'Reserve'),
         ('Meanwhile, melt 2 TBSP plain butter (4 TBSP for 4 servings) in pan used for mushrooms '
          'over medium-high heat.', 'Melt'),
         ('Add scallion whites and cook until just softened, 30 seconds to 1 minute.', 'Cook'),
         ('Add flour and cook, stirring, until lightly browned, 1-2 minutes.', 'Cook'),
         ('Whisk in milk and â…“ cup pasta cooking water (Â½ cup for 4), making sure...', 'Whisk'),
         ('Add Parmesan and stir until melted, 1-2 minutes.', 'Add'),
         ('Add gemelli, mushrooms, and any remaining scallion greens to pan with sauce. Toss to '
          'coat and add more reserved pasta cooking water as needed to thin sauce.', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide between plates and serve, topped with extra Parmesan if desired.', 'Divide')])

    # 18
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Adjust rack to upper position and preheat oven to 425 degrees.', 'Adjust, Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Slice zucchini into Â¼-inch-thick rounds.', 'Slice'),
         ('Cut tomato into Â½-inch-thick wedges.', 'Cut'),
         ('Toss zucchini and tomato with 1 TBSP olive oil and half the Italian seasoning on a baking sheet.', 'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Roast zucchini and tomato in oven until just shy of tender, about 10 minutes.', 'Roast'),
         ('Once water is boiling, add half the orzo from package to pot (use the rest as you like).', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Drain, then return to pot.', 'Drain, Return'),
         ('With your hand on top of one chicken breast, cut Â¾ of the way through middle, '
          'parallel to cutting board, stopping before you slice through completely.', 'Cut'),
         ('Repeat with other chicken breast.', 'Repeat'),
         ('Open each up and season all over with salt, pepper, and remaining Italian seasoning.', 'Open, Season'),
         ('Heat a drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add chicken and cook until no longer pink in center, 3-4...', 'Add, Cook'),
         ('Flip and cook until browned and cooked through, 2-3 minutes more.', 'Flip, Cook'),
         ('Divide orzo between plates.', 'Divide'),
         ('Top with chicken and roasted vegetables.', 'Top')])

    # 19
    tagged1.append([('Wash and dry all produce.', 'Wash'),
                    ('Preheat oven to 400 degrees or grill to high.', 'Preheat'),
                    ('Bring a large pot of salted water to a boil.', 'Boil'),
                    ('Cut tomatoes into quarters.', 'Cut'),
                    ('Mince or grate garlic.', 'Mince'),
                    ('Pick leaves from parsley; discard stems.', 'Pick'),
                    ('Roughly chop leaves.', 'Chop'),
                    ('Cut mozzarella into Â½-inch cubes.', 'Cut'),
                    ('Pat steak dry with a paper towel.', 'Pat'),
                    ('Once water is boiling, add orzo to pot.', 'Add'),
                    ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
                    ('Drain.', 'Drain'),
                    ('Heat a drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
                    ('Season steak all over with herbs de Provence, salt, and pepper.', 'Season'),
                    ('Sear in pan and cook until browned, 2-3 minutes per side.', 'Sear'),
                    ('Transfer to a baking sheet.', 'Transfer'),
                    ('Roast in oven to desired doneness, 7-10 minutes.', 'Roast'),
                    ('TIP: If grilling, grill seasoned steak to desired doneness, 3-6 minutes per side.', 'Grill'),
                    ('Heat another drizzle of olive oil in same pan over medium heat.', 'Heat'),
                    ('Add garlic and cook until fragrant, about 30 seconds.', 'Add'),
                    ('Add tomatoes and cook until slightly softened, 1-2 minutes.', 'Add'),
                    ('Season with salt and pepper.', 'Season'),
                    ('Stir in orzo, mozzarella, and parsley.', 'Stir'),
                    ('Divide among plates and serve.', 'Divide')])

    # 20
    tagged1.append([('Wash and dry all produce.', 'Wash'),
                    ('Bring a large pot of salted water to a boil.', 'Boil'),
                    ('Trim woody bottom ends from baby broccoli.', 'Trim'),
                    ('Cut stalks and florets into 1-inch pieces.', 'Cut'),
                    ('Remove sausage from casings.', 'Remove'),
                    ('Once water is boiling, add orecchiette to pot.', 'Add'),
                    ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
                    ('Carefully scoop out and reserve  ¼ cup pasta cooking water, then drain.', 'Scoop'),
                    ('Heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
                    ('Add baby broccoli and 2 tsp water.', 'Add'),
                    ('Cover and steam 3 minutes.', 'Steam'),
                    ('Uncover and increase heat to medium high.', 'Increase'),
                    ('Cook, tossing occasionally, until browned and tender, 3-6 minutes more.', 'Cook'),
                    ('Season with salt and pepper.', 'Season'),
                    ('Remove from pan and set aside.', 'Remove'),
                    ('Heat another drizzle of olive oil in same pan over medium-high heat.', 'Heat'),
                    ('Add sausage, breaking up meat into pieces.', 'Add'),
                    ('Cook until crisp at edges and no longer pink, 4-5 minutes.', 'Cook'),
                    ('Add a pinch of chili flakes (to taste) and cook another 30 seconds.', 'Add'),
                    (
                    'Add orecchiette, baby broccoli, pesto, pasta cooking water, and half the Parmesan to pan.', 'Add'),
                    ('Toss until everything is well-coated and a thick sauce has formed, 1-2 minutes.', 'Toss'),
                    ('Season with salt and pepper.', 'Season'),
                    ('Divide orecchiette mixture between plates.', 'Divide'),
                    ('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])

    # 21
    tagged1.append([
        ('Wash and dry all produce.', 'Wash'),
        ('Bring a large pot of salted water to a boil.', 'Boil'),
        ('Cut any large broccoli florets into bite-size pieces.', 'Cut'),
        ('Remove sausage from casings.', 'Remove'),
        ('Once water is boiling, add orecchiette to pot.', 'Add'),
        ('Cook, stirring occasionally, until al dente, 9-12 minutes.', 'Cook'),
        ('Carefully scoop out and reserve  ¼ cup pasta cooking water, then drain.', 'Scoop'),
        ('Heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
        ('Add broccoli and 2 tsp water.', 'Add'),
        ('Cover and steam 3 minutes.', 'Steam'),
        ('Uncover and increase heat to medium high.', 'Increase'),
        ('Cook, tossing occasionally, until browned and tender, 3-6 minutes more.', 'Cook'),
        ('Season with salt and pepper.', 'Season'),
        ('Remove from pan and set aside.', 'Remove'),
        ('Heat another drizzle of olive oil in same pan over medium-high heat.', 'Heat'),
        ('Add sausage, breaking up meat into pieces.', 'Add'),
        ('Cook until crisp at edges and no longer pink, 4-5 minutes.', 'Cook'),
        ('Add a pinch of chili flakes (to taste) and cook another 30 seconds.', 'Add'),
        ('Add orecchiette, broccoli, pesto, pasta cooking water, and half the Parmesan to pan.', 'Add'),
        ('Toss until everything is well-coated and a thick sauce has formed, 1-2 minutes.', 'Toss'),
        ('Season with salt and pepper.', 'Season'),
        ('Divide orecchiette mixture between plates.', 'Divide'),
        ('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])
    # 22
    tagged1.append(
        [('Heat broiler to high.', 'Heat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Core, deseed, and dice bell pepper.', 'Core'),
         ('Halve, peel, and dice onion.', 'Peel'),
         ('Mince or grate garlic.', 'Mince'),
         ('Cut mozzarella into Â½-inch cubes.', 'Cut'),
         ('Once water is boiling, add penne to pot.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve Â½ cup pasta cooking water (Â¾ cup for 4 servings), then drain.', 'Reserve'),
         ('Meanwhile, heat a large drizzle of olive oil in a large, preferably ovenproof, pan over medium-high heat.',
          'Heat'),
         ('Add bell pepper and cook, stirring, until just browned, 4-6 minutes.', 'Add'),
         ('Stir in onion, garlic, and half the Tuscan Heat Spice (youâ€™ll use the rest later).', 'Stir'),
         ('Cook, stirring, until onion is softened, 3-5 minutes.', 'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Add marinara sauce, penne, remaining Tuscan Heat Spice, and reserved pasta cooking '
          'water to pan with veggies; stir to combine.', 'Add'),
         ('Let simmer until warmed through, 3-4 minutes.', 'Simmer'),
         ('Add half the mozzarella; stir to combine.', 'Add'),
         ('Sprinkle remaining mozzarella over the top.', 'Sprinkle'),
         ('Transfer pan to broiler and broil until cheese is bubbly and golden brown, 1-2 minutes.', 'Transfer')])

    # 23
    tagged1.append(
        [('Adjust rack to top position and preheat broiler to 500 degrees).', 'Adjust'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Slice mozzarella into thin rounds.', 'Slice'),
         ('Pat chicken dry with paper towels, then season all over with salt, pepper, and'
          ' half the Tuscan Heat Spice (you’ll use the rest later).', 'Pat'),
         ('Once water is boiling, add penne to pot.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve ¼ cup pasta cooking water, then drain.', 'Reserve'),
         ('Meanwhile, heat a large drizzle of oil in a large, high-sided pan over medium-high '
          'heat (use an ovenproof pan if you have one).', 'Heat'),
         ('Add chicken and cook, stirring occasionally, until browned on all sides but not yet'
          ' cooked through, 1-2 minutes.', 'Cook'),
         ('Add crushed tomatoes, stock concentrates, penne, remaining Tuscan Heat Spice, and reserved '
          'pasta cooking water to pan with chicken.', 'Add'),
         ('Stir to combine and bring to a simmer.', 'Stir'),
         ('Simmer until chicken is cooked through and sauce has thickened slightly, 8-10 minutes.', 'Simmer'),
         ('Season with salt and pepper.', 'Season'),
         ('Tear basil leaves into small pieces.', 'Tear'),
         ('Once chicken mixture is done, top with mozzarella rounds.', 'Top'),
         ('Broil until cheese is melted and bubbly, 1-2 minutes.', 'Broil'),
         ('Serve penne and chicken topped with basil.', 'Serve')])
    # 24
    tagged1.append(
        [('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Adjust broiler rack so that it is in position closest to flame and heat broiler to high.', 'Adjust'),
         ('Once water is boiling, add cavatappi to pot.', 'Add'),
         ('Cook, stirring occasionally, until just al dente, about 8 minutes.', 'Cook'),
         ('Drain.', 'Drain'),
         ('Meanwhile, pat chicken dry with paper towel.', 'Pat'),
         ('Season generously with salt and pepper.', 'Season'),
         ('Heat 2 TBSP olive oil in a large pan over medium-high heat (use an ovenproof pan if you have one).', 'Heat'),
         ('Add chicken and cook until browned and no longer pink in center, 5-6 minutes per side.', 'Cook'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Wash and dry all produce.', 'Wash'),
         ('Place broccoli and 1 TBSP water in a medium, microwave-safe bowl.', 'Place'),
         ('Cover with plastic wrap and poke a few holes in wrap.', 'Cover'),
         ('Microwave on high until tender, about 3 minutes.', 'Microwave'),
         ('Melt 2 TBSP butter in pan used for chicken over medium-high heat.', 'Melt'),
         ('Add flour and ranch spice.', 'Add'),
         ('Stir constantly until', 'Stir'),
         ('Add 1 1/2 cups milk and stir until mixture comes to a simmer and thickens, 2-3 minutes.', 'Add'),
         ('Stir in cheddar and half the Parmesan until melted and smooth, 1-2 minutes.', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Add pasta to pot with boiling water and cook until al dente, 2-3 minutes.', 'Add'),
         ('Reserve 1/2 cup pasta cooking water, then drain pasta and broccoli.', 'Reserve'),
         ('Add pasta and broccoli to pan with sauce and toss to coat.', 'Add'),
         ('If mixture is too thick, add reserved pasta water, 1 TBSP at a time, until desired consistency is reached.',
          'Add'),
         ('Divide among plates and sprinkle with remaining Parmesan.', 'Divide')])
    # 25
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Trim woody bottom ends from baby broccoli.', 'Trim'),
         ('Cut into 1-inch pieces.', 'Cut'),
         ('Roughly chop garlic.', 'Chop'),
         ('Pick oregano leaves from stems; discard stems.', 'Pick'),
         ('Zest lemon until you have 1 tsp zest, then cut into halves.', 'Zest'),
         ('Remove sausage from casing.', 'Remove'),
         ('Once water is boiling, add gemelli to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-12 minutes total.', 'Cook'),
         ('About 4 minutes before gemelli is done, add baby broccoli to pot.', 'Add'),
         ('(TIP: Gemelli should be chewy on the outside but dry in the center at this point.)',
          'Tip'),
         ('Cook until baby broccoli is tender and gemelli is done, 3-4 minutes, then drain.',
          'Cook'),
         ('While pasta cooks, place almonds, oregano, and garlic on your cutting board in a pile '
          'and finely chop until the mixture has a pesto-like texture.', 'Chop'),
         ('TIP: It\'s OK if the almonds are somewhat coarse.', 'Tip')])

    # 26
    tagged1.append([('Wash and dry all produce.', 'Wash'),
                    ('Bring a large pot of salted water to a boil.', 'Boil'),
                    ('Trim woody bottom ends from baby broccoli.', 'Trim'),
                    ('Cut stalks and florets into 1-inch pieces.', 'Cut'),
                    ('Remove sausage from casings.', 'Remove'),
                    ('Once water is boiling, add orecchiette to pot.', 'Add'),
                    ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
                    ('Carefully scoop out and reserve  ¼ cup pasta cooking water, then drain.', 'Scoop'),
                    ('Heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
                    ('Add baby broccoli and 2 tsp water.', 'Add'),
                    ('Cover and steam 3 minutes.', 'Steam'),
                    ('Uncover and increase heat to medium high.', 'Increase'),
                    ('Cook, tossing occasionally, until browned and tender, 3-6 minutes more.', 'Cook'),
                    ('Season with salt and pepper.', 'Season'),
                    ('Remove from pan and set aside.', 'Remove'),
                    ('Heat another drizzle of olive oil in same pan over medium-high heat.', 'Heat'),
                    ('Add sausage, breaking up meat into pieces.', 'Add'),
                    ('Cook until crisp at edges and no longer pink, 4-5 minutes.', 'Cook'),
                    ('Add a pinch of chili flakes (to taste) and cook another 30 seconds.', 'Add'),
                    (
                    'Add orecchiette, baby broccoli, pesto, pasta cooking water, and half the Parmesan to pan.', 'Add'),
                    ('Toss until everything is well-coated and a thick sauce has formed, 1-2 minutes.', 'Toss'),
                    ('Season with salt and pepper.', 'Season'),
                    ('Divide orecchiette mixture between plates.', 'Divide'),
                    ('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])

    # 27
    tagged1.append(
        [('Bring a medium pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Pick basil leaves from stems and discard stems;', 'Pick'),
         ('reserve a few leaves for garnish and mince remaining.', 'Reserve'),
         ('Zest and quarter lemon.', 'Zest'),
         ('In a large bowl, whisk together 2 TBSP olive oil (4 TBSP for 4 servings),'
          ' minced basil, lemon zest, juice from half the lemon, salt (we used Â½ tsp; use 1 tsp for 4), '
          'and pepper.', 'Whisk'),
         ('Set aside.', 'Set'),
         ('Once water is boiling, add pasta to pot.', 'Add'),
         ('Cook until al dente, 13-15 minutes.', 'Cook'),
         ('Drain.', 'Drain'),
         ('Meanwhile, pat chicken dry with paper towels.', 'Pat'),
         ('Heat a drizzle of oil in a large pan over medium-high heat.', 'Heat'),
         ('Add chicken and season with a few large pinches of salt and pepper.', 'Add'),
         ('Cook, stirring occasionally, until browned all over, 2-3 minutes.', 'Cook'),
         ('Sprinkle with Italian Seasoning.', 'Sprinkle'),
         ('Continue cooking until chicken is cooked through, 2-3 minutes more.', 'Cook'),
         ('Turn off heat.', 'Turn off'),
         ('Once cooled, cut into 1-inch pieces.', 'Cut'),
         ('Halve, core, and thinly slice onion.', 'Slice'),
         ('Halve, seed, and thinly slice red bell pepper.', 'Slice'),
         ('In a large bowl, whisk together mayonnaise, apple cider vinegar, sugar, and a pinch of salt and pepper.',
          'Whisk'),
         ('Add cooked pasta, chicken, onion, and red bell pepper to bowl with dressing.', 'Add'),
         ('Toss to coat.', 'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Chop reserved basil.', 'Chop'),
         ('Divide pasta salad between plates.', 'Divide'),
         ('Garnish with chopped basil leaves.', 'Garnish')])
    # 28
    tagged1.append(
        [('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Wash and dry produce.', 'Wash'),
         ('Finely dice tomato.', 'Dice'),
         ('Peel and thinly slice garlic.', 'Slice'),
         ('Pick parsley leaves from stems; roughly chop leaves.', 'Pick'),
         ('Pat chicken* dry with paper towels; season all over with half the Italian Seasoning '
          '(all for 4 servings), salt (we used 1/4 tsp; 1/2 tsp for 4), and pepper.', 'Pat'),
         ('Heat a drizzle of oil in a large pan over medium-high heat.', 'Heat'),
         ('Add chicken and cook until browned and cooked through, 3-5 minutes per side.', 'Cook'),
         ('TIP: If chicken starts to brown too quickly, lower heat to medium and cover pan '
          'with lid after flipping chicken.', 'Lower'),
         ('Transfer to a cutting board and tent with foil to keep warm.', 'Transfer'),
         ('Wipe out pan.', 'Wipe'),
         ('Once water is boiling, add spaghetti to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve 1/2 cup pasta cooking water (1 cup for 4 servings), then drain pasta.', 'Reserve'),
         ('Heat a large drizzle of olive oil in pan used for chicken over medium-low.', 'Heat'),
         ('Add tomato, garlic, and chili flakes to taste (we used 1/2 tsp; add a pinch more if you like '
          'things spicy), and cook, stirring occasionally, until softened and fragrant, 2-3 minutes.', 'Add'),
         ('Stir in cream sauce base and 1/4 cup reserved pasta cooking water (1/2 cup for 4 servings).', 'Stir'),
         ('Bring to a simmer, then remove from heat.', 'Bring'),
         ('Taste and season with salt and pepper.', 'Season'),
         ('Stir drained spaghetti, parsley, and 1/2 TBSP butter (1 TBSP for 4 servings) into pan with sauce.', 'Stir'),
         ('Taste and season with salt and pepper if desired.', 'Season'),
         ('TIP: If needed, stir in more reserved cooking water a splash at a time until pasta is '
          'coated in a creamy sauce.', 'Stir'),
         ('Thinly slice chicken crosswise.', 'Slice'),
         ('Divide pasta between bowls; top with chicken and serve.', 'Divide')])

    # 29
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Keep it covered to speed things up.', 'Cover'),
         ('Heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Halve, peel, and dice onion.', 'Dice'),
         ('Trim woody bottom ends from asparagus.', 'Trim'),
         ('Cut stalks into 1-inch pieces.', 'Cut'),
         ('Add onion and half the pancetta to pan once hot (use remaining pancetta as you like).', 'Add'),
         ('Season with salt, pepper, and Italian seasoning.', 'Season'),
         ('Cook, tossing, until onion is soft and pancetta is crisped, about 5 minutes.', 'Cook'),
         ('Place tomatoes in a medium bowl and break up with your hands into small pieces.', 'Break up'),
         ('Once water is boiling, add tagliatelle to pot.', 'Add'),
         ('Cook, stirring occasionally, until chewy on the outside but still firm in the center, 6-7 minutes.', 'Cook'),
         ('Add asparagus to pot and cook until bright green and just tender, 3-5 minutes more.',
          'Add'),
         ('Drain the pasta and reserve ½ cup pasta water.', 'Drain'),
         ('Return the pasta to the pot.', 'Return'),
         ('Add tomatoes, remaining pancetta, and ¼ cup reserved pasta water to the pan.', 'Add'),
         ('Cook until sauce has thickened slightly, 1-2 minutes.', 'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide pasta between plates.', 'Divide'),
         ('Top with breadcrumbs and additional Parmesan, if desired.', 'Top')])

    # 30
    tagged1.append([('Wash and dry all produce.', 'Wash')])
    tagged1.append([('Take out creamcheese from refrigerator and set aside.', 'Take out')])
    tagged1.append([('Cut half the broccoli into small pieces (use the rest as you like).', 'Cut')])
    tagged1.append([('Mince or grate garlic.', 'Mince')])
    tagged1.append([('Zest lemon until you have 1 tsp zest, then cut into halves.', 'Zest')])
    tagged1.append([('Squeeze juice into a small bowl.', 'Squeeze')])
    tagged1.append([('Pick basil leaves from stems; discard stems.', 'Pick')])
    tagged1.append([('Roughly chop leaves.', 'Chop')])

    tagged1.append([('Pat chicken dry with a paper towel, then cut into 1½-inch pieces.', 'Pat')])
    tagged1.append([('Heat a drizzle of olive oil in a large pot over medium-high heat.', 'Heat')])
    tagged1.append([('Season chicken all over with salt and pepper.', 'Season')])
    tagged1.append([('Add to pot along with garlic.', 'Add')])
    tagged1.append([('Cook, tossing occasionally, until browned all over, 3-5 minutes.', 'Cook')])
    tagged1.append([('Remove from heat and transfer chicken to a large bowl.', 'Remove')])

    tagged1.append([('Add lemon juice to empty pot, scraping up any brown bits from bottom.', 'Add')])
    tagged1.append([('Pour over chicken in bowl and set aside.', 'Pour')])
    tagged1.append([('Add stock concentrates, 3 cups water, and gemelli to pot and give it a stir.', 'Add')])
    tagged1.append([('Bring to a boil over high heat, then lower heat to medium and reduce to a simmer.', 'Bring')])
    tagged1.append([('Cook, stirring frequently, for 8 minutes.', 'Cook')])

    tagged1.append([('Stir chicken and juices from bowl into pot with pasta, along with broccoli '
                    'and half the peas (use the rest as you like).', 'Stir')])
    tagged1.append([(
        'Cook until chicken is no longer pink in center, broccoli is just tender, and gemelli is al dente, 4-5 minutes.',
        'Cook')])

    tagged1.append([('Stir creamcheese, lemon zest, half the Parmesan, and half the basil into pot.', 'Stir')])
    tagged1.append([('Keep stirring until cheeses melt and a creamy sauce has formed.', 'Stir')])
    tagged1.append([('Season with salt and pepper.', 'Season')])

    tagged1.append([('Divide pasta mixture between plates.', 'Divide')])
    tagged1.append([('Sprinkle with remaining basil and Parmesan and serve.', 'Sprinkle')])

    # 31
    tagged1.append([('Wash and dry all produce.', 'Wash'),
                    ('Bring a large pot of salted water to a boil.', 'Boil'),
                    ('Dice one tomato.', 'Dice'),
                    ('Zest 1 tsp zest from lemon, then cut into quarters.', 'Zest'),
                    ('Pat chicken dry with a paper towel.', 'Pat'),
                    ('Season with salt, pepper, and Tuscan heat spice.', 'Season'),
                    ('Once water is boiling, add cavatappi to pot.', 'Add'),
                    ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
                    ('Reserve Â¼ cup cooking water, then drain.', 'Reserve'),
                    ('Meanwhile, heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
                    ('Add chicken and cook until no longer pink in center, 4-5 minutes per side.', 'Cook'),
                    ('(TIP: Work in batches if you canâ€™t fit all the chicken comfortably.)', 'Work'),
                    ('Remove from pan and set aside to rest.', 'Remove'),
                    ('Cut chicken into 1-inch pieces once cool enough to handle.', 'Cut'),
                    ('Heat another drizzle of olive oil in same pan over medium heat.', 'Heat'),
                    ('Add diced tomato.', 'Add'),
                    ('Cook, tossing, until slightly softened, 1-2 minutes.', 'Cook')])

    # 32
    tagged1.append([('Wash and dry all produce.', 'Wash')])
    tagged1.append([('Bring a large pot of salted water to a boil.', 'Boil')])
    tagged1.append([('Cut any large broccoli florets into bite-sized pieces.', 'Cut')])
    tagged1.append([('Remove sausage from casings.', 'Remove')])

    tagged1.append([('Wash and dry all produce.', 'Wash')])
    tagged1.append([('Bring a large pot of salted water to a boil.', 'Boil')])
    tagged1.append([('Cut any large broccoli florets into bite-sized pieces.', 'Cut')])
    tagged1.append([('Remove sausage from casings.', 'Remove')])

    tagged1.append([('Heat a drizzle of olive oil in a large pan over medium heat.', 'Heat')])
    tagged1.append([('Add broccoli and 2 tsp water.', 'Add')])
    tagged1.append([('Cover and steam 3 minutes.', 'Steam')])
    tagged1.append([('Uncover and increase heat to medium high.', 'Increase')])
    tagged1.append([('Cook, tossing occasionally, until browned and tender, 3-6 minutes more.', 'Cook')])
    tagged1.append([('Season with salt and pepper.', 'Season')])
    tagged1.append([('Remove from pan and set aside.', 'Remove')])

    tagged1.append([('Heat another drizzle of olive oil in same pan over medium-high heat.', 'Heat')])
    tagged1.append([('Add sausage, breaking up into pieces with a spatula or wooden spoon.', 'Add')])
    tagged1.append([('Cook until crisp at edges and no longer pink, 4-5 minutes.', 'Cook')])
    tagged1.append([('Add a pinch of chili flakes (to taste) and cook another 30 seconds', 'Add')])

    tagged1.append([('Add orecchiette, broccoli, pesto, pasta cooking water, and half the Parmesan to pan.', 'Add')])
    tagged1.append([('Toss until everything is well-coated and a thick sauce has formed, 1-2 minutes.', 'Toss')])
    tagged1.append([('Season with salt and pepper.', 'Season')])

    tagged1.append([('Divide orecchiette mixture between plates.', 'Divide')])
    tagged1.append([('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])

    # 33
    tagged1.append([('Bring a medium pot of salted water to a boil.', 'Boil')])
    tagged1.append([('Wash and dry all produce.', 'Wash')])
    tagged1.append([('Trim and thinly slice scallions, separating whites from greens.', 'Trim')])
    tagged1.append([('Trim and thinly slice mushrooms into ¼-inch-thick pieces.', 'Trim')])
    tagged1.append([('Heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat')])
    tagged1.append([('Add mushrooms; season with salt and pepper.', 'Add')])
    tagged1.append([('Cook, stirring occasionally, until browned and slightly crispy, 5-7 minutes.', 'Cook')])
    tagged1.append([('Turn off heat; transfer to a paper-towel lined plate.', 'Transfer')])
    tagged1.append([('Rinse and wipe out pan.', 'Rinse')])
    tagged1.append([('Once water is boiling, add gemelli to pot.', 'Add')])
    tagged1.append([('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook')])
    tagged1.append([('Reserve 1 cup pasta cooking water, then drain.', 'Reserve')])
    tagged1.append([('Meanwhile, melt 2 TBSP plain butter (4 TBSP for 4 servings) in pan used for '
                    'mushrooms over medium-high heat.','Melt')])
    tagged1.append([('Add scallion whites and cook until just softened, 30 seconds to 1 minute.', 'Add')])
    tagged1.append([('Add flour and cook, stirring, until lightly browned, about 1 minute.', 'Add')])
    tagged1.append([('Gradually whisk in chicken stock concentrate and 1 cup water until smooth.', 'Whisk')])
    tagged1.append([('Bring to a boil, then reduce heat and simmer until thickened, 2-3 minutes.', 'Simmer')])
    tagged1.append([('Stir in half the Parmesan (we\'ll use the rest later) until melted and combined.', 'Stir')])
    tagged1.append([('Season with salt and pepper.', 'Season')])
    tagged1.append([('Add cooked gemelli, mushroom mixture, and spinach to pan with sauce.', 'Add')])
    tagged1.append([('Toss until well combined, 1-2 minutes.', 'Add')])
    tagged1.append([('Divide between plates. Sprinkle with remaining Parmesan.', 'Divide')])

    # 34
    tagged1.append([('Wash and dry all produce.', 'Wash'),
                    ('Preheat the oven to 400 degrees.', 'Preheat'),
                    ('Bring a large pot of salted water to a boil.', 'Boil'),
                    ('Halve, peel, and finely chop the onion.', 'Chop'),
                    ('Mince or grate the garlic.', 'Mince'),
                    ('Tear the mozzarella into small pieces.', 'Tear'),
                    ('Remove and discard the kale ribs and stems before coarsely chopping the leaves.',
                     'Remove'),
                    ('Pick then coarsely chop the basil leaves.', 'Chop'),
                    ('Add the fusilli to the boiling water.', 'Add'),
                    ('Cook 9-11 minutes, until al dente.', 'Cook'),
                    ('Drain.', 'Drain'),
                    ('Meanwhile, heat a large drizzle of olive oil in a large pan over medium heat.', 'Heat'),
                    ('Add the onions.', 'Add'),
                    ('Cook, tossing, for 4-5 minutes, until softened.', 'Cook'),
                    ('Add the beef, garlic, oregano, and as many chili flakes as you like.', 'Add'),
                    ('Break up the meat into pieces, until browned.', 'Break'),
                    ('Add the kale to the pan.', 'Add'),
                    ('Toss 3-4 minutes, until wilted.', 'Toss'),
                    ('Add a splash of water, if needed.', 'Add'),
                    ('Season with salt and pepper.', 'Season'),
                    ('Stir in the cooked fusilli, marinara sauce, and 1 cup water.', 'Stir'),
                    ('Top with mozzarella.', 'Top'),
                    ('Bake for 15-20 minutes, until the cheese is melted and bubbly.', 'Bake')])

    # 35
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Adjust rack to upper position and preheat oven to 400 degrees.', 'Preheat'),
         ('Zest Â½ tsp zest from lemon, then cut into quarters.', 'Zest'),
         ('Squeeze 1 TBSP juice into a small bowl (save any remaining lemon for another use).', 'Squeeze'),
         ('Cut tomato into Â½-inch-thick wedges.', 'Cut'),
         ('Line a baking sheet with aluminum foil, then arrange tomato wedges on it skin-side down.', 'Line'),
         ('Sprinkle with a drizzle of olive oil.', 'Sprinkle'),
         ('Season with salt, pepper, and 1 tsp Tuscan heat spice (save the rest for step 4).', 'Season'),
         ('Roast in oven until wilted and beginning to release their juices, about 25 minutes.', 'Roast'),
         ('Around the same time that tomatoes have roasted 10 minutes, add linguine to pot of boiling water.', 'Add'),
         ('Cook until al dente, 10-12 minutes.', 'Cook'),
         ('Reserve Â½ cup pasta cooking water, then drain.', 'Reserve'),
         ('Set linguine aside in strainer; keep pot handy for use.', 'Set'),
         ('Mince garlic and parsley leaves together until finely chopped.', 'Mince'),
         ('Heat a drizzle of olive oil in pan used for tomatoes over medium heat.', 'Heat'),
         ('Add garlic and parsley and cook, stirring, until fragrant and tender, about 2 minutes.', 'Add'),
         ('Add roasted tomatoes and their juices to pan with garlic and parsley.', 'Add'),
         ('Reduce heat to medium low and simmer until linguine is done.', 'Simmer'),
         ('Add linguine and reserved pasta cooking water to pan with sauce.', 'Add'),
         ('Toss to combine.', 'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Serve with remaining Tuscan heat spice and Parmesan cheese, if desired.', 'Serve')])
    # 36
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Adjust rack to upper position and preheat oven to 450 degrees.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Line a baking sheet with aluminum foil and lightly oil foil.', 'Line'),
         ('Halve baguettes lengthwise.', 'Halve'),
         ('Peel carrots, then chop into small pieces.', 'Peel'),
         ('Roughly chop parsley.', 'Chop'),
         ('Quarter zucchini lengthwise, then slice into thin triangles.', 'Slice'),
         ('Once water boils, add 9 oz cavatappi to pot (1½ packages; use the remainder as you like).', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-12 minutes.', 'Cook'),
         ('Drain.', 'Drain'),
         ('Heat a large drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add carrots, zucchini, and 1½ tsp Tuscan heat spice (we’ll use the rest later).', 'Add'),
         ('Cook, tossing, until browned, 6-8 minutes.', 'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Heat another drizzle of olive oil in same pan over medium-high heat.', 'Heat'),
         ('Add turkey and remaining Tuscan heat spice, breaking up meat into pieces.', 'Add'),
         ('Cook until lightly browned 3-4 minutes.', 'Cook'),
         ('Season well with salt and pepper.', 'Season'),
         ('Stir in milk and stock concentrate.', 'Stir'),
         ('Bring to a simmer and let bubble until reduced by half, 1-3 minutes.', 'Simmer'),
         ('Return veggies to pan and stir in marinara sauce.', 'Return'),
         ('Let simmer gently until meal is ready.', 'Simmer'),
         ('Spread herb butter onto cut side of baguettes.', 'Spread'),
         ('Place on lined baking sheet buttered side up and season with salt and pepper.', 'Place'),
         ('Toast in oven until light golden, 4-5 minutes.', 'Toast'),
         ('Sprinkle up to ⅓ of the Parmesan on top.', 'Sprinkle'),
         ('Return to oven and allow Parmesan to melt, about 3 minutes.', 'Allow'),
         ('Add cream cheese, half the remaining Parmesan, and all of the cooked cavatappi to pan with turkey mixture.',
          'Add'),
         ('Stir until warmed through, 2-3 minutes.', 'Stir'),
         ('Divide between bowls and sprinkle with remaining Parmesan, parsley, and chili flakes (to taste).',
          'Sprinkle'),
         ('Serve with garlic bread on the side.', 'Serve')])

    # 37
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Mince or grate garlic.', 'Mince'),
         ('Pick mint leaves from stems; discard stems.', 'Pick'),
         ('Roughly chop leaves.', 'Chop'),
         ('Heat a large, empty pan over medium-low heat.', 'Heat'),
         ('Add pine nuts and toast, tossing frequently, until lightly browned and fragrant, 2-3 minutes.', 'Add'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Once water is boiling, add penne to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Carefully scoop out and reserve ⅓ cup pasta cooking water, then drain.', 'Scoop'),
         ('Heat a large drizzle of oil in same pan over medium heat.', 'Heat'),
         ('Add half the pancetta (use the rest as you like) and cook, tossing, until lightly crisped, 2-3 minutes.',
          'Add'),
         ('Add garlic and peas and cook, tossing, until fragrant, about 1 minute.', 'Add'),
         ('Stir sour cream into pancetta mixture in pan.', 'Stir'),
         ('Add penne, half the Parmesan, stock concentrate, and reserved pasta cooking water.', 'Add'),
         ('Gently toss over medium heat until a thick, creamy sauce forms, 3-4 minutes.', 'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide penne mixture between plates.', 'Divide'),
         ('Sprinkle with mint (to taste), pine nuts, and remaining Parmesan.', 'Sprinkle')])

    # 38
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a medium pot of salted water to a boil.', 'Boil'),
         ('Heat a drizzle of oil in a large pan over medium-high heat.', 'Heat'),
         ('Pat chicken dry with a paper towel and season all over with salt, pepper, and 2 tsp Tuscan heat'
          ' spice (save the rest for step 4).', 'Season'),
         ('Add to pan and cook until no longer pink in center, 5-8 minutes per side.', 'Cook'),
         ('(TIP: Lower heat to medium if surface starts to blacken before meat is cooked through.)', 'Lower'),
         ('Remove from pan and set aside to rest.', 'Remove'),
         ('Once water boils, add gemelli to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 10-12 minutes.', 'Cook'),
         ('While gemelli cooks, pick half the basil from stems (leave the remainder on the stem and save for lunch).',
          'Pick'),
         ('Roughly chop picked leaves or tear into smaller pieces with your hands.', 'Chop'),
         ('Once gemelli is done, scoop out and reserve ¼ cup pasta cooking water, then drain.', 'Scoop'),
         ('TIP: Don’t put away the pot just yet; we’ll use it later.', 'Put'),
         ('Cut mozzarella and tomatoes into 1/2-inch pieces.', 'Cut'),
         ('Place half the tomatoes and all of the mozzarella in a reusable container.', 'Place'),
         ('Add 2 tsp vinegar and 2 tsp pesto (we’ll use more vinegar and pesto later).', 'Add'),
         ('Once chicken is cool enough to touch, cut half (2 breasts) into bite-sized pieces.', 'Cut'),
         ('Add cut chicken to container, toss to combine, and keep refrigerated until you’re '
          'ready to prep lunch in the morning.', 'Add'),
         ('Heat a drizzle of oil in pan used for chicken over medium heat.', 'Heat'),
         ('Add 1 tsp sugar and remaining tomato, Tuscan heat spice, and vinegar to pan.', 'Add'),
         ('Cook until vinegar and any juices have thickened slightly, 1-2 minutes.', 'Cook'),
         ('Stir in stock concentrate and 3 TBSP water.', 'Stir'),
         ('Bring to a simmer, then remove pan from heat.', 'Bring'),
         ('Stir in 2 TBSP butter.', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Return drained gemelli to pot and place over low heat, then stir in 2 TBSP butter, '
          'remaining pesto, and a splash of reserved pasta cooking water.', 'Stir'),
         ('(TIP: If pasta seems dry, add more water as needed.)', 'Add'),
         ('Season with plenty of salt and pepper.', 'Season'),
         ('Divide remaining chicken breasts between plates and spoon tomato sauce over top.', 'Divide'),
         ('Add pasta to the side and sprinkle with Parmesan.', 'Add'),
         ('Garnish with chopped basil and serve.', 'Garnish'),
         ('The next morning, pick remaining basil leaves from stems.', 'Pick'),
         ('Tear leaves into smaller pieces and toss into reserved chicken salad in container.', 'Toss'),
         ('Fill tortillas with chicken salad, roll into wraps, pack, and refrigerate before enjoying '
          'cold or at room temperature.', 'Fill')])

    # 39
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Preheat broiler to high.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Core, seed, and finely dice tomato.', 'Dice'),
         ('Drain and roughly chop artichokes.', 'Chop'),
         ('Once water is boiling, add cavatappi to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Scoop out and reserve ½ cup pasta cooking water, then drain.', 'Scoop'),
         ('Melt 1 TBSP butter in a medium pan over medium heat (use an ovenproof pan if you have one).', 'Melt'),
         ('Add panko and toast, tossing frequently, until golden brown, 3-4 minutes.', 'Toast'),
         ('Transfer to a plate or small bowl.', 'Transfer'),
         ('Season with salt, pepper, and 1 tsp Tuscan heat spice (we’ll use more later).', 'Season'),
         ('Heat a drizzle of oil in same pan over medium-high heat.', 'Heat'),
         ('Add spinach and cook, tossing, until just wilted, about 2 minutes.', 'Add'),
         ('Toss in artichokes and tomato.', 'Toss'),
         ('Cook and allow to warm through, 1-2 minutes.', 'Cook'),
         ('Reduce heat to low, then add cream cheese and Italian cheese.', 'Add'),
         ('Stir until melted, then stir in remaining Tuscan heat spice.', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Stir drained cavatappi into pan, followed by ¼ cup pasta cooking water.', 'Stir'),
         ('Remove pan from heat.', 'Remove'),
         ('Add more water, if needed, to coat pasta in a loose, creamy sauce.', 'Add'),
         ('Stir Parmesan into panko, then sprinkle panko mixture over cavatappi in pan.', 'Stir'),
         ('Place under broiler and broil until panko is golden brown and crispy, 3-5 minutes.', 'Broil'),
         ('Allow pasta to cool for at least 5 minutes after removing from broiler, then divide '
          'between plates and serve.', 'Allow')])

    # 40
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Mince or grate garlic.', 'Mince'),
         ('Halve, peel, and thinly slice shallot.', 'Slice'),
         ('Finely chop parsley.', 'Chop'),
         ('Once water is boiling, add tagliatelle to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve 1 cup pasta cooking water for step 5, then drain.', 'Reserve'),
         ('Meanwhile, heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add shallot and cook, tossing, until softened, 3-5 minutes.', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Add veggie crumbles and Tuscan heat spice (to taste) to pan, breaking up crumbles '
          'into smaller pieces with a spatula or wooden spoon.','Add'),
         ('Cook, stirring occasionally, until lightly browned and crisped, 3-5 minutes.', 'Cook'),
         ('Stir in garlic and most of the parsley (save a few big pinches for garnish).', 'Stir'),
         ('Cook until fragrant, about 1 minute.', 'Cook'),
         ('Stir tomatoes, stock concentrate, and 1 cup water into pan.', 'Stir'),
         ('Bring to a boil, then lower heat and let simmer until slightly reduced, 5-10 minutes.', 'Simmer'),
         ('Season with salt and pepper.', 'Season'),
         ('Give the Bolognese a taste.', 'Taste'),
         ('If it seems sharp, try adding up to 1 tsp sugar to mellow it out.', 'Add'),
         ('Add tagliatelle, half the Parmesan, and a splash of pasta cooking water to pan '
          'and toss until thoroughly combined.', 'Add'),
         ('If Bolognese seems dry, add more pasta cooking water until it’s nice and saucy.', 'Add'),
         ('Divide pasta between plates.', 'Divide'),
         ('Garnish with reserved parsley and remaining Parmesan.', 'Garnish')])

    # 41
    tagged1.append(
        [('Adjust rack to top position and preheat oven to 450 degrees.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Halve, peel, and thinly slice onion.', 'Slice'),
         ('Trim and halve zucchini lengthwise; cut crosswise into ½-inch-thick half-moons.', 'Trim'),
         ('Toss zucchini on a baking sheet with a drizzle of oil, half the Tuscan Heat Spice, '
          'and a pinch of salt and pepper.', 'Toss'),
         ('Roast on top rack, tossing halfway through, until browned and tender, 14-16 minutes.', 'Roast'),
         ('Loosely cover with foil to keep warm.', 'Cover'),
         ('Once water is boiling, add gemelli to pot.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve 1½ cups pasta cooking water (2 cups for 4 servings), then drain.', 'Reserve'),
         ('Heat a drizzle of oil in a large pan over medium-high heat.', 'Heat'),
         ('Add onion and a pinch of salt and pepper.', 'Add'),
         ('Cook, stirring occasionally, until softened, 5-6 minutes.', 'Cook'),
         ('Add sausage and cook, breaking up meat into pieces, until browned all over, '
          '3-4 minutes (it’ll finish cooking in the next step).','Add'),
         ('Add tomato paste and remaining Tuscan Heat Spice to pan.', 'Add'),
         ('Cook, stirring constantly, until fragrant, 1-2 minutes.', 'Cook'),
         ('Stir in stock concentrate, 1 cup reserved pasta cooking water (1½ cups for 4 servings), '
          'and a big pinch of salt and pepper.', 'Stir'),
         ('Bring to a low simmer; cook until sauce is slightly thickened and sausage is cooked through, 2-3 minutes.',
          'Simmer'),
         ('Reduce heat under pan to medium low.', 'Reduce'),
         ('Stir gemelli, zucchini, sour cream, and 1 TBSP butter (2 TBSP for 4 servings) '
          'into pan until thoroughly combined.', 'Stir'),
         ('Divide between bowls.', 'Divide'),
         ('Sprinkle with Parmesan.', 'Sprinkle')])

    # 42

    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Once boiling, add penne and cook, stirring occasionally, until al dente, 10-12 minutes.', 'Cook'),
         ('Carefully scoop out and reserve ½ cup pasta cooking water, then drain.', 'Scoop'),
         ('Meanwhile, halve zucchini lengthwise, then slice into ¼-inch-thick half-moons.', 'Slice'),
         ('Thinly slice half the chili (if you like it spicy, feel free to use all).', 'Slice'),
         ('Rinse shrimp, then pat dry with a paper towel, removing as much moisture as you can.', 'Rinse'),
         ('Heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add zucchini and chili and cook, tossing occasionally, until zucchini is lightly browned, about 2 minutes.',
          'Cook'),
         ('Push zucchini to one side of pan and add another large drizzle of olive oil to center.', 'Add'),
         ('Add shrimp and cook, tossing occasionally, until pink and just cooked through, 3-4 minutes.', 'Cook'),
         ('Add linguine, garlic herb butter, half the Parmesan, and ¼ cup pasta cooking water to pan.', 'Add'),
         ('Season with plenty of salt and pepper.', 'Season'),
         ('Toss until combined and coated in a loose sauce.', 'Toss'),
         ('TIP: Add remaining ¼ cup pasta cooking water, as needed, if mixture seems dry.', 'Add'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Sprinkle with remaining Parmesan and a drizzle of olive oil.', 'Sprinkle'),
         ('TIP: Garnish with additional chili (to taste) for extra heat.', 'Garnish')])

    # 43
    tagged1.append(
        [('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Core, deseed, and thinly slice green pepper.', 'Slice'),
         ('Halve, peel, and thinly slice shallot.', 'Slice'),
         ('Mince garlic.', 'Mince'),
         ('Once water is boiling, add penne to pot.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Drain.', 'Drain'),
         ('Meanwhile, rinse shrimp, then pat very dry with paper towels; place in a medium bowl.',
          'Rinse'),
         ('Toss with a large drizzle of olive oil, half the oregano, salt, and pepper.',
          'Toss'),
         ('Heat a large, preferably nonstick, pan over medium-high heat.', 'Heat'),
         ('Add shrimp mixture and cook, stirring occasionally, until opaque and cooked through, 3-4 minutes.',
          'Cook'),
         ('Transfer to a plate.', 'Transfer'),
         ('Heat a large drizzle of olive oil in same pan over medium-high heat.', 'Heat'),
         ('Add green pepper, shallot, and a large pinch of salt.', 'Add'),
         ('Cook, stirring occasionally, until slightly softened, about 5 minutes.', 'Cook'),
         ('Stir in garlic, remaining oregano, and Â¼ tsp chili flakes (add more or less if you like).',
          'Stir'),
         ('Cook until fragrant, 30 seconds to 1 minute.', 'Cook'),
         ('Stir diced tomatoes and their juices, stock concentrate, and Â½ tsp salt (1 tsp for 4 servings) '
          'into pan with veggies.', 'Stir'),
         ('Bring to a boil, then reduce heat to medium and simmer until sauce is slightly thickened, 5-7 minutes.',
          'Simmer'),
         ('Stir in shrimp, penne, and 2 TBSP butter (4 TBSP for 4) until combined.', 'Stir'),
         ('Turn off heat.', 'Turn off'),
         ('Taste and season with salt.', 'Season'),
         ('For a kick, add more chili flakes.', 'Add'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Sprinkle with additional chili flakes, if desired.', 'Sprinkle')])

    # 44

    tagged1.append(
        [('Adjust rack to top position and preheat oven to 400 degrees.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Zest and quarter lemon.', 'Zest'),
         ('Cut tomatoes into Â½-inch-thick wedges.', 'Cut'),
         ('Line a baking sheet with foil.', 'Line'),
         ('Arrange tomato wedges on prepared sheet, skin sides down.', 'Arrange'),
         ('Drizzle with olive oil and season with salt, pepper, and 1 tsp Tuscan Heat Spice '
          '(save the rest for step 4).', 'Drizzle'),
         ('Roast on top rack until softened and beginning to release their juices, 20-25 minutes.',
          'Roast'),
         ('Once tomatoes have roasted 10 minutes, add spaghetti to pot of boiling water.',
          'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve Â½ cup pasta cooking water (1 cup for 4 servings), then drain.', 'Reserve'),
         ('Set spaghetti aside in strainer; keep pot handy for use in step 5.', 'Set aside'),
         ('Pat chicken dry with paper towels; season all over with salt, pepper, and remaining Tuscan Heat Spice.',
          'Season'),
         ('Heat a drizzle of oil in a large pan over medium-high heat.', 'Heat'),
         ('Add chicken and cook, stirring occasionally, until browned and cooked through, 4-6 minutes.',
          'Cook'),
         ('Turn off heat.', 'Turn off'),
         ('Melt 1 TBSP plain butter (2 TBSP for 4 servings) in pot used for spaghetti over medium-low heat.',
          'Melt'),
         ('Add lemon zest, cream cheese, and â…“ cup reserved pasta cooking water (Â¾ cup for 4); whisk until smooth.',
          'Add'),
         ('Stir in spaghetti, garlic herb butter, juice from half the lemon (whole lemon for 4), '
          'and half the Parmesan.', 'Stir'),
         ('Stir in chicken and season with salt and pepper.', 'Stir'),
         ('Pick basil leaves from stems; discard stems and roughly chop or tear leaves.', 'Pick'),
         ('Divide spaghetti between bowls and top with tomato wedges.', 'Divide'),
         ('Garnish with basil leaves and remaining Parmesan.', 'Garnish')])

    # 45

    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Halve, peel, and finely chop onion.', 'Chop'),
         ('Mince or grate garlic.', 'Grate'),
         ('Pick leaves from tarragon; discard stems.', 'Pick'),
         ('Finely chop leaves.', 'Chop'),
         ('Halve lemon.', 'Halve'),
         ('Thinly slice mushrooms.', 'Slice'),
         ('Once water is boiling, add tagliatelle to pot.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Drain, reserving Â½ cup cooking water.', 'Drain'),
         ('Meanwhile, heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add onion and season with salt and pepper.', 'Add'),
         ('Cook, tossing, until softened, about 5 minutes.', 'Cook'),
         ('Add garlic and mushrooms.', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Cook, tossing, until mushrooms are tender, about 5 minutes more.', 'Cook'),
         ('Add stock concentrates, pasta cooking water, and half the tarragon to pan with mushrooms.',
          'Add'),
         ('Let simmer until slightly reduced, about 3 minutes.', 'Simmer'),
         ('Stir in sour cream.', 'Stir'),
         ('Cook until slightly thickened, about 3 minutes more.', 'Cook'),
         ('Add tagliatelle, a squeeze of lemon, and half the Parmesan to pan with sauce and toss to combine.',
          'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide tagliatelle and mushrooms between plates.', 'Divide'),
         ('Sprinkle with remaining Parmesan and tarragon (to taste) and serve.', 'Sprinkle')])

    # 46
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Preheat oven to 450 degrees.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Zest lemon until you have 1 tsp zest, then cut into halves.', 'Zest'),
         ('Cut one half into wedges.', 'Cut'),
         ('Mince or grate garlic.', 'Grate'),
         ('Thinly slice basil leaves.', 'Slice'),
         ('Core, seed, and thinly slice bell peppers.', 'Slice'),
         ('Toss bell peppers on a baking sheet with a large drizzle of olive oil and a pinch of salt and pepper.',
          'Toss'),
         ('Roast in oven until lightly browned, about 15 minutes.', 'Roast'),
         ('Melt 2 TBSP butter in a large pan over medium heat.', 'Melt'),
         ('Add panko and toast, stirring, until golden brown, 2-3 minutes.', 'Add'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Once water is boiling, add farfalle to pot.', 'Add'),
         ('Cook, stirring occasionally, until just al dente, about 9 minutes.', 'Cook'),
         ('Scoop out and reserve 1 cup pasta water, then drain.', 'Scoop'),
         ('While pasta cooks, heat a large drizzle of olive oil in same pan over medium-high heat.',
          'Heat'),
         ('Rinse shrimp and pat dry with a paper towel.', 'Rinse'),
         ('Season with Italian seasoning, salt, and pepper.', 'Season'),
         ('Add to pan and cook, tossing, until almost opaque, 1-2 minutes.', 'Cook'),
         ('Add garlic and cook, tossing, until fragrant, about 1 minute more.', 'Cook'),
         ('Toss pasta and bell peppers into pan with shrimp.', 'Toss'),
         ('Add lemon zest, 2 TBSP butter, half the basil, pasta water, and a squeeze of lemon.',
          'Add'),
         ('Bring to a boil and let bubble, stirring occasionally, until a sauce has formed, 3-4 minutes.',
          'Bring'),
         ('Season with salt, pepper, and a squeeze of lemon (to taste).', 'Season'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Sprinkle with panko and remaining basil.', 'Sprinkle'),
         ('Top with a large drizzle of olive oil and serve with lemon wedges on the side for squeezing over.',
          'Top')])

    # 47
    tagged1.append(
        [('Bring a large pot of salted water to a boil.', 'Bring'),
         ('Wash and dry all produce.', 'Wash'),
         ('Trim and dice zucchini into Â¼-inch pieces.', 'Trim'),
         ('Dice mushrooms into Â¼-inch pieces.', 'Dice'),
         ('Dice tomato into Â¼-inch pieces.', 'Dice'),
         ('Halve, peel, and finely dice onion.', 'Dice'),
         ('Once water is boiling, add spaghetti to pot and cook until al dente, 9-11 minutes.', 'Add'),
         ('Reserve 2 cups pasta cooking water, then drain.', 'Reserve'),
         ('Meanwhile, heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add onion and cook until lightly browned, 3-4 minutes.', 'Add'),
         ('Add mushrooms and zucchini and cook until lightly browned and slightly softened, another 5-7 minutes.',
          'Add'),
         ('Season generously with salt and pepper.', 'Season'),
         ('Add tomato, tomato paste, Italian Seasoning, Â¾ tsp garlic powder (1Â½ tsp for 4 servings), '
          'and a small pinch of chili flakes to pan.', 'Add'),
         ('Cook, stirring, until thoroughly combined, 1-2 minutes.', 'Cook'),
         ('Add stock concentrate and 1Â½ cups reserved pasta cooking water.', 'Add'),
         ('Bring to a boil, then reduce heat to a simmer.', 'Bring'),
         ('Cook until thickened and veggies are soft, 7-8 minutes.', 'Cook'),
         ('Meanwhile, place 2 TBSP butter (4 TBSP for 4 servings) in a small bowl and'
          ' microwave until just softened, about 10 seconds (do not melt).', 'Place'),
         ('Stir in 1 TBSP Parmesan (2 TBSP for 4 servings), remaining garlic powder, '
          'a pinch of salt, and a pinch of chili flakes (to taste).', 'Stir'),
         ('Halve demi-baguette and toast until golden.', 'Halve'),
         ('Spread butter mixture onto cut sides of baguette, then halve on a diagonal.', 'Spread'),
         ('Add spaghetti, 1 TBSP butter (2 TBSP for 4 servings), and a splash of remaining '
          'pasta cooking water to sauce.', 'Add'),
         ('Toss to combine, adding more pasta water as needed for sauce to fully coat pasta.', 'Toss'),
         ('Taste and season generously with salt and pepper.', 'Taste'),
         ('Divide finished pasta between bowls.', 'Divide'),
         ('Top with remaining Parmesan and a pinch of remaining chili flakes, if desired.', 'Top'),
         ('Serve with garlic bread on the side.', 'Serve')])

    # 48
    tagged1.append(
        [('Adjust oven rack to top position and heat broiler to high.', 'Adjust'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Trim and dice zucchini into Â¼-inch pieces.', 'Trim'),
         ('Halve, peel, and dice onion.', 'Halve'),
         ('Peel and mince or grate garlic.', 'Peel'),
         ('Cut mozzarella into Â½-inch cubes.', 'Cut'),
         ('Once water is boiling, add penne to pot.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve Â½ cup pasta cooking water (Â¾ cup for 4 servings), then drain.',
          'Reserve'),
         ('While pasta cooks, heat a large drizzle of olive oil in a large, preferably ovenproof, '
          'pan over medium-high heat.', 'Heat'),
         ('Add zucchini and cook, stirring, until just browned, 4-6 minutes.', 'Add'),
         ('Stir in onion, garlic, and half the Tuscan Heat Spice (youâ€™ll use the rest in the next step).',
          'Stir'),
         ('Cook, stirring, until onion is softened, 3-5 minutes.', 'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Add marinara sauce, penne, remaining Tuscan Heat Spice, and reserved pasta cooking water to '
          'pan with veggies; stir to combine.', 'Add'),
         ('Simmer until warmed through, 3-4 minutes.', 'Simmer'),
         ('Stir in half the Parmesan (youâ€™ll use the rest in the next step).', 'Stir'),
         ('Season with plenty of salt and pepper.', 'Season'),
         ('Remove pan from heat.', 'Remove'),
         ('TIP: If your pan is not ovenproof, transfer pasta now to a baking dish.', 'Transfer'),
         ('In a small bowl, stir together panko, remaining Parmesan, and a drizzle of olive oil.', 'Stir'),
         ('Top pasta with mozzarella, then panko mixture.', 'Top'),
         ('Broil pasta on top rack until panko is golden brown, sauce is bubbly, and cheese has melted, 5-7 minutes.',
          'Broil'),
         ('(TIP: Watch carefully to avoid burning.)', 'Watch'),
         ('Let cool slightly, then divide between plates or bowls.', 'Divide'),
         ('Drizzle with basil oil and serve.', 'Drizzle')])
    # 49
    tagged1.append([
        ('Wash and dry all produce.', 'Wash'),
        ('Preheat broiler to high or oven to 500 degrees.', 'Preheat'),
        ('Bring a large pot of salted water to a boil.', 'Boil'),
        ('Mince or grate garlic.', 'Mince'),
        ('Roughly chop parsley.', 'Chop'),
        ('Once water is boiling, add cavatappi to pot.', 'Add'),
        ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
        ('Drain.', 'Drain'),
        ('Place 1 TBSP butter in a small bowl.', 'Place'),
        ('Microwave on high until melted, about 20 seconds.', 'Microwave'),
        ('(TIP: Alternatively, melt butter in a small pan.)', 'Melt'),
        ('Add panko and half the parsley to bowl and stir to combine.', 'Add'),
        ('Season with salt and pepper.', 'Season'),
        ('Heat a drizzle of oil in a large, tallsided pan over medium-high heat (use'
         ' an ovenproof pan if you have one).', 'Heat'),
        ('Add pancetta and cook, tossing, until crisp, 4-5 minutes.', 'Add'),
        ('Transfer to a paper-towel lined plate with a slotted spoon, keeping as much oil in pan as possible.',
         'Transfer'),
        ('Lower heat under pan to medium.', 'Lower'),
        ('Add garlic and cook until fragrant, about 30 seconds.', 'Add'),
        ('Add flour and cook, stirring constantly, until it loses its raw smell, about 1 minute.', 'Add'),
        ('Slowly pour in 2 cups milk (we sent more), whisking vigorously to incorporate.', 'Pour'),
        ('Bring to a gentle boil and cook until thickened, 1-2 minutes.', 'Boil'),
        ('Remove from heat, then add Parmesan and stir until melted.', 'Remove'),
        ('Add tomatoes and spinach to pan.', 'Add'),
        ('Stir to wilt spinach (if leaves do not wilt, return pan to medium heat).', 'Stir'),
        ('Season with salt and pepper.', 'Season'),
        ('Stir in drained cavatappi, pancetta, and remaining parsley.', 'Stir'),
        ('Season with salt and pepper.', 'Season'),
        ('(TIP: If your pan is not ovenproof, transfer mixture to a small baking dish at this point.)', 'Transfer'),
        ('Sprinkle crust mixture over top of pasta.', 'Sprinkle'),
        ('Broil or bake until crust is golden, 2-3 minutes.', 'Broil'),
        ('Divide pasta between plates and serve.', 'Divide')
    ])

    # 50
    tagged1.append(
        [('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Peel and thinly slice shallot.', 'Peel'),
         ('Thinly slice garlic.', 'Slice'),
         ('Zest lemon until you have ½ tsp; quarter lemon.', 'Zest'),
         ('Roughly chop olives.', 'Chop'),
         ('Thinly slice chili.', 'Slice'),
         ('Once water is boiling, add spaghetti to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve ¼ cup pasta cooking water, then drain.', 'Reserve'),
         ('Meanwhile, in a medium bowl, whisk together juice from 2 lemon wedges, a drizzle '
          'of olive oil, and lemon zest until combined.', 'Whisk'),
         ('Stir in 1 TBSP shallot and season with salt and pepper.', 'Stir'),
         ('Heat a large drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add garlic, half the olives, and remaining shallot.', 'Add'),
         ('Cook, stirring, until softened, 2-3 minutes.', 'Cook'),
         ('If desired, add a pinch of chili for spiciness; cook for 15 seconds.', 'Add'),
         ('Add marinara and a pinch of salt and pepper.', 'Add'),
         ('Bring to a simmer and cook for 2 minutes, stirring a couple of times.', 'Simmer'),
         ('Turn off heat.', 'Turn off'),
         ('Add spaghetti to pan with sauce; stir until thoroughly coated.', 'Add'),
         ('Stir in half the Parmesan and 2 TBSP butter.', 'Stir'),
         ('If sauce seems thick, add reserved pasta cooking water, 1 TBSP at a time, until loosened.', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Add arugula to bowl with dressing; season with salt and pepper and toss to thoroughly coat.', 'Add'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Top with remaining olives and remaining Parmesan.', 'Top'),
         ('Sprinkle with a pinch of remaining chili (to taste).', 'Sprinkle'),
         ('Serve with salad on the side and remaining lemon wedges for squeezing over.', 'Serve')])

    # 51
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Adjust rack to upper position and preheat oven to 375 degrees.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Cut tomatoes into wedges.', 'Cut'),
         ('Toss with 1 TBSP olive oil, salt, and pepper on a foil-lined baking sheet and arrange skin-side down.',
          'Toss'),
         ('Roast until soft and juicy, about 30 minutes.', 'Roast'),
         ('Meanwhile, mince garlic.', 'Mince'),
         ('Finely chop parsley.', 'Chop'),
         ('Cut chorizo into ¼-inch cubes.', 'Cut'),
         ('Once water boils, add penne to pot.', 'Add'),
         ('Cook until al dente, 10-12 minutes.', 'Cook'),
         ('Scoop out and reserve 2 cups pasta cooking water, then drain.', 'Reserve'),
         ('While penne cooks, heat a large pan over medium-high heat.', 'Heat'),
         ('Add chorizo and pancetta.', 'Add'),
         ('Cook, tossing, until beginning to release oil and crisp, 5-6 minutes.', 'Cook'),
         ('Remove a quarter of the meats from pan and set aside,', 'Remove'),
         ('Toss garlic into pan and cook until fragrant, about 30 seconds.', 'Cook'),
         ('Add tomato paste and cook, stirring, 2-3 minutes.', 'Add'),
         ('Add 1½ cups pasta cooking water and cream cheese;', 'Add'),
         ('Stir until well-combined.', 'Stir'),
         ('Stir peas into pan and allow to warm through, about 2 minutes.', 'Stir'),
         ('Season with plenty of salt and pepper.', 'Season'),
         ('Stir in drained penne, 2 TBSP butter, and a pinch of chili flakes (to taste).', 'Stir'),
         ('(TIP: Add more pasta cooking water, if needed, to give sauce a loose, saucy consistency.)', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide pasta between bowls and top with roasted tomatoes.', 'Divide'),
         ('Sprinkle with Parmesan, parsley, and a pinch of chili flakes (to taste—you may want to '
          'leave this off for the kids).', 'Sprinkle'),
         ('Garnish with reserved chorizo and pancetta.', 'Garnish')])

    # 52

    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Cut any large broccoli florets into bite-sized pieces.', 'Cut'),
         ('Remove sausage from casings.', 'Remove'),
         ('Once water is boiling, add orecchiette to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Carefully scoop out and reserve 1/2 cup pasta cooking water, then drain.', 'Scoop'),
         ('Heat a large drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add broccoli and 4 tsp water.', 'Add'),
         ('Cover and steam 3 minutes.', 'Steam'),
         ('Uncover and increase heat to medium-high.', 'Increase'),
         ('Cook, tossing occasionally, until browned and tender, 3-6 minutes more.', 'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Heat another large drizzle of olive oil in same pan over medium-high heat.', 'Heat'),
         ('Add sausage, breaking up into pieces with a spatula or wooden spoon.', 'Add'),
         ('Cook until crisp at edges and no longer pink, 4-5 minutes.', 'Cook'),
         ('Add a pinch of chili flakes (to taste) and cook another 30 seconds.', 'Add'),
         ('Add broccoli, pesto, pasta cooking water, sausage mixture, and half the Parmesan to pot with orecchiette.',
          'Add'),
         ('Return pot to stove over medium-high heat.', 'Return'),
         ('Toss until everything is well-coated and a thick sauce has formed, 1-2 minutes.', 'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide orecchiette mixture between plates.', 'Divide'),
         ('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])

    # 53
    tagged1.append(
        [('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Once water is boiling, add penne and cook, stirring occasionally, until al dente, 10-12 minutes.', 'Add'),
         ('Scoop out and reserve ½ cup pasta cooking water, then drain.', 'Scoop'),
         ('Meanwhile, wash and dry all produce.', 'Wash'),
         ('Drain capers; thoroughly pat dry with paper towels.', 'Drain'),
         ('Trim off and discard woody ends from asparagus; cut crosswise into 1-inch pieces.', 'Trim'),
         ('Dice tomato.', 'Dice'),
         ('Zest 1 tsp zest from lemon; quarter lemon.', 'Zest'),
         ('Heat a large drizzle of oil in a large pan over medium-high heat.', 'Heat'),
         ('Once oil is hot enough that a caper sizzles immediately when added to the pan, '
          'add capers and cook, stirring occasionally, until crispy, 1-3 minutes.', 'Add'),
         ('Carefully transfer capers to a paper-towel-lined plate.', 'Transfer'),
         ('Heat a drizzle of oil in same pan over medium-high heat.', 'Heat'),
         ('Add asparagus and a pinch of chili flakes.', 'Add'),
         ('Cook, stirring often, until bright green, 2-4 minutes.', 'Cook'),
         ('Add tomato and cook, stirring, until slightly softened, 1-2 minutes.', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Add penne, garlic herb butter, half the Parmesan, and ⅓ cup reserved pasta cooking water to pan.', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Stir until thoroughly combined and a loose sauce has formed.', 'Stir'),
         ('Turn off heat; stir in a squeeze of lemon juice.', 'Stir'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Sprinkle with remaining Parmesan, a drizzle of olive oil and as many crispy '
          'capers as you like (you may have capers leftover).', 'Sprinkle'),
         ('Garnish with lemon zest and additional chili flakes (to taste).', 'Garnish'),
         ('Serve with remaining lemon wedges on the side for squeezing over.', 'Serve')])
    # 54
    tagged1.append(
        [('Bring a large pot of salted water to a boil.', 'Bring'),
         ('Wash and dry produce.', 'Wash'),
         ('Peel and mince garlic.', 'Peel'),
         ('Halve, peel, and finely dice onion.', 'Dice'),
         ('Once water is boiling, add pasta to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve 1 1⁄2 cups pasta cooking water (2 1⁄2 cups for 4 servings), then drain.', 'Reserve'),
         ('While pasta cooks, melt 1 TBSP butter (2 TBSP for 4) in a large pan over medium heat.', 'Melt'),
         ('Stir in garlic, panko, and 1⁄4 tsp Tuscan Heat Spice (1⁄2 tsp for 4).', 'Stir'),
         ('Cook, stirring occasionally, until panko is golden brown and garlic is fragrant, 2-4 minutes.', 'Cook'),
         ('Transfer to a small bowl.', 'Transfer'),
         ('Wipe out pan.', 'Wipe'),
         ('Heat a drizzle of oil in same pan over medium-high heat.', 'Heat'),
         ('Add sausage*, 1⁄2 TBSP Tuscan Heat Spice (1 TBSP for 4 servings; save the rest '
          'for another use), and a pinch of salt.', 'Add'),
         ('Cook, breaking up meat into pieces, until sausage is browned and cooked through, 4-6 minutes.', 'Cook'),
         ('Transfer sausage to a plate.', 'Transfer'),
         ('Reserve pan.', 'Reserve'),
         ('Heat a drizzle of oil in same pan over medium-high heat.', 'Heat'),
         ('Add onion and cook, stirring occasionally until slightly browned and softened, 4-6 minutes.', 'Add'),
         ('Reduce heat to medium.', 'Reduce'),
         ('Stir in cream cheese, stock concentrate, cream sauce base, broccoli rice, half the '
          'Parmesan (save the rest for serving), 1 cup reserved pasta cooking water (2 cups for 4 servings), '
          'and 1⁄2 tsp salt (1 tsp for 4).', 'Stir'),
         ('Bring to a simmer and cook, stirring, until thickened, 2-3 minutes.', 'Bring'),
         ('Reduce heat to low; stir drained pasta and sausage into pan with sauce.', 'Stir'),
         ('Increase heat to medium high; simmer until sauce is slightly thickened, 1-3 minutes.', 'Simmer'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Top with garlic panko and remaining Parmesan and serve.', 'Top')
         ])

    # 55
    tagged1.append(
        [('Adjust rack to middle position and preheat oven to 400 degrees.', 'Adjust'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Halve bell pepper; remove stem and seeds.', 'Halve'),
         ('Peel garlic.', 'Peel'),
         ('Thinly slice chili.', 'Slice'),
         ('Remove sausage* from casing; discard casing.', 'Remove'),
         ('Drizzle each bell pepper half with oil and season with salt and pepper; place cut sides '
          'down on a lightly oiled baking sheet.', 'Drizzle'),
         ('Place garlic in the center of a small piece of foil.', 'Place'),
         ('Drizzle with oil; season with salt and pepper.', 'Drizzle'),
         ('Cinch into a packet and place on same sheet.', 'Cinch'),
         ('Roast on middle rack until pepper is lightly charred and garlic is softened, 20-25 minutes.', 'Roast'),
         ('Once water is boiling, add cavatappi to pot.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve 1 cup pasta cooking water (2 cups for 4 servings), then drain.', 'Reserve'),
         ('While pasta cooks, heat a drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add sausage and cook, breaking up meat into pieces, until browned and cooked through, 4-6 minutes.', 'Cook'),
         ('If desired, stir in a pinch of chili; cook until fragrant, 15 seconds.', 'Stir'),
         ('Add tomato paste and ½ cup reserved pasta cooking water (¾ cup for 4 servings).', 'Add'),
         ('Simmer until thickened, 2-3 minutes more.', 'Simmer'),
         ('Turn off heat.', 'Turn off'),
         ('Carefully transfer roasted bell pepper and garlic to a cutting board.', 'Transfer'),
         ('Thinly slice bell pepper into strips; mash garlic with a fork.', 'Slice'),
         ('Return pan with sauce to low heat; stir in garlic.', 'Return'),
         ('Pour in cream sauce base.', 'Pour'),
         ('Stir in bell pepper, drained cavatappi, half the Parmesan (save the rest for serving), '
          'and 2 TBSP butter (4 TBSP for 4 servings).', 'Stir'),
         ('Season pasta with salt and pepper and divide between bowls.', 'Season'),
         ('Sprinkle with remaining Parmesan and, if desired, a pinch of remaining chili.', 'Sprinkle'),
         ('Serve.', 'Serve')])

    # 56
    tagged1.append(
        [('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Trim and thinly slice scallions, separating whites from greens.', 'Trim'),
         ('Remove any large stems and ribs from kale; thinly slice leaves.', 'Remove'),
         ('Heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add beef and season with salt and pepper.', 'Add'),
         ('Cook, breaking up meat into pieces, until browned and cooked through, 4-6 minutes.', 'Cook'),
         ('Turn off heat.', 'Turn off'),
         ('Using a slotted spoon and leaving as much fat in pan as possible, transfer beef to a large bowl.',
          'Transfer'),
         ('Once water is boiling, add penne to pot.', 'Add'),
         ('Cook until al dente, about 10 minutes.', 'Cook'),
         ('Reserve 2 cups pasta cooking water, then drain and set aside.', 'Reserve'),
         ('Return pot to stove.', 'Return'),
         ('Add kale to pan with reserved fat and season generously with salt and pepper.', 'Add'),
         ('Cook over medium-high heat, stirring often, until tender and bright green, 5-7 minutes.', 'Cook'),
         ('TIP: If pan seems dry, add another drizzle of olive oil.', 'Add'),
         ('Turn off heat.', 'Turn off'),
         ('Transfer to bowl with beef.', 'Transfer'),
         ('Heat 1 TBSP butter in pot used to cook pasta.', 'Heat'),
         ('Add scallion whites and half the Tuscan Heat Spice.', 'Add'),
         ('Cook, stirring, until tender, 1-2 minutes.', 'Cook'),
         ('Add tomato paste and cook, stirring, until dark red, 1-2 minutes.', 'Add'),
         ('Stir in cream cheese, sour cream, and ¾ cup pasta cooking water until thoroughly combined.', 'Stir'),
         ('Reduce heat to medium low.', 'Reduce'),
         ('Stir beef and kale, pasta, 1 TBSP butter, ¼ cup remaining pasta cooking water, '
          'and remaining Tuscan Heat Spice into pot with sauce.', 'Stir'),
         ('Cook, stirring, until thoroughly combined, 1-2 minutes.', 'Cook'),
         ('TIP: If pan seems dry, gradually add remaining pasta cooking water to achieve desired consistency.', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Sprinkle with Parmesan and scallion greens.', 'Sprinkle')])

    # 57
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Adjust rack to upper position and preheat oven to 450 degrees.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Line a baking sheet with foil.', 'Line'),
         ('Roughly chop hazelnuts.', 'Chop'),
         ('Zest lemon until you have 1 tsp zest, then halve.', 'Zest'),
         ('Squeeze 1 TBSP juice into a small bowl.', 'Squeeze'),
         ('Halve, peel, and finely mince shallot.', 'Mince'),
         ('Mince garlic.', 'Mince'),
         ('Finely chop chives.', 'Chop'),
         ('In another small bowl, whisk honey, a drizzle of olive oil, and a few large pinches of salt.', 'Whisk'),
         ('Place carrots on lined sheet and toss with honey mixture until coated.', 'Toss'),
         ('Arrange carrots toward one side of sheet, keeping at least a quarter of the surface area empty.', 'Arrange'),
         ('Roast in oven 12 minutes, then remove from oven and add hazelnuts to empty space on sheet.', 'Roast'),
         ('Return sheet to oven and continue roasting until carrots are tender and hazelnuts '
          'are golden brown, about 3 minutes.', 'Roast'),
         ('Meanwhile, pat chicken dry with a paper towel.', 'Pat'),
         ('Season all over with salt and pepper.', 'Season'),
         ('Heat a large drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add chicken.', 'Add'),
         ('Cook until no longer pink in center, about 6 minutes per side.', 'Cook'),
         ('Remove chicken from pan, transfer to a cutting board, and cover with foil to keep warm.', 'Remove'),
         ('Melt 2 TBSP plain butter in same pan over medium heat.', 'Melt'),
         ('Add shallot and garlic.', 'Add'),
         ('Cook until fragrant, 30-60 seconds.', 'Cook'),
         ('Whisk milk and a pinch of salt and pepper into pan, then bring to a simmer.', 'Whisk'),
         ('Add Italian cheese, cream cheese, and half the Parmesan.', 'Add'),
         ('Stir until smooth.', 'Stir'),
         ('Add pasta to pot of water.', 'Add'),
         ('Cook until just tender, about 2 minutes.', 'Cook'),
         ('Scoop out 1 cup water, then drain.', 'Scoop'),
         ('Return pasta to empty pot off heat.', 'Return'),
         ('To pan with sauce, whisk in â…“ cup pasta water.', 'Whisk'),
         ('Simmer until just thickened, about 1 minute.', 'Simmer'),
         ('Stir in peas and half the chives.', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Pour cheese sauce into pot with pasta; stir to combine.', 'Pour'),
         ('TIP: Add more water, 1 TBSP at a time, to loosen sauce, if needed.', 'Add'),
         ('Toss carrots with lemon zest and lemon juice.', 'Toss'),
         ('Sprinkle with hazelnuts, if desired.', 'Sprinkle'),
         ('Slice chicken.', 'Slice'),
         ('Divide pasta between plates.', 'Divide'),
         ('Arrange chicken on top and dollop with truffle butter, to taste.', 'Arrange'),
         ('Sprinkle with remaining Parmesan and chives.', 'Sprinkle')])

    # 58
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Once boiling, add penne and cook, stirring occasionally, until al dente, 10-12 minutes.',
          'Add'),
         ('Carefully scoop out and reserve Â½ cup pasta cooking water, then drain.',
          'Scoop'),
         ('Meanwhile, halve zucchini lengthwise, then slice into Â¼-inch-thick half-moons.',
          'Slice'),
         ('Thinly slice half the chili (if you like it spicy, feel free to use all).',
          'Slice'),
         ('Rinse shrimp, then pat dry with a paper towel, removing as much moisture as you can.',
          'Rinse'),
         ('Heat a large drizzle of olive oil in a large pan over medium-high heat.',
          'Heat'),
         ('Add zucchini and chili and cook, tossing occasionally, until zucchini is lightly browned, about 2 minutes.',
          'Add'),
         ('Push zucchini to one side of pan and add another large drizzle of olive oil to center.',
          'Add'),
         ('Add shrimp and cook, tossing occasionally, until pink and just cooked through, 3-4 minutes.',
          'Add'),
         ('Add penne, garlic herb butter, half the Parmesan, and Â¼ cup pasta cooking water to pan.',
          'Add'),
         ('Season with plenty of salt and pepper.', 'Season'),
         ('Toss until combined and coated in a loose sauce.',
          'Toss'),
         ('TIP: Add remaining Â¼ cup pasta cooking water, as needed, if mixture seems dry.',
          'Add'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Sprinkle with remaining Parmesan and a drizzle of olive oil.',
          'Sprinkle'),
         ('TIP: Garnish with additional chili (to taste) for extra heat.',
          'Garnish')])

    # 59

    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Mince or grate garlic.', 'Mince'),
         ('Halve, peel, and thinly slice shallot.', 'Slice'),
         ('Finely chop parsley.', 'Chop'),
         ('Once water is boiling, add linguine pasta to pot and cook until al dente, 9-11 minutes, '
          'stirring occasionally.', 'Add'),
         ('Reserve 1 cup pasta cooking water, then drain.', 'Reserve'),
         ('Heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add shallot and cook until softened, 3-5 minutes, tossing.', 'Add'),
         ('Season with salt and pepper', 'Season'),
         ('Add seitan crumbles and Tuscan heat spice (to tasteâ€”itâ€™s spicy) to pan, breaking '
          'up seitan into pieces with a spatula or wooden spoon.', 'Add'),
         ('Cook until lightly browned and crisped, 3-5 minutes, stirring occasionally.',
          'Cook'),
         ('Stir in garlic and most of the parsley and cook until fragrant, another 1 minute'
          ' (save a few big pinches of parsley for garnish).', 'Stir'),
         ('Stir diced tomatoes, stock concentrate, and 1 cup water into pan.', 'Stir'),
         ('Bring to a boil, then lower heat and let simmer until slightly reduced, 5-10 minutes.',
          'Bring'),
         ('Season with salt and pepper.', 'Season'),
         ('Give the Bolognese a taste.', 'Give'),
         ('If it seems sharp, try adding up to 1 tsp sugar to mellow it out.',
          'Adding'),
         ('Add linguine pasta, half the Parmesan, and a splash of pasta cooking water to pan and toss '
          'to thoroughly combine.', 'Add'),
         ('If Bolognese seems dry, add more pasta cooking water until itâ€™s nice and saucy.',
          'Add'),
         ('Divide pasta between plates.', 'Divide'),
         ('Garnish with reserved parsley and remaining Parmesan.', 'Garnish')])

    # 60

    tagged1.append(
        [('Preheat oven to 425 degrees.', 'Preheat'),
         ('Wash and dry all produce.', 'Wash'),
         ('Trim, peel, and dice carrot into small pieces.', 'Trim'),
         ('Halve, peel, and finely chop onion.', 'Chop'),
         ('Dice tomato.', 'Dice'),
         ('(JESSICAâ€™S TIP: Skip this stepâ€”wet hands, form sausage into Â½-inch balls, and set aside until step 4.)',
          'Form'),
         ('Heat a drizzle of olive oil in a large pot over medium-high heat.', 'Heat'),
         ('Add sausage and cook, breaking up meat into pieces, until browned and cooked through, 5-7 minutes.',
          'Cook'),
         ('Add another drizzle of olive oil to pot; stir in carrot, onion, and a big pinch of salt.',
          'Stir'),
         ('Cook, stirring occasionally, until just softened, 5-7 minutes.', 'Cook'),
         ('Add tomato, Â¼ tsp garlic powder (Â½ tsp for 4 servings), and half the Italian Seasoning '
          '(use the rest of the spice as you like) to pot.', 'Add'),
         ('Cook, stirring, until fragrant, 30 seconds to 1 minute.', 'Cook'),
         ('Stir in stock concentrates and 3Â½ cups warm water (6 cups for 4), scraping up any '
          'browned bits from bottom of pot.', 'Stir'),
         ('Add half the gemelli (all for 4).', 'Add'),
         ('(JESSICAâ€™S TIP: Stir in sausage meatballs now.)', 'Stir'),
         ('Cover, bring to a boil, then immediately reduce heat to low.', 'Boil'),
         ('Simmer until pasta is al dente (and meatballs are cooked through), 10 minutes.',
          'Simmer'),
         ('Meanwhile, place 2 TBSP butter (3 TBSP for 4 servings) in a small microwave-safe bowl; '
          'microwave until just softened, about 10 seconds.', 'Place'),
         ('Stir in 1 TBSP Parmesan (2 TBSP for 4), Â¼ tsp garlic powder (use remaining garlic powder for '
          '4), a pinch of salt, and a pinch of chili flakes.', 'Stir'),
         ('Halve ciabatta and spread with garlic butter; place cut sides up on a baking sheet.',
          'Halve'),
         ('Toast in oven until golden and crispy, 4-5 minutes, then halve on a diagonal.',
          'Toast'),
         ('Stir spinach and 2 TBSP Parmesan (Â¼ cup for 4 servings) into soup until spinach has wilted.',
          'Stir'),
         ('Season with plenty of salt and pepper.', 'Season'),
         ('Divide soup between bowls.', 'Divide'),
         ('Sprinkle with remaining Parmesan and a pinch of remaining chili flakes if you like.',
          'Sprinkle'),
         ('Serve with toasts on the side.', 'Serve')])

    # 61
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Adjust racks to middle and upper positions and preheat oven to 450 degrees.', 'Preheat'),
         ('Bring a medium pot of salted water to a boil.', 'Boil'),
         ('Halve zucchini lengthwise, then cut crosswise into Â¼-inch-thick half-moons.', 'Halve'),
         ('Mince or grate garlic.', 'Mince'),
         ('Slice sweet potatoes into Â¼-inch-thick rounds.', 'Slice'),
         ('Once water boils, add fusilli to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-12 minutes, then drain.', 'Cook'),
         ('Heat a drizzle of oil in a large ovenproof pan over medium-high heat.', 'Heat'),
         ('Add zucchini and cook until tender, 4-5 minutes.', 'Cook'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Heat another drizzle of oil in same pan over medium-high heat.', 'Heat'),
         ('Add garlic and cook until fragrant, about 30 seconds.', 'Add'),
         ('Add half the beef, breaking up meat into pieces.', 'Add'),
         ('Cook until browned, 5-6 minutes.', 'Cook'),
         ('Drain any excess grease.', 'Drain'),
         ('Season beef with plenty of salt and pepper.', 'Season'),
         ('Toss in zucchini and Tuscan heat spice.', 'Toss'),
         ('While beef cooks, toss sweet potatoes on a baking sheet with a drizzle of oil.', 'Toss'),
         ('Season with salt, pepper, and thyme.', 'Season'),
         ('Roast in oven on upper rack until tender and lightly crisped, 20-25 minutes, tossing halfway through.',
          'Roast'),
         ('Measure out Â¼ cup marinara sauce and place in a small bowl.', 'Measure'),
         ('Stir in a pinch of salt and pepper.', 'Stir'),
         ('Set aside.', 'Set aside'),
         ('After adding zucchini and spice to pan, stir in milk and remaining marinara sauce.', 'Stir'),
         ('Bring to a simmer.', 'Bring'),
         ('Cook until slightly reduced, 2-3 minutes.', 'Cook'),
         ('Lower heat under pan to medium.', 'Lower'),
         ('Stir in fusilli.', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Remove from heat.', 'Remove'),
         ('Sprinkle half the mozzarella over pasta.', 'Sprinkle'),
         ('Bake on middle rack of oven until cheese melts, 5-7 minutes.', 'Bake'),
         ('Set aside to cool.', 'Set aside'),
         ('Split buns in half and toast in oven or toaster until golden, 2-3 minutes.', 'Toast'),
         ('Shape rest of beef into two patties and season with salt and pepper.', 'Shape'),
         ('Heat a drizzle of oil in a large pan over medium-high heat.', 'Heat'),
         ('Add patties to pan and cook until just shy of desired doneness, 3-5 minutes per side.', 'Cook'),
         ('Top with reserved Â¼ cup marinara sauce and sprinkle with remaining mozzarella.', 'Top'),
         ('Cover pan and let cheese melt, 1-2 minutes.', 'Cover'),
         ('Fill buns with patties, divide between plates, and serve with sweet potatoes.', 'Fill'),
         ('Divide pasta between two reusable containers.', 'Divide'),
         ('Keep refrigerated until lunchtime.', 'Keep')])

    # 62
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Preheat grill or broiler to high.', 'Preheat'),
         ('If grilling, place skewers in a shallow dish and cover with water to soak.', 'Place'),
         ('Bring a medium pot of salted water to a boil.', 'Boil'),
         ('Halve, peel, and cut onion into Â½-inch wedges.', 'Cut'),
         ('If broiling, cut zucchini into Â½-inch cubes.', 'Cut'),
         ('If grilling, cut zucchini into Â¾-inch cubes.', 'Cut'),
         ('If broiling, toss onion on one side of a baking sheet with a drizzle of olive oil.', 'Toss'),
         ('Toss zucchini on other side with a drizzle of olive oil.', 'Toss'),
         ('Season both with salt and pepper.', 'Season'),
         ('If grilling, remove skewers from water.', 'Remove'),
         ('Thread onion and zucchini onto separate skewers, placing only one type of veggie on each.', 'Thread'),
         ('Drizzle with olive oil and season with salt and pepper.', 'Drizzle'),
         ('Broil or grill veggies until lightly charred, about 10 minutes.', 'Broil'),
         ('Meanwhile, stir together barbecue sauce and a pinch of chipotle powder in a small bowl.', 'Stir'),
         ('Add more chipotle powder to tasteâ€”itâ€™s spicy.', 'Add'),
         ('Once water in pot is boiling, add 4Â½ oz penne (about Â¾ of the packageâ€” use the rest as you like).',
          'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Drain, then rinse under cold water.', 'Drain'),
         ('Season chicken with salt and pepper.', 'Season'),
         ('If broiling, place on a foil-lined baking sheet and brush with half the sauce.', 'Place'),
         ('Broil until nearly cooked through, 10-12 minutes,', 'Broil'),
         ('Brush chicken with remaining sauce.', 'Brush'),
         ('Continue broiling until no longer pink in center, about 5 minutes more.', 'Broil'),
         ('If grilling, brush chicken with half the sauce,', 'Brush'),
         ('Grill over direct heat, 5-7 minutes per side.', 'Grill'),
         ('Brush with remaining sauce halfway through.', 'Brush'),
         ('While chicken cooks, halve tomatoes.', 'Halve'),
         ('Cut mozzarella into Â½-inch cubes.', 'Cut'),
         ('Toss tomatoes, mozzarella, pesto, zucchini, onion, and penne in a large bowl.', 'Toss'),
         ('Divide penne mixture and chicken between plates and serve.', 'Divide')])
    # 63
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Mince or grate garlic.', 'Mince'),
         ('Halve, peel, and thinly slice shallot.', 'Slice'),
         ('Finely chop parsley.', 'Chop'),
         ('Once water is boiling, add linguine to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve 1 cup pasta cooking water, then drain.', 'Reserve'),
         ('Meanwhile, heat a drizzle of olive oil in a large pan over medium heat.', 'Heat'),
         ('Add shallot and cook until softened, 3-5 minutes, tossing.', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Add seitan crumbles and Tuscan heat spice (to taste—it’s spicy) to pan, breaking up seitan '
          'into pieces with a spatula or wooden spoon.', 'Add'),
         ('Cook until lightly browned and crisped, 3-5 minutes, stirring occasionally.', 'Cook'),
         ('Stir in garlic and most of the parsley and cook until fragrant, another 1 minute'
          ' (save a few big pinches of parsley for garnish).', 'Stir'),
         ('Stir diced tomatoes, stock concentrate, and 1 cup water into pan.', 'Stir'),
         ('Bring to a boil, then lower heat and let simmer until slightly reduced, 5-10 minutes.', 'Simmer'),
         ('Season with salt and pepper.', 'Season'),
         ('Give the Bolognese a taste.', 'Taste'),
         ('If it seems sharp, try adding up to 1 tsp sugar to mellow it out.', 'Adding'),
         ('Add linguine, half the Parmesan, and a splash of pasta cooking water to pan and toss to thoroughly combine.',
          'Add'),
         ('If Bolognese seems dry, add more pasta cooking water until it’s nice and saucy.', 'Add'),
         ('Divide pasta between plates.', 'Divide'),
         ('Garnish with reserved parsley and remaining Parmesan.', 'Garnish')])

    # 64

    tagged1.append(
        [('Bring a medium pot of salted water to a boil.', 'Boil'),
         ('Wash and dry produce.', 'Wash'),
         ('Core, deseed, and finely dice bell pepper.', 'Dice'),
         ('Drain corn and pat dry with paper towels.', 'Drain'),
         ('Mince half the jalapeño (whole jalapeño for 4 servings), removing ribs and seeds for less heat.', 'Mince'),
         ('Trim and thinly slice scallions, separating whites from greens.', 'Slice'),
         ('Once water is boiling, add penne to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve 1⁄2 cup pasta cooking water (1 cup for 4 servings), then drain.', 'Reserve'),
         ('While pasta cooks, heat a drizzle of oil in a large pan over medium heat.', 'Heat'),
         ('Add bell pepper and season with a pinch of salt and pepper.', 'Add'),
         ('Cook, stirring occasionally, until tender, 5-7 minutes.', 'Cook'),
         ('TIP: If bell pepper starts to char, add a few splashes of water.', 'Add'),
         ('Add a drizzle of oil, corn, jalapeño, scallion whites, garlic powder, and half the oregano '
          '(all for 4 servings) to pan with bell pepper.', 'Add'),
         ('Cook, stirring occasionally, until fragrant, 2-3 minutes.', 'Cook'),
         ('Remove from heat.', 'Remove'),
         ('Stir in half the paprika (all for 4).', 'Stir'),
         ('Transfer 1⁄4 of the veggie mixture to a plate; reserve for serving.', 'Transfer'),
         ('Return pan with remaining veggies to stovetop over low heat.', 'Return'),
         ('Stir in drained penne, cream sauce base, cream cheese, half the pepper jack, '
          'half the scallion greens, and 1⁄4 cup reserved pasta cooking water.', 'Stir'),
         ('Cook, stirring, until cream cheese is just melted and pasta is coated in a creamy sauce.', 'Cook'),
         ('Remove from heat; stir in 1 TBSP butter (2 TBSP for 4) until melted.', 'Remove'),
         ('Taste and season generously with salt and pepper.', 'Season'),
         ('TIP: If needed, stir in more reserved cooking water a splash at a time.', 'Stir'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Top with reserved veggies and remaining pepper jack.', 'Top'),
         ('Garnish with scallion greens and serve.', 'Garnish')])

    # 65
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Dice one tomato.', 'Dice'),
         ('Zest 1 tsp zest from lemon, then cut into quarters.', 'Zest'),
         ('Pat chicken dry with a paper towel.', 'Pat'),
         ('Season with salt, pepper, and Tuscan heat spice.', 'Season'),
         ('Once water is boiling, add cavatappi to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve ¼ cup cooking water, then drain.', 'Reserve'),
         ('Meanwhile, heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add chicken and cook until no longer pink in center, 4-5 minutes per side.', 'Cook'),
         ('(TIP: Work in batches if you can’t fit all the chicken comfortably.)', 'Work'),
         ('Remove from pan and set aside to rest.', 'Remove'),
         ('Cut chicken into 1-inch pieces once cool enough to handle.', 'Cut'),
         ('Heat another drizzle of olive oil in same pan over medium heat.', 'Heat'),
         ('Add diced tomato.', 'Add'),
         ('Cook, tossing, until slightly softened, 1-2 minutes.', 'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Add cavatappi, 1 TBSP butter, and ¾ of the pesto and toss to combine.', 'Add'),
         ('Stir in lemon zest and half the Parmesan.', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Stir half the chicken into pan with pasta.', 'Stir'),
         ('Remove from heat and stir in a squeeze or two of lemon.', 'Stir'),
         ('(TIP: If mixture seems dry, add a bit of pasta cooking water.)', 'Add'),
         ('Let pasta cool slightly, then stir in ⅔ of the arugula.', 'Stir'),
         ('Divide between plates, sprinkle with remaining Parmesan, and serve.', 'Divide'),
         ('FOR LUNCH: After dinner, toss together sour cream, a squeeze of lemon, and remaining '
          'chicken and pesto in a large bowl.', 'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Cover and set aside in the fridge.', 'Cover'),
         ('When ready to pack your lunch, slice remaining tomato into thin rounds.', 'Slice'),
         ('Cut baguettes in half lengthwise.', 'Cut'),
         ('Divide chicken, tomato, baguettes, and remaining arugula and lemon between lunchboxes.', 'Divide'),
         ('FOR LUNCH: When you’re ready to eat lunch, toast the baguettes in a toaster until crisp and golden.',
          'Toast'),
         ('Toss arugula with a squeeze of lemon juice, a drizzle of olive oil, and salt and pepper.', 'Toss'),
         ('Fill baguettes with chicken, arugula, and tomato, making sandwiches.', 'Fill')])

    # 66
    tagged1.append(
        [('Bring a large pot of salted water to a boil.', 'Bring'),
         ('Add pasta and cook, stirring, until al dente, 15-17 minutes.', 'Add'),
         ('Reserve ½ cup pasta cooking water, then drain.', 'Reserve'),
         ('Meanwhile, wash and dry all produce.', 'Wash'),
         ('Halve, peel, and thinly slice shallot.', 'Slice'),
         ('Roughly chop sage leaves until you have 1 TBSP.', 'Chop'),
         ('Thinly slice mushrooms.', 'Slice'),
         ('Finely chop garlic.', 'Chop'),
         ('While pasta cooks, in a medium microwave-safe bowl, combine butternut squash and a splash of water.',
          'Combine'),
         ('Cover with plastic wrap and poke a few holes in wrap.', 'Cover'),
         ('Microwave until tender, about 2 minutes.', 'Microwave'),
         ('Drain if necessary.', 'Drain'),
         ('Heat a large drizzle of olive oil in a large pan over medium-high heat '
          '(use a nonstick pan if you have one).', 'Heat'),
         ('Add butternut squash and ¼ tsp sugar.', 'Add'),
         ('Cook, stirring occasionally, until browned and slightly crispy, 2-3 minutes.', 'Cook'),
         ('Add shallot and chopped sage.', 'Add'),
         ('Cook, stirring, until lightly browned, 1-2 minutes.', 'Cook'),
         ('Add a pinch of chili flakes; season with salt.', 'Add'),
         ('Add mushrooms to pan and cook, stirring occasionally, until lightly browned, about 3 minutes.',
          'Add'),
         ('Add garlic and cook until fragrant, about 1 minute.', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Add pasta and 3 TBSP butter to pan; stir until butter has melted.', 'Add'),
         ('Add reserved pasta cooking water and half the Parmesan; stir until thoroughly combined.', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Sprinkle with remaining Parmesan and chili flakes (to taste).', 'Sprinkle')])

    # 67
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Adjust racks to middle and upper position and preheat oven to 400 degrees.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Trim and thinly slice mushrooms.', 'Slice'),
         ('Halve, peel, and finely dice onion.', 'Dice'),
         ('Pick tarragon leaves from stems and roughly chop; discard stems.', 'Pick'),
         ('Cut lemon into wedges.', 'Cut'),
         ('Halve, peel, and quarter shallots, then place on a large piece of aluminum foil and '
          'toss with salt, pepper, 1 TBSP vinegar (we sent more), and a drizzle of olive oil.', 'Toss'),
         ('Wrap and seal foil around shallots to create a packet.', 'Wrap'),
         ('Place on a baking sheet and roast in oven on upper rack until softened, about 25 minutes.', 'Roast'),
         ('Meanwhile, stir together 3 cups water and 2 stock concentrates in a medium bowl.', 'Stir'),
         ('Microwave on high for 1 minute.', 'Microwave'),
         ('Heat a drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add half the onion and all of the rice.', 'Add'),
         ('Cook, stirring, until translucent, 1-2 minutes.', 'Cook'),
         ('Stir stock into pan.', 'Stir'),
         ('Bring to a boil, then lower heat and reduce to a simmer.', 'Simmer'),
         ('Cover pan with a lid or foil and bake in oven on middle rack until rice is al dente, 20-25 minutes.',
             'Bake'),
         ('Once water boils, add gemelli to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, about 11 minutes.', 'Cook'),
         ('Reserve 1 cup pasta water, then drain well.', 'Reserve'),
         ('Heat a drizzle of olive oil in another large pan over medium-high heat.', 'Heat'),
         ('Remove sausage from casings.', 'Remove'),
         ('Add to pan, breaking up meat into pieces.', 'Add'),
         ('Cook until browned and cooked through.', 'Cook'),
         ('Remove from pan and set aside.', 'Remove'),
         ('Heat 1 TBSP butter and another drizzle of olive oil in same pan.', 'Heat'),
         ('Add mushrooms and remaining onion.', 'Add'),
         ('Cook, tossing, until tender and browned, 5-6 minutes.', 'Cook'),
         ('Stir remaining stock concentrate, Â¼ cup pasta water, and a squeeze of lemon juice into pan.', 'Stir'),
         ('Reduce heat to low, then stir in 1 TBSP butter, sour cream, and half the tarragon.', 'Stir'),
         ('Stir in gemelli and half the sausage.', 'Stir'),
         ('Season with plenty of salt and pepper.', 'Season'),
         ('Divide between plates and sprinkle with Â¼ cup Parmesan (1 packet) and remaining '
          'tarragon (to taste), then serve.', 'Sprinkle'),
         ('Stir 2 TBSP butter, shallots, and remaining sausage into rice.', 'Stir'),
         ('Using a peeler, shave zucchini lengthwise into ribbons, rotating until you get to core; discard core.',
          'Shave'),
         ('Stir ribbons into rice.', 'Stir'),
         ('Season with plenty of salt and pepper.', 'Season'),
         ('Divide between reusable plastic containers and pack with remaining Parmesan.', 'Divide')])

    # 68
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Preheat oven to 450 degrees.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Pick and roughly chop 1 tsp rosemary leaves.', 'Pick'),
         ('Pick parsley leaves; discard stems.', 'Pick'),
         ('Roughly chop leaves.', 'Chop'),
         ('Mince or grate garlic.', 'Grate'),
         ('Halve mozzarella; cut one half into two slices (use the rest of the rosemary and cheese as you like).',
          'Halve'),
         ('Pat chicken dry with a paper towel and season all over with salt and pepper; set aside.',
          'Pat'),
         ('Place broccoli on a baking sheet and toss with a drizzle of olive oil.', 'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Roast in oven on top rack until tender and crisped, 12-15 minutes total (we’ll check in before it’s done).',
          'Roast'),
         ('Heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add chicken and cook without disturbing until browned on bottom, 4-5 minutes.',
          'Cook'),
         ('Flip and sprinkle with chopped rosemary and half the garlic.', 'Sprinkle'),
         ('Lay a mozzarella slice on each piece of chicken, followed by a few slices of prosciutto '
          '(you’ll have some left over).', 'Lay'),
         ('Remove broccoli from oven, toss with remaining garlic, and push toward one side of sheet.',
          'Remove'),
         ('Transfer topped chicken to the other side.', 'Transfer'),
         ('Roast in oven until prosciutto is slightly crisp, 7-8 minutes.', 'Roast'),
         ('Once water boils, add fusilli to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Scoop out 1 cup cooking water, then drain.', 'Scoop'),
         ('Add marinara to the same pot and place over medium heat.', 'Add'),
         ('Stir cream cheese into pot with marinara.', 'Stir'),
         ('Gently stir in fusilli, ¼ cup cooking water, half the Parmesan, 1 TBSP butter, '
          'and a pinch of chili flakes (if desired).', 'Stir'),
         ('Stir in more cooking water if very thick.', 'Stir'),
         ('Set aside.', 'Set aside'),
         ('Add stock concentrate and ¼ cup cooking water to the pan used for chicken over medium-high heat.',
          'Add'),
         ('Bring to a simmer and let reduce slightly, 1-2 minutes.', 'Bring'),
         ('Stir in 1 TBSP butter.', 'Stir'),
         ('Remove from heat.', 'Remove'),
         ('Stir half the parsley into sauce in the pan.', 'Stir'),
         ('Season with pepper.', 'Season'),
         ('Divide chicken and broccoli between plates and drizzle pan sauce over chicken.', 'Divide'),
         ('Add pasta to the side and sprinkle with remaining parsley and Parmesan.', 'Add'),
         ('Sprinkle with additional chili flakes for extra heat.', 'Sprinkle')])

    # 69
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Trim and quarter mushrooms, cutting any large pieces into smaller ones.', 'Trim'),
         ('Trim, then thinly slice scallions, separating greens and whites.', 'Trim'),
         ('Heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('In a medium bowl, combine beef, scallion whites, and half the Tuscan Heat Spice.', 'Combine'),
         ('Season with salt and pepper.', 'Season'),
         ('Shape into 8-10 meatballs.', 'Shape'),
         ('Add to pan and cook, turning occasionally, until browned and desired doneness is reached, 5-7 minutes.',
          'Add'),
         ('Remove from pan and set aside on a paper-towel-lined plate.', 'Remove'),
         ('Once water boils, add fusilli to pot.', 'Add'),
         ('Cook until al dente, 9-12 minutes.', 'Cook'),
         ('Scoop out and reserve Â½ cup pasta cooking water, then drain well.', 'Scoop'),
         ('Return pasta to pot along with 1 TBSP butter and toss to melt.', 'Return'),
         ('Season with salt and pepper.', 'Season'),
         ('Heat a large drizzle of olive oil in same pan over medium heat.', 'Heat'),
         ('Add mushrooms and cook, tossing occasionally, until browned and tender, 5-7 minutes.', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('Add spinach and toss until wilted, 2-3 minutes.', 'Add'),
         ('Add garlic and scallion greens and cook until fragrant, 30 seconds to 1 minute.', 'Add'),
         ('Add cream cheese and stir until melted and combined, 1-2 minutes.', 'Add'),
         ('Add cooked pasta, reserved pasta cooking water, and remaining Tuscan Heat Spice to pan.',
          'Add'),
         ('Toss until everything is well coated and a thick sauce has formed, 1-2 minutes.', 'Toss'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide creamy Tuscan beef pasta between plates.', 'Divide'),
         ('Top with meatballs and sprinkle over Parmesan.', 'Sprinkle')])

    # 70
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Preheat oven to 200 degrees.', 'Preheat'),
         ('Zest 1 tsp zest from lemon, then halve.', 'Zest'),
         ('Squeeze 2 TBSP juice into a small bowl.', 'Squeeze'),
         ('Halve shallot.', 'Halve'),
         ('Peel and finely chop one half; save the other half for another use.', 'Chop'),
         ('Thinly slice garlic.', 'Slice'),
         ('Chop parsley.', 'Chop'),
         ('Cut tomato into small cubes.', 'Cut'),
         ('Heat a drizzle of olive oil in a large, preferably nonstick pan over medium heat.', 'Heat'),
         ('Add panko and a pinch of salt.', 'Add'),
         ('Toast, stirring often, until golden brown, about 5 minutes.', 'Toast'),
         ('Remove from pan and set aside on a plate to cool.', 'Remove'),
         ('Heat a large drizzle of olive oil in same pan over medium heat.', 'Heat'),
         ('Add crab cakes and cook until browned on bottom, about 4 minutes.', 'Cook'),
         ('Flip and cook until browned on other side, about 4 minutes more.', 'Cook'),
         ('Transfer crab cakes to a baking sheet and place in oven to keep warm.', 'Transfer'),
         ('Once water boils, add tagliatelle to pot.', 'Add'),
         ('Cook until just tender, about 2 minutes.', 'Cook'),
         ('Scoop out and reserve Â½ cup pasta cooking water, then drain.', 'Scoop'),
         ('Immediately pour reserved cooking water into bowl with reserved 2 TBSP lemon juice.', 'Pour'),
         ('Add 1 tsp flour (we sent more), 1 tsp lemon zest, and stock concentrate.', 'Add'),
         ('Whisk with a fork until smooth.', 'Whisk'),
         ('Stir in capers and their juice.', 'Stir'),
         ('Melt 1 TBSP butter in pan used for crab cakes over medium-high heat.', 'Melt'),
         ('Stir in garlic, chopped shallot, and a pinch of chili flakes (if you like heat).', 'Stir'),
         ('Cook until fragrant, 30 seconds to 1 minute.', 'Cook'),
         ('Pour in pasta water mixture, bring to a boil, and cook until thickened, about 1 minute.', 'Pour'),
         ('Remove pan from heat and stir in another 1 TBSP butter.', 'Stir'),
         ('Gently stir in tagliatelle and half the parsley.', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Place panko, tomato, and remaining parsley in another small bowl.', 'Place'),
         ('Season with salt and pepper.', 'Season'),
         ('Toss to combine.', 'Toss'),
         ('Divide pasta between plates or bowls and top with crab cakes.', 'Divide'),
         ('Scatter tomato mixture over top.', 'Scatter'),
         ('Sprinkle with a drizzle of olive oil and chili flakes to taste.', 'Sprinkle')])

    # 71
    tagged1.append([('Wash and dry all produce.', 'Wash'),
                    ('Trim, peel, and cut carrot into a small dice.', 'Trim'),
                    ('Halve, peel, and finely chop onion.', 'Chop'),
                    ('Dice tomato.', 'Dice'),
                    ('Heat a drizzle of olive oil in a large pot over medium-high heat.', 'Heat'),
                    ('Add sausage* and cook, breaking up meat into pieces, until browned, 4-6 minutes '
                     '(it’ll finish cooking in the next step).', 'Add'),
                    (
                        'Add another drizzle of olive oil to pot with sausage, then stir in carrot, onion, '
                        'and a big pinch of salt.', 'Add'),
                    ('Cook, stirring occasionally, until veggies are just softened and sausage is cooked through,'
                     ' 5-7 minutes.', 'Cook'),
                    ('Add tomato, half the Italian Seasoning (use the rest as you like), and ¼ tsp garlic powder'
                     ' (½ tsp for 4 servings) to pot.', 'Add'),
                    ('Cook, stirring, until fragrant, 1 minute.', 'Cook'),
                    ('Stir in stock concentrates and 3½ cups warm water (6 cups for 4), scraping up any '
                     'browned bits from bottom of pot.', 'Stir'),
                    ('Add half the farfalle (all for 4).', 'Add'),
                    ('Cover and bring to a boil, then immediately reduce heat to low.', 'Cover'),
                    ('Simmer until pasta is al dente, 10 minutes.', 'Simmer'),
                    ('Meanwhile, place 2 TBSP butter (3 TBSP for 4 servings) in a small microwave-safe bowl; '
                     'microwave until just softened, 10 seconds (do not melt).', 'Place'),
                    ('Stir in 1 TBSP Parmesan, ¼ tsp garlic powder (use 2 TBSP Parmesan and remaining garlic '
                     'powder for 4), a pinch of salt, and chili flakes to taste.', 'Stir'),
                    ('Halve ciabatta and toast until golden.', 'Halve'),
                    ('Spread butter mixture onto cut sides, then halve on a diagonal.', 'Spread'),
                    ('Stir spinach and 2 TBSP Parmesan (4 TBSP for 4 servings) into soup until spinach is wilted.',
                     'Stir'),
                    ('Season with plenty of salt and pepper.', 'Season'),
                    (
                    'Divide soup between bowls; sprinkle with remaining Parmesan and a pinch of chili '
                    'flakes if desired.', 'Divide'),
                    ('Serve with toasts on the side for dipping.', 'Serve')])

    # 72
    tagged1.append([
        ('Wash and dry all produce.', 'Wash'),
        ('Bring a large pot of salted water to a boil.', 'Boil'),
        ('Mince or grate garlic.', 'Mince'),
        ('Pick mint leaves from stems; discard stems.', 'Pick'),
        ('Roughly chop leaves.', 'Chop'),
        ('Heat a large, empty pan over medium-low heat.', 'Heat'),
        ('Add pine nuts and toast, tossing frequently, until lightly browned and fragrant, 2-3 minutes.', 'Add'),
        ('Remove from pan and set aside.', 'Remove'),
        ('Once water is boiling, add penne to pot.', 'Add'),
        ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
        ('Carefully scoop out and reserve ⅓ cup pasta cooking water, then drain.', 'Scoop'),
        ('Heat a large drizzle of olive oil in pan used for pine nuts over medium heat.', 'Heat'),
        ('Add half the pancetta from package and cook, tossing, until lightly crisped, 2-3 minutes'
         '(use the rest of the pancetta as you like).', 'Add'),
        ('Add garlic and peas and cook, tossing, until fragrant, about 1 minute.', 'Add'),
        ('Stir penne, sour cream, half the Parmesan, half the truffle zest, stock concentrate, '
         'and reserved pasta cooking water into pan.', 'Stir'),
        ('Gently toss until a thick, creamy sauce forms, 3-4 minutes.', 'Toss'),
        ('Season with salt and pepper.', 'Season'),
        ('Divide penne mixture between plates.', 'Divide'),
        ('Sprinkle with pine nuts and remaining Parmesan, as well as mint and remaining truffle zest to taste.',
         'Sprinkle')])

    # 73
    tagged1.append([
        ('Adjust rack to middle position and preheat oven to 450 degrees.', 'Adjust'),
        ('Bring a large pot of salted water to a boil.', 'Boil'),
        ('Wash and dry all produce.', 'Wash'),
        ('Dice tomato.', 'Dice'),
        ('Dice potatoes into 1-inch pieces.', 'Dice'),
        ('Toss on a baking sheet with a large drizzle of olive oil, salt, and pepper.', 'Toss'),
        ('Roast until lightly browned and tender, about 15 minutes.', 'Roast'),
        ('Meanwhile, pat chicken dry with paper towels; season all over with salt, pepper, and Tuscan Heat Spice.',
         'Pat'),
        ('Heat a large drizzle of olive oil in a large pan over medium-high heat (use a nonstick pan if you have one).',
         'Heat'),
        ('Add chicken and cook until browned and cooked through, 5-6 minutes per side.', 'Cook'),
        ('Turn off heat; transfer to a plate and set aside.', 'Transfer'),
        ('Once potatoes have roasted 15 minutes, remove from oven.', 'Remove'),
        ('Toss with half the Parmesan and push toward one side of sheet.', 'Toss'),
        ('Toss green beans on other side of sheet with a drizzle olive oil, salt, and a pinch of'
         ' chili flakes (use more if you like it spicy).', 'Toss'),
        ('Return to oven and roast until potatoes are very crisp and green beans are tender '
         'and lightly browned, about 10 minutes.', 'Roast'),
        ('Once water boils, add gemelli to pot.', 'Add'),
        ('Cook until al dente, 10-12 minutes.', 'Cook'),
        ('Reserve ¼ cup pasta cooking water, then drain gemelli and return to empty pot.', 'Reserve'),
        ('Meanwhile, add balsamic glaze, stock concentrate, and ⅓ cup plain water to pan used for chicken.', 'Add'),
        ('Simmer over medium-low until thickened, 3-4 minutes.', 'Simmer'),
        ('Turn off heat and stir in 1 TBSP butter.', 'Stir'),
        ('Add 2 chicken breasts to pan and flip to coat in sauce.', 'Add'),
        ('Divide potatoes and green beans between plates.', 'Divide'),
        ('Top with chicken, then drizzle with remaining sauce from pan and serve '
         '(save the remaining ingredients for lunch).', 'Top'),
        ('When ready to prep lunch, add pesto and pasta cooking water to pot with gemelli and toss to coat.', 'Add'),
        ('Stir in tomato.', 'Stir'),
        ('Season with salt and pepper.', 'Season'),
        ('Divide mixture between two reusable containers.', 'Divide'),
        ('Slice remaining chicken and arrange on top of pasta.', 'Slice'),
        ('Sprinkle with remaining Parmesan.', 'Sprinkle'),
        ('Keep refrigerated.', 'Keep'),
        ('Heat in a microwave on high for about 2 minutes before eating.', 'Heat')])

    # 74
    tagged1.append(
        [('Adjust rack to middle position and preheat oven to 400 degrees.', 'Adjust'),
         ('Bring a large pot of salted water to a boil.', 'Bring'),
         ('Wash and dry all produce.', 'Wash'),
         ('Halve bell pepper, then remove and discard stem and seeds.', 'Halve'),
         ('Thinly slice chili, removing seeds for less heat.', 'Slice'),
         ('Remove sausage from casings; discard casings.', 'Remove'),
         (
             'Drizzle bell pepper halves with oil, salt, and pepper; place cut sides down on a lightly oiled baking sheet.',
             'Drizzle'),
         ('Place garlic cloves on a small piece of foil and drizzle with oil, salt, and pepper; '
          'cinch into a packet and place on baking sheet.', 'Place'),
         ('Roast until bell pepper is lightly charred and garlic is softened, 20-25 minutes.', 'Roast'),
         ('Once water is boiling, add cavatappi to pot.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve 1 cup pasta cooking water (2 cups for 4 servings), then drain.', 'Reserve'),
         ('Heat a drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add sausage and cook, breaking up meat into pieces, until browned and cooked through, 6-8 minutes.', 'Add'),
         ('If there’s excess grease in your pan, carefully pour it out.', 'Pour'),
         ('If desired, stir in a pinch of chili; cook until fragrant, 15 seconds.', 'Stir'),
         ('Add tomato paste and Â½ cup reserved pasta cooking water (Â¾ cup for 4 servings).', 'Add'),
         ('Simmer until thickened, 2-3 minutes.', 'Simmer'),
         ('Turn off heat.', 'Turn'),
         ('Transfer roasted bell pepper halves to a cutting board; thinly slice.', 'Transfer'),
         ('Remove roasted garlic cloves from foil; transfer to cutting board and gently mash with a fork.', 'Remove'),
         ('Return pan with sauce to low heat.', 'Return'),
         ('Add mashed garlic and stir to combine.', 'Add'),
         ('Stir in sliced bell pepper, cavatappi, sour cream, 2 TBSP butter (4 TBSP for 4 servings), '
          'and half the Parmesan.', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Sprinkle with remaining Parmesan and, if desired, a pinch of remaining chili.', 'Sprinkle')])

    # 75
    tagged1.append(
        [('Adjust rack to the middle position and preheat oven to 400 degrees.', 'Adjust'),
         ('Bring a large pot of salted water to a boil.', 'Bring'),
         ('Wash and dry all produce.', 'Wash'),
         ('Halve bell peppers, then remove and discard cores and stems.', 'Halve'),
         ('Thinly slice chili.', 'Slice'),
         ('Remove sausage from casings; discard casings.', 'Remove'),
         ('Drizzle pepper halves with oil, salt, and pepper; place cut sides down on a lightly oiled baking sheet.',
          'Drizzle'),
         ('Place whole garlic cloves on a 6-x-6-inch piece of aluminum foil and drizzle with oil, salt, and pepper.',
          'Place'),
         ('Cinch foil to make a closed pouch; place on baking sheet.', 'Cinch'),
         ('Roast until pepper begins to char and garlic is soft, 20-25 minutes.', 'Roast'),
         ('Remove from oven.', 'Remove'),
         ('While veggies roast, add gemelli to boiling water.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve ¾ cup pasta water, then drain.', 'Reserve'),
         ('Heat a large drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add sausage and cook, breaking up meat into pieces, until browned, 6-8 minutes.', 'Add'),
         ('Pour out any excess fat from pan.', 'Pour'),
         ('If desired, stir in a pinch of chili; cook 15 seconds.', 'Stir'),
         ('Add tomato paste and ½ cup reserved pasta cooking water.', 'Add'),
         ('Simmer until thickened, about 2 minutes.', 'Simmer'),
         ('Turn off heat.', 'Turn'),
         ('Transfer roasted bell pepper halves to a cutting board; thinly slice.', 'Transfer'),
         ('Remove roasted garlic cloves from foil; transfer to cutting board and gently smash with a fork.', 'Remove'),
         ('Return pan with sauce to low heat.', 'Return'),
         ('Add garlic and stir to combine.', 'Add'),
         ('Stir in sliced bell pepper, pasta, sour cream, 4 TBSP butter, and half the Parmesan.', 'Stir'),
         ('(TIP: If sauce seems dry, stir in a splash of remaining reserved cooking water.)', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Sprinkle with remaining Parmesan and, if desired, a pinch of remaining chili.', 'Sprinkle')])

    # 76
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Adjust rack to upper position and preheat oven to 425 degrees.', 'Adjust'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Trim ends from zucchini.', 'Trim'),
         ('Halve lengthwise.', 'Halve'),
         ('Slice crosswise into Â¼-inch-thick half-moons.', 'Slice'),
         ('Halve, peel, and thinly slice onion.', 'Slice'),
         ('Cut tomatoes into 1-inch-thick wedges.', 'Cut'),
         ('Mince garlic.', 'Mince'),
         ('Toss zucchini and onion on a baking sheet with half the garlic, Â½ TBSP Tuscan heat '
          'spice (weâ€™ll use more in step 4), a large drizzle of olive oil, and a pinch of salt and pepper.', 'Toss'),
         ('Roast in oven until just softened, about 10 minutes.', 'Roast'),
         ('Remove from oven and carefully push slices toward one side of baking sheet.', 'Push'),
         ('Toss tomatoes, a large drizzle of olive oil, and a pinch of salt and pepper on empty side of baking sheet.',
          'Toss'),
         ('Return to oven and roast until all veggies are browned and tender, 5-7 minutes.', 'Roast'),
         ('Meanwhile, add fusilli to pot of boiling water.', 'Add'),
         ('Cook until al dente, 10-12 minutes.', 'Cook'),
         ('Reserve 1Â½ cups pasta cooking water, then drain and set aside.', 'Reserve'),
         ('Heat a large drizzle of olive oil in pot used for pasta over medium-high heat.', 'Heat'),
         ('Add chicken and season with a pinch of salt and pepper and 1 TBSP Tuscan heat spice '
          '(save the rest for another use).', 'Add'),
         ('Cook, stirring occasionally, until browned and cooked through, about 5 minutes.', 'Cook'),
         ('Add 4 TBSP tomato paste (we sent more) and remaining garlic to pot.', 'Add'),
         ('Cook, stirring occasionally, until fragrant, 1-2 minutes.', 'Cook'),
         ('Stir in cream cheese and 1 cup pasta cooking water.', 'Stir'),
         ('Add fusilli, veggies, half the Parmesan, and 2 TBSP butter.', 'Add'),
         ('Stir until well combined.', 'Stir'),
         ('Remove from heat; season with salt and pepper.', 'Remove'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Sprinkle with remaining Parmesan and serve.', 'Sprinkle')])

    # 77
    tagged1.append(
        [('Preheat oven to 400 degrees.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Wash and dry all produce.', 'Wash'),
         ('Trim and thinly slice scallions, separating whites from greens.', 'Trim'),
         ('Toss cauliflower on a baking sheet with a large drizzle of olive oil and a pinch of salt and pepper.',
          'Toss'),
         ('Roast until tender, 20-25 minutes.', 'Roast'),
         ('Once water is boiling, add cavatappi to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Reserve Â¼ cup pasta cooking water (Â½ cup for 4 servings), then drain.', 'Reserve'),
         ('Meanwhile, heat a large, dry pan over medium-high heat.', 'Heat'),
         ('Add bacon and cook, flipping occasionally, until just crispy, 6-10 minutes.', 'Add'),
         ('Turn off heat.', 'Turn off'),
         ('Transfer bacon to a paper-towel-lined plate.', 'Transfer'),
         ('Discard all but 1 tsp bacon fat (2 tsp for 4 servings) from pan.', 'Discard'),
         ('Melt 1 TBSP butter (2 TBSP for 4 servings) in same pan over medium heat.', 'Melt'),
         ('Add scallion whites and cook until softened, about 1 minute.', 'Add'),
         ('Add flour and stir constantly until lightly browned, 1-2 minutes.', 'Add'),
         ('Slowly whisk in milk, then stock concentrate.', 'Whisk'),
         ('Increase heat to high and let bubble until slightly thickened, 1-2 minutes.', 'Increase'),
         ('Turn off heat, then whisk in cheese.', 'Turn off'),
         ('Season with salt and pepper.', 'Season'),
         ('Using your hands, crumble bacon into small pieces.', 'Crumble'),
         ('Stir bacon, cavatappi, cauliflower, and 2 TBSP reserved pasta cooking water '
          '(â…“ cup for 4 servings) into sauce.', 'Stir'),
         ('TIP: If pasta seems dry, add a few more splashes of reserved cooking water.', 'Add'),
         ('Divide mac â€™nâ€™ cheese between plates.', 'Divide'),
         ('Garnish with scallion greens and serve.', 'Garnish')])

    # 78
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Preheat the oven to 425 degrees.', 'Preheat'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Line up the baby broccoli on your cutting board, and cut into 1-inch pieces.', 'Cut'),
         ('Discard the ends.', 'Discard'),
         ('Roughly chop the garlic.', 'Chop'),
         ('Pick the oregano leaves off the stems.', 'Pick'),
         ('Discard the stems.', 'Discard'),
         ('Cook the sausage:', 'Cook'),
         ('Place the sausage onto a baking sheet.', 'Place'),
         ('Cook in the oven for about 15 minutes.', 'Cook'),
         ('Boil the pasta:', 'Boil'),
         ('Add the pasta to the boiling water.', 'Add'),
         ('Cook 9-11 minutes, until al dente.', 'Cook'),
         ('While the pasta cooks, add the baby broccoli to the same water.', 'Add'),
         ('Cook 3-4 minutes, until tender.', 'Cook'),
         ('Remove the baby broccoli with a slotted spoon and set aside.', 'Remove'),
         ('Meanwhile, place the almonds, oregano leaves, and chopped garlic in a pile on your cutting board.', 'Place'),
         ('Run your knife over the mixture until finely chopped (some larger pieces of nuts can remain).', 'Chop'),
         ('Check on the pasta, drain when ready, then return to the pot.', 'Check'),
         ('Heat two large drizzles of olive oil in a large pan over medium-low heat.', 'Heat'),
         ('Add the gremolata mixture.', 'Add'),
         ('Cook, tossing, for 3-4 minutes, until beginning to turn golden brown.', 'Cook'),
         ('Season generously with salt and pepper.', 'Season'),
         ('Remove pan from heat.', 'Remove'),
         ('Zest about 2 teaspoons lemon directly in the pan, and stir thoroughly to release the lemon oils.', 'Zest'),
         ('Toss and serve:', 'Toss'),
         ('Thinly slice the sausage.', 'Slice'),
         ('Halve the lemons.', 'Halve'),
         ('Toss the sausage, baby broccoli, gremolata, half the Parmesan cheese, and a large '
          'drizzle of olive oil into the pot with the pasta.', 'Toss'),
         ('Reheat over medium heat if necessary.', 'Reheat'),
         ('Season generously with salt and pepper.', 'Season'),
         ('Stir in a few squeezes of lemon, to taste.', 'Stir'),
         ('Divide between bowls, serve with the Parmesan cheese, and enjoy!', 'Divide')])

    # 79
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Quarter zucchini lengthwise, then cut into Â½-inch pieces.', 'Cut'),
         ('Halve, peel, and dice onion.', 'Dice'),
         ('Mince garlic.', 'Mince'),
         ('Strip 2 tsp thyme leaves from stems; discard stems.', 'Discard'),
         ('Roughly chop leaves.', 'Chop'),
         ('Heat a drizzle of olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add beef, breaking up meat into pieces.', 'Add'),
         ('Cook, tossing, until browned but not yet cooked through, 4-5 minutes.', 'Cook'),
         ('Season with salt and pepper.', 'Season'),
         ('Once water is boiling, add spaghetti to pot.', 'Add'),
         ('Cook, stirring occasionally, until al dente, 9-11 minutes.', 'Cook'),
         ('Carefully scoop out and reserve Â½ cup pasta cooking water, then drain.', 'Scoop'),
         ('Add onion and zucchini to pan with beef.', 'Add'),
         ('Cook, tossing, until softened, about 5 minutes.', 'Cook'),
         ('Toss in garlic, thyme, soy sauce, and half the Italian seasoning (use the other half as you like).', 'Toss'),
         ('Cook until fragrant, about 30 seconds.', 'Cook'),
         ('Add tomatoes and reserved pasta cooking water to pan.', 'Add'),
         ('Bring to a boil, then reduce heat and let simmer until thick and saucy, about 5 minutes.', 'Simmer'),
         ('Season with salt and pepper.', 'Season'),
         ('TIP: If you have time, let the ragÃ¹ simmer longer. Itâ€™ll just get better!', 'Simmer'),
         ('Add spaghetti to pan with ragÃ¹ and toss to combine.', 'Add'),
         ('Divide everything between plates, then sprinkle with Parmesan.', 'Divide'),
         ('Drizzle with pepperolio (to tasteâ€”itâ€™s spicy).', 'Drizzle')])

    # 80
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Then add fusilli.', 'Add'),
         ('After about 8 minutes, add broccoli to same pot.', 'Add'),
         ('Cook until florets are tender and pasta is al dente, 2-4 minutes.', 'Cook'),
         ('Scoop out and reserve Â½ cup cooking water, then drain.', 'Scoop'),
         ('Meanwhile, heat a large pan over medium-high heat.', 'Heat'),
         ('Add almonds and stir occasionally until lightly toasted, 2-3 minutes.', 'Add'),
         ('(TIP: Immediately remove pan from heat if almonds start to burn.)', 'Remove'),
         ('Transfer to a plate, then wipe out and set pan aside while you prep.', 'Transfer'),
         ('Finely chop garlic and sun-dried tomatoes.', 'Chop'),
         ('Heat 1 TBSP butter and a drizzle of olive oil in same pan over medium-high heat.', 'Heat'),
         ('Add garlic and a pinch of chili flakes (save the rest for steps 5 and 6).', 'Add'),
         ('Cook, stirring, until fragrant, about 1 minute.', 'Cook'),
         ('Add flour to same pan and stir until lightly toasted, about 30 seconds.', 'Add'),
         ('Stir in sun-dried tomatoes and milk.', 'Stir'),
         ('Season with salt and pepper.', 'Season'),
         ('Bring to a gentle boil, then immediately reduce heat to medium-low.', 'Boil'),
         ('Simmer until slightly thickened, 1-2 minutes.', 'Simmer'),
         ('Meanwhile, pick basil leaves from stems and roughly chop.', 'Pick'),
         ('Add sour cream to pan with sauce and stir until well-combined.', 'Add'),
         ('Stir in fusilli and broccoli.', 'Stir'),
         ('Add just enough pasta water to coat everything in a loose sauce (start with Â¼ cup and add '
          'more from there).', 'Add'),
         ('Season with salt and pepper.', 'Season'),
         ('(TIP: Give the sauce a taste and season with more salt, pepper, or chili flakes as desired).', 'Give'),
         ('Add half the Parmesan and half the basil.', 'Add'),
         ('Stir until everything is well-combined.', 'Stir'),
         ('Divide pasta between bowls.', 'Divide'),
         ('Sprinkle with almonds and remaining Parmesan and basil.', 'Sprinkle'),
         ('Garnish with additional chili flakes to taste.', 'Garnish')])

    # 81
    tagged1.append(
        [('Wash and dry all produce.', 'Wash'),
         ('Bring a large pot of salted water to a boil.', 'Boil'),
         ('Adjust rack to position closest to flame and preheat broiler to high.', 'Adjust'),
         ('Halve, seed, and thinly slice green peppers.', 'Halve'),
         ('Halve, peel, and thinly slice onion.', 'Halve'),
         ('Trim root ends from scallions, leaving shoots whole.', 'Trim'),
         ('Halve and core tomato.', 'Halve'),
         ('Zest ½ tsp zest from lime, then cut into quarters.', 'Zest'),
         ('Once water boils, add fusilli to pot.', 'Add'),
         ('Cook until al dente, 9-11 minutes.', 'Cook'),
         ('Drain and transfer to a large bowl.', 'Transfer'),
         ('Meanwhile, place scallions and tomato halves on a baking sheet and sprinkle with a '
          'drizzle of olive oil, salt, pepper, and ½ tsp Southwest spice (save the rest for later).',
          'Place'),
         ('Arrange tomato halves cut-side down.', 'Arrange'),
         ('Broil until tomato skins crack and scallions soften and are lightly charred, 3-4 minutes.', 'Broil'),
         ('Transfer to a cutting board to cool.', 'Transfer'),
         ('Meanwhile, mix together sour cream, 2 TBSP water, lime zest, and a pinch of salt in a small bowl.', 'Mix'),
         ('Chop broiled tomato and scallions and place in a separate medium bowl.', 'Chop'),
         ('Squeeze in juice from one lime quarter and season with a pinch of salt.', 'Squeeze'),
         ('Set aside.', 'Set'),
         ('Heat 1 TBSP olive oil in a large pan over medium-high heat.', 'Heat'),
         ('Add sausage, breaking it up into pieces.', 'Add'),
         ('Cook 1 minute.', 'Cook'),
         ('Add green peppers and onion to pan.', 'Add'),
         ('Cook, stirring, until sausage is cooked through and veggies soften, 8-9 minutes more.', 'Cook'),
         ('Transfer half the sausage and veggies to bowl with fusilli and set aside.', 'Transfer'),
         ('Add chili powder and remaining Southwest spice to sausage and veggies in pan.', 'Add'),
         ('Cook, stirring, until well combined, about 1 minute.', 'Cook'),
         ('Remove from heat.', 'Remove'),
         ('Stir pesto into fusilli mixture in bowl, then divide between two reusable containers.', 'Stir'),
         ('Sprinkle with Parmesan and set aside to cool.', 'Sprinkle'),
         ('Fill tortillas with sausage mixture.', 'Fill'),
         ('Top with pepper jack cheese, crema, and salsa.', 'Top'),
         ('Serve with remaining lime quarters and hot sauce for drizzling over.', 'Serve'),
         ('Once pasta has cooled, put lids on containers and store in fridge overnight.', 'Store'),
         ('When ready to eat for lunch, enjoy at room temperature or warmed in microwave.', 'Enjoy')])


def createFrequencyDists():
    l = []
    for list_ in tagged1:
        for pair in list_:
            regex = r"[a-zA-Z0-9_\/\’]+"  # splits string into individual words, removes commas and parenthesis
            tokens = regexp_tokenize(pair[0], pattern=regex)
            if (pair[1] == 'a'):
                print("PROBLEM " + pair)
                print(pair.index)
            freqDistWithLabel = (FreqDist(tokens), pair[1])
            freqDistsWithTag.append(freqDistWithLabel)
            l.append(pair[1])
    print(set(l))

def split_train_and_test(dataset, percentage=0.9):
    index = int(len(dataset) * percentage)
    training = dataset[0:index:1]
    test = dataset[index:len(dataset):1]
    return (training, test)


def createClassifier(training):
    classifier = NaiveBayesClassifier.train(training)
    print(classifier.labels())
    print(classifier.most_informative_features(10))
    return classifier


def main():
    # Use a breakpoint in the code line below to debug your script.
    tagInstructions()
    createFrequencyDists()
    training = split_train_and_test(freqDistsWithTag)[0]
    test = split_train_and_test(freqDistsWithTag)[1]
    classifier = createClassifier(training)
    correct = 0
    false = 0
    for query in test:
        if classifier.classify(query[0]) != query[1]:  # prints labels that were classified incorrectly
            print(query[1])
            print("guessed " + classifier.classify(query[0]))
            false += 1
        else:
            correct += 1

    print("Accuracy: " + str(correct / (correct + false)))


if __name__ == '__main__':
    main()
