import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = [h.text for h in soup.find_all('h2', class_='headline')]
    return headlines

# Example usage
headlines = fetch_headlines("https://news.ycombinator.com/")
print("\n".join(headlines))