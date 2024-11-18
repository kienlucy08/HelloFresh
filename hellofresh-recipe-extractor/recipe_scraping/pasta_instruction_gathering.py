"""Module: pasta_instruction_gathering.py"""
from recipe_scrapers import scrape_me
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def get_children_links(link):
    """Get children links from link using selenium"""
    children_links = []
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    driver.maximize_window()
    scroll_pause_time = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    recipe_cards = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-test-id='recipe-image-card']"))
    )

    for card in recipe_cards:
        recipe_link = card.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        children_links.append(recipe_link)

    driver.quit()
    return children_links


def trim_links(links):
    """Trim links to only include pasta recipes"""
    # from testing this would return an extra 5 links that were not pasta recipies:
    # /recipes/ingredients, /recipes/meals, /recipes/one-pot-pan-meals, /recipes/difficulty
    # recipes/dietary-lifestyles

    # remove half, since the list is doubled
    for i in range(len(links) // 2):
        links.pop()

    return links


def make_data_frame():
    """Make data frame for the recipies"""
    # should have a list of recipes
    # columns should be link, name of recipe, ingredients, instructions
    # should just return a data frame with these columns
    return pd.DataFrame(columns=['link', 'name', 'ingredients', 'instructions'])


def get_recipe_name(link):
    """Get recipe name from link"""
    scraper = scrape_me(link)
    return scraper.title()


def get_ingredients(link):
    """Get ingredients from link"""
    scraper = scrape_me(link)
    return scraper.ingredients()


def get_instructions(link):
    """Get instructions from link"""
    scraper = scrape_me(link)
    return scraper.instructions_list()


def process_links(links):
    """Process links to get the data frame"""
    data_frame = make_data_frame()
    for link in links:
        recipe_name = get_recipe_name(link)
        print('scraping recipe: ' + recipe_name)
        ingredients = get_ingredients(link)
        instructions = get_instructions(link)
        data_frame = data_frame._append(
            {'link': link, 'name': recipe_name, 'ingredients': ingredients, 'instructions': instructions},
            ignore_index=True)
        print('done scraping recipe: ' + recipe_name)
    return data_frame


def write_to_csv(data_frame, file_name):
    """Write data frame to csv"""
    data_frame.to_csv(file_name, index=False)


def append_to_file(file_name, text):
    """Append text to a file"""
    str_text = str(text)
    with open(file_name, "a") as file:
        file.write(str_text)
        file.write('\n')


if __name__ == '__main__':
    """Main function"""
    starting_link = 'https://www.hellofresh.com/recipes/pasta-recipes/popular?page=8'
    # link directing to the hello fresh website for pasta recipes
    links = get_children_links(starting_link)
    links = trim_links(links)
    data_frame = process_links(links)
    print(data_frame)
    write_to_csv(data_frame, 'scraped_pasta_recipes.csv')
