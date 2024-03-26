from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import urllib.parse


def get_random_page_urls(driver, languages):
    base_url = 'https://{lang}.wikipedia.org/wiki/Special:Random'
    urls = []
    while len(urls) < 15:
        for lang in languages:
            driver.get(base_url.format(lang=lang))
            urls.append(driver.current_url)
    return urls


def get_urls(driver, base_url):
    driver.get(base_url)
    # Attendre que les liens interlangues soient chargés
    wait = WebDriverWait(driver, 20)

    urls = {}
    try :
        interlanguage_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.interlanguage-link a')))
        urls = {link.get_attribute('lang'): link.get_attribute('href') for link in interlanguage_links}

    except TimeoutException:
        print(f"Could not find interlanguage links for {base_url}")
    # print(urls)
    return urls

def extract_first_paragraph(driver, url):
    driver.get(url)
    
    paragraph = None

    # Extrait le premier paragraphe
    try:
        elements = driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div/p')
        if elements:
            if elements[0] == "":
                paragraph = elements[1].text + "\n" + elements[2].text
            else:
                paragraph = elements[0].text + "\n" + elements[1].text
    except:
        print(f"Could not find paragraph for {url}")

    return paragraph


def write_txt(data_folder, lang, url, paragraph):
    # Parse the URL to extract the article title, which is the part after the last '/'
    parsed_url = urllib.parse.urlparse(url)
    article_title = os.path.basename(parsed_url.path)
    
    # URL decode the article title (e.g., replace '%E1%83%90' with actual characters)
    article_title = urllib.parse.unquote(article_title)
    
    # Replace any remaining invalid file name characters (like '/') in the title with '_'
    valid_article_title = ''.join(char if char.isalnum() else '_' for char in article_title)
    
    # Ensure the data folder exists
    os.makedirs(data_folder, exist_ok=True)
    
    # Generate the filename and write the paragraph to the file
    filename = f"{valid_article_title}_{lang}.txt"
    file_path = os.path.join(data_folder, filename)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(paragraph)


def main():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('detach', True)

    driver = webdriver.Chrome()
    
    data_folder = "./data/raw/"
    languages = ['ar', 'fr', 'en', 'de', 'es', 'ja', 'ko', 'ru', 'zh']
    base_urls = get_random_page_urls(driver, languages)

    # Boucle sur les URLs de base
    for base_url in base_urls:
        urls = get_urls(driver, base_url)
        
        # Filter the URLs for the desired languages
        filtered_urls = {lang: urls[lang] for lang in languages if lang in urls}
        
        for lang, url in filtered_urls.items():
            paragraph = extract_first_paragraph(driver, url)
            print(f"Langue: {lang}\nParagraph: {paragraph}\n")
            
            # Write the results to text files
            if paragraph:
                write_txt(data_folder, lang, url, paragraph)

    driver.quit()

if __name__ == "__main__":
    main()
