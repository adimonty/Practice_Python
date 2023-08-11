import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
ttl_lst = []

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find titles under both h2 and span tags with specific classes
titles_h2 = soup.find_all('h2', class_='story-heading')
titles_span = soup.find_all('span', class_='css-xxaj7r')

# Extract text from h2 and span titles
for title in titles_h2:
    ttl_lst.append(title.get_text(strip=True))
for title in titles_span:
    ttl_lst.append(title.get_text(strip=True))

for title in ttl_lst:
    print(title)