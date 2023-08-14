import requests
from bs4 import BeautifulSoup

def extract_article_text(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for unsuccessful responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        article_text = ""
        paragraphs = soup.find_all('p', class_='css-1g9td1c')
        for paragraph in paragraphs:
            article_text += paragraph.get_text() + "\n"
        
        return article_text
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

def save_text_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    base_url = "https://www.nytimes.com/"
    article_text = extract_article_text(base_url)
    
    if article_text:
        save_text_to_file(article_text, "nytimes_article.txt")
        print("Article text has been saved to 'nytimes_article.txt'.")
    else:
        print("Failed to retrieve article text.")

if __name__ == "__main__":
    main()
