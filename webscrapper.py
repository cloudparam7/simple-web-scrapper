import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Scraping all the links from the page
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))
        
        # You can extend this to scrape other information as needed
        
    else:
        print("Failed to retrieve the webpage.")

# Example usage
url = "https://www.expample.com/"
simple_web_scraper(url)
