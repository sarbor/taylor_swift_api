import requests
from bs4 import BeautifulSoup

# Define the headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def find_lyrics_source(artist_name):
    search_url = f"https://www.google.com/search?q={artist_name.replace(' ', '+')}+lyrics+site:genius.com"
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Look for the first search result link
        link = soup.find('a', href=True)
        if link:
            return link['href']
    return None

# Replace 'Taylor Swift' with the actual artist name you are searching for
artist_name = 'Taylor Swift'
lyrics_source_url = find_lyrics_source(artist_name)

if lyrics_source_url:
    print(f"Found lyrics source: {lyrics_source_url}")
else:
    print("No lyrics source found.")
