import requests
from bs4 import BeautifulSoup
from time import sleep

def scrape(url, text, want_status):

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        links = soup.find_all('a')

        for link in links:
            href = link.get('href')
            href_tags = soup.find_all(href=True)
            for tag in href_tags:
                print(tag['href'])
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    if text.lower() in (soup.get_text()).lower():
                        print(f"{text} found in {url}")
                    else:
                        print(f"{text} not found in {url}")
                else:
                    if want_status:
                        print(f"Failed to crawl {url}. Status code: {response.status_code}")
                    print(f"Failed to crawl {url}")
                scrape(tag['href'], text)
                print(scrape(tag['href'], text, False))
                sleep(1)

    else:
        return (f"Failed to crawl {url}. Status code: {response.status_code}")
url = input("Enter a URL: ")
text = input("Enter a word to search for: ")
want_status = input("Do you want to see status codes? (y/n): ")
flag = want_status.lower() == 'y'
scrape('https://www.google.com', text, flag)
