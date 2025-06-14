import requests
from bs4 import BeautifulSoup

def fetch_trends():
    url = "https://www.vogue.com/fashion-shows"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = [h.text for h in soup.find_all("h2")[:5]]
    return titles