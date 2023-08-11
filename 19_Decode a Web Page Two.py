import requests
from bs4 import BeautifulSoup

def extract_article_text(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for unsuccessful responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        article_text = ""
        all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p")
        for elem in all_p_cn_text_body[7:]:
            article_text += elem.text + "\n"
        
        return article_text
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

def main():
    base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    article_text = extract_article_text(base_url)
    
    if article_text:
        print(article_text)
    else:
        print("Failed to retrieve article text.")

if __name__ == "__main__":
    main()
