# Importing the necessary libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

#  Initialize empty lists to store the scraped data
Brand_Name = []
Price = []
Rating = []
Rating_count = []
review_count = []
Ranking = []
URL = []

# Loop through pages 2 to 11 of the Flipkart search results
for i in range(2, 12):
 url = "https://www.flipkart.com/search?q=Mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
r = requests.get(url)
#print(r)

 # Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(r.text, "lxml")
box = soup.find("div", class_="DOjaWF gdgoEp")

# Find the main container for the product listings
names = box.find_all("div", class_="KzDlHZ")

 # Extract product names
for item in names:
 name = item.text
Brand_Name.append(name) # Append the product name to the list
print(Brand_Name)

# IF want to extract the only fiest name of Brand (Uncomment the code while using)
#def extract_first_name(Brand_Name):
 #   words = Brand_Name.split()
  #  return words[0]
#for item in Brand_Name:
 #   name= item.text
  #  Brand_Name.append(name)
   # print(Brand_Name)


# Extract product prices
Prices = box.find_all("div", class_="Nx9bqj _4b5DiR")

for item in Prices:
 name = item.text
Price.append(name)
print(Price)

# Extract Product Rating
Ratings = box.find_all("div", class_="XQDdHH")

for item in Ratings:
 name = item.text
Rating.append(name)
print(Rating)

# Extract Rating Count and Review Count
RatingAndReview = box.find_all("span", class_="Wphh3N")
for item in RatingAndReview:
 name = item.text
 Rating_count.append(name)
 print(Rating_count)

# Extract URLs of the products
Url = box.find_all("a", class_ ="CGtC98")
for item in Url:
            name = item.get("href")
            URL.append("https://www.flipkart.com" + name)


# Create a DataFrame with the extracted data
df = pd.DataFrame({
    "Brand Name": Brand_Name,
    "Price": Price,
    "Rating": Rating,
    "Rating Count": Rating_count,
    "URL": URL
})

# Save the DataFrame to an Excel file
df.to_excel("D:/Mobile_Data/mobile_under_50000.xlsx", index=False)  # Save the DataFrame to an Excel file
