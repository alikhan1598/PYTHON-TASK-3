import requests
from bs4 import BeautifulSoup

# Website to scrape
url = 'https://news.ycombinator.com/'

# Get webpage content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find headlines
headlines = soup.find_all('a')

# Save text content from links
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for tag in headlines:
        text = tag.get_text(strip=True)
        if text and len(text.split()) > 3:
            file.write(text + '\n')

print(f"{len(headlines)} headlines saved to headlines.txt")
