import requests
from bs4 import BeautifulSoup
import json


def get_news_urls() -> dict:
    result: dict[str, str] = dict()
    url = 'https://tw-nba.udn.com/nba/index'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    # Find the breaking news section
    breaking_news_section = soup.find("div", class_="splide__track")
    a_tags = breaking_news_section.find_all('a')
    for a_tag in a_tags:
        result[a_tag['title']] = a_tag['href']

    return result


def _clean_dirty_json(string: str) -> str:
    """Make the string could be loaded by json.loads."""
    with open('post_data.json', 'w') as f:
        f.write(string)
    with open('post_data.json', 'r') as f:
        lines = f.readlines()
        string = ''.join(lines)
        string = string.replace('\n', '')
    return string


def get_timelines_info(url: str):
    news: dict = dict()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    content = soup.find("script", type='application/ld+json')
    string = _clean_dirty_json(string=content.text)
    info = json.loads(string)[0]
    news['headline'] = info['headline']
    news['image'] = info['thumbnailUrl']
    news['date_published'] = info['datePublished']
    news['date_modified'] = info['dateModified']
    news['author'] = info['author']['name']
    news['publisher'] = info['publisher']['name']
    for s in soup.select("div[id='story_body_content'] span p"):
        line = s.text
        if not line:
            continue
        news['context'] = news.get('context', '') + line

    return news


def main():
    urls = get_news_urls()
    for title, url in urls.items():
        print(title, url)
        news = get_timelines_info(url=url)
        print(news)


if __name__ == '__main__':
    main()
