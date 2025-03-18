from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def articleExtractor(driver, link):
    """
    Loads the given link in the existing driver, waits for the article
    paragraphs to appear, then returns the combined text.
    """

    # 1) Load the page
    driver.get(link)

    # 2) Wait up to 40 seconds for paragraphs to appear
    WebDriverWait(driver, 40).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.story-text p.story-text__paragraph")
        )
    )

    # 3) Find the paragraphs
    elements = driver.find_elements(By.CSS_SELECTOR, "div.story-text p.story-text__paragraph")

    # 4) Concatenate them into a single string
    article_text = " ".join(elem.text for elem in elements).strip()

    return article_text
