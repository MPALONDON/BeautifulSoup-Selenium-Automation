import requests
from bs4 import BeautifulSoup


base_url = "https://books.toscrape.com/"
response = requests.get(base_url)
response.encoding = 'utf-8'

data = response.text
soup = BeautifulSoup(data, "html.parser")

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
        price = article.select_one(".price_color").get_text()
        rating = article.select_one("p.star-rating")["class"][1]
        stock = article.select_one(".instock").get_text().strip()

        all_books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "stock": stock
        })

print(all_books)
