from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By
from articleExtractor import articleExtractor
import pandas as pd
import time

# We can retry loading each article multiple times if Politico is slow or blocks us.
MAX_RETRIES = 3

# 1. Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Give each page up to 120 seconds to fully load
    driver.set_page_load_timeout(120)

    # 2. Go to Politico homepage
    driver.get("https://www.politico.com/")
    time.sleep(3)  # Give the homepage a moment to load

    # 3. Scrape headlines and links
    elements = driver.find_elements(By.CSS_SELECTOR, "h3 a")
    headlines = []
    links = []

    for elem in elements:
        headline_text = elem.text.strip()
        link_url = elem.get_attribute("href")

        if headline_text and link_url:
            headlines.append(headline_text)
            links.append(link_url)

    # 4. Create a DataFrame with the headlines and links
    df = pd.DataFrame({
        "Headlines": headlines,
        "Article Links": links
    })
    # articles = []
    # for link in df["Article Links"]:
    #     article_text = None

    #     for attempt in range(MAX_RETRIES):
    #         try:
    #             # Load the article and extract text
    #             article_text = articleExtractor(driver, link)
    #             # If it succeeds, break out of the retry loop
    #             break
    #         except Exception as e:
    #             if attempt < MAX_RETRIES - 1:
    #                 # Wait 5 seconds before retrying
    #                 time.sleep(5)
    #             else:
    #                 # If all retries fail, store the error message
    #                 article_text = f"Error after {MAX_RETRIES} attempts: {e}"

    #     articles.append(article_text)

    #     time.sleep(5)

   
    # df["Article Text"] = articles


    print(df)

finally:
    # 8. Close the browser
    driver.quit()
