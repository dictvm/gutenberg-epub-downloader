#!/usr/bin/env python3

import os
import time
import re
from bs4 import BeautifulSoup
import requests
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def get_third_param(url):
    return url.split('/')[2]

def filter_invalid_urls(urls, invalid_patterns):
    return [url for url in urls if not any(re.search(pattern, url) for pattern in invalid_patterns)]

books_url = os.environ["BOOKS_URL","https://www.projekt-gutenberg.org/info/texte/allworka.html"]
response = requests.get(books_url)

soup = BeautifulSoup(response.text, "html.parser")
urls = [urllib.parse.urljoin(books_url, link["href"]) for link in soup.find_all("a", href=True)]
sorted_urls = sorted(urls, key=get_third_param)

invalid_patterns = [r"abc\.de", r"lesetipps", r"info/texte", r"@",r"autoren/info",r"index.html"]
filtered_urls = filter_invalid_urls(sorted_urls, invalid_patterns)

webdriver_service = Service(os.environ.get("CHROMEDRIVER_PATH", "./chromedriver"))

for book_url in filtered_urls:
    epub2go_url = f"http://www.epub2go.eu/?t={book_url}"
    print(f"Processing {epub2go_url}")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = os.environ.get("CHROMIUM_PATH", "/usr/bin/google-chrome")

    driver = webdriver.Chrome(service=webdriver_service, options=options)
    driver.get(epub2go_url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'download') and contains(@href, '.epub')]"))
        )
        epub_url = element.get_attribute("href")
        epub_filename = urllib.parse.unquote(epub_url.split("=")[-1])
        print(f"Found EPUB: {epub_filename}")
        print(f"Downloading...")
        with requests.get(epub_url, stream=True) as r:
            r.raise_for_status()
            with open(epub_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Downloaded {epub_filename}")
    except Exception as e:
        print(f"Error processing {epub2go_url}: {e}")
    finally:
        driver.quit()

    time.sleep(0.5)  # Wait half a second before processing the next URL
