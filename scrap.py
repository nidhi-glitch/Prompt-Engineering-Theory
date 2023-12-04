import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://books.toscrape.com/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the HTML
    # For example, let's extract the titles of all books on the first page
    book_titles = []
    for book in soup.find_all('h3'):
        book_titles.append(book.a.attrs['title'])

    # Print the book titles
    for title in book_titles:
        print(title)
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
