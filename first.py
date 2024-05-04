import requests
from bs4 import BeautifulSoup

def fetch_novel_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the title
        title_element = soup.find('h3', class_='chapter-title')
        title = title_element.text.strip() if title_element else None
        
        # Find the content
        content_element = soup.find('div', class_='chapter-c')
        content = content_element.text.strip() if content_element else None
        
        return title, content
    else:
        print("Failed to fetch data from", url)
        return None, None

def main():
    novel_url = 'https://readnovelfull.vip/library-of-heavens-path/chapter-1-swindler/'
    chapter_title, chapter_content = fetch_novel_data(novel_url)
    if chapter_title and chapter_content:
        print("Chapter Title:", chapter_title)
        print("Chapter Content:", chapter_content)
    else:
        print("No data fetched. Check your URL or internet connection.")

if __name__ == "__main__":
    main()
