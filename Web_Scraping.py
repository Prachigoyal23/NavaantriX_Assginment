import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    url = f"https://www.amazon.com/s?k={query}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.select('.s-main-slot .s-result-item'):
        title = item.h2.text if item.h2 else 'N/A'
        price = item.select_one('.a-price .a-offscreen').text if item.select_one('.a-price .a-offscreen') else 'N/A'
        rating = item.select_one('.a-icon-alt').text if item.select_one('.a-icon-alt') else 'N/A'
        products.append({'Name': title, 'Price': price, 'Rating': rating})

    return products

def scrape_flipkart(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    url = f"https://www.flipkart.com/search?q={query}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.select('._1AtVbE'):
        title = item.select_one('._4rR01T').text if item.select_one('._4rR01T') else 'N/A'
        price = item.select_one('._30jeq3').text if item.select_one('._30jeq3') else 'N/A'
        rating = item.select_one('._3LWZlK').text if item.select_one('._3LWZlK') else 'N/A'
        products.append({'Name': title, 'Price': price, 'Rating': rating})

    return products

def save_to_excel(products, filename='products.xlsx'):
    df = pd.DataFrame(products)
    df.to_excel(filename, index=False)

def main():
    query = input("Enter the product to search: ")
    amazon_products = scrape_amazon(query)
    flipkart_products = scrape_flipkart(query)

    all_products = amazon_products + flipkart_products
    save_to_excel(all_products)

    print(f"Scraped {len(all_products)} products and saved to 'products.xlsx'.")

if __name__ == "__main__":
    main()
