import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from plotting import create_graph

base_url = "https://books.toscrape.com/"
response = requests.get(base_url)
response.encoding = 'utf-8'

data = response.text
soup = BeautifulSoup(data,"html.parser")

num_pages = int(input("How many pages do you want to scrape? "))

all_books = []

for i in range(1, num_pages+1):
    page_url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(page_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.select("article.product_pod")
    for article in articles:
        title = article.select_one("h3 a")["title"]
        url = f"{base_url}catalogue/{article.select_one("h3 a")["href"]}"
        price = article.select_one(".price_color").get_text()
        rating = article.select_one("p.star-rating")["class"][1]
        stock = article.select_one(".instock").get_text().strip()

        all_books.append({
            "title": title,
            "url": url,
            "price": price,
            "rating/5": rating,
            "stock": stock
        })

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for _ in range(len(all_books)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdv5b0saNk_Oa7J2s5599I6Oa-PYXgqkz9SNdDWMJD2A-0btg/viewform?usp=header")
    time.sleep(2)

    book_title = driver.find_element(by=By.CSS_SELECTOR, value = "input[aria-labelledby='i1 i4']")

    book_url = driver.find_element(by=By.CSS_SELECTOR, value = "input[aria-labelledby='i6 i9']")

    book_price = driver.find_element(by=By.CSS_SELECTOR, value = "input[aria-labelledby='i11 i14']")

    book_rating = driver.find_element(by=By.CSS_SELECTOR, value = "input[aria-labelledby='i16 i19']")

    book_stock = driver.find_element(by=By.CSS_SELECTOR, value = "input[aria-labelledby='i21 i24']")

    submit_button = driver.find_element(by=By.XPATH, value = "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    book_title.send_keys(all_books[_]["title"])
    book_url.send_keys(all_books[_]["url"])
    book_price.send_keys(all_books[_]["price"])
    book_rating.send_keys(all_books[_]["rating"])
    book_stock.send_keys(all_books[_]["stock"])
    submit_button.click()

create_graph(all_books)
