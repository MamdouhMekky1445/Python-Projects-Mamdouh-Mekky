## first you have to run this code in the cmd ###################
###### pip install beautifulsoup4 requests pandas  ######
#################################################################
######## I put the data in Excel sheet as an output #############
#################################################################


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to extract the title and rating of a single book from a BeautifulSoup object
def get_book_info(book):
    # Extract the book title
    title = book.find('h3').find('a')['title']
    # Extract the book rating by getting the second class (which indicates the rating)
    rating = book.find('p', class_='star-rating')['class'][1]
    # Return a dictionary containing the title and rating
    return {'title': title, 'rating': rating}

# Function to scrape book information from a given page URL
def scrape_books(url):
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code != 200:
        # If the request was unsuccessful, return an empty list
        return []
    
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all book elements on the page
    books = soup.find_all('article', class_='product_pod')
    # Extract and return book information for each book found on the page
    return [get_book_info(book) for book in books]

# Function to scrape book information from all pages of the website
def scrape_all_books():
    # Base URL for the paginated book listings
    base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
    # Initialize an empty list to store information about all books
    all_books = []
    
    # Iterate over all 50 pages (assuming there are 50 pages)
    for page_num in range(1, 51):
        # Format the URL for the current page number
        url = base_url.format(page_num)
        # Scrape book information from the current page
        books = scrape_books(url)
        # Check if no books were found (this could indicate the end of the pages)
        if not books:
            # If no books were found, exit the loop
            break
        # Extend the list of all books with the books found on the current page
        all_books.extend(books)
        
    # Return the list of all books
    return all_books

# Function to save the scraped book information to an Excel file
def save_to_excel(books, filename):
    # Convert the list of book dictionaries to a pandas DataFrame
    df = pd.DataFrame(books)
    # Save the DataFrame to an Excel file with the specified filename
    df.to_excel(filename, index=False)

if __name__ == "__main__":
    # Scrape all book information from the website
    books = scrape_all_books()
    # Save the scraped book information to an Excel file named 'books.xlsx'
    save_to_excel(books, 'books.xlsx')
    # Print a message indicating that the scraping is complete and the data is saved
    print("Scraping completed and data saved to books.xlsx")
