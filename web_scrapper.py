import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"  # A test website for web scraping
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

products = []
for item in soup.select(".product-item"):  # Replace with actual class name
    name = item.select_one(".product-title").text.strip()
    price = item.select_one(".product-price").text.strip()
    rating = item.select_one(".product-rating").text.strip() if item.select_one(".product-rating") else "No rating"
    products.append([name, price, rating])

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Rating"])
    writer.writerows(products)

print("Data scraped and saved to products.csv!")
