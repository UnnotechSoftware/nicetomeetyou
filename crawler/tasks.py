from celery.utils.log import get_task_logger
from crawler import app
import requests
from bs4 import BeautifulSoup
import json
from pprint import pformat


logger = get_task_logger(__name__)


@app.task
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


@app.task
def get_timelines_info(url: str) -> dict:
    news: dict = dict()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    content = soup.find("script", type='application/ld+json')
    string = _clean_dirty_json(string=content.text)
    info = json.loads(string)[0]
    news['story_id'] = float('.'.join(info['url'].split('/')[-2:]))
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


@app.task
def process():
    ip_addr = '127.0.0.1:8000'
    urls = get_news_urls()
    for title, url in urls.items():
        logger.info(f'>>> title: {title} <<<')
        logger.info(f'>>> url: url <<<')
        news = get_timelines_info(url=url)
        logger.info(pformat(news))
        headers = {'Content-Type': 'application/json'}
        url_news = "http://{}/api/news/".format(ip_addr)
        res = requests.post(url=url_news, data=json.dumps(news), headers=headers)
        if res.status_code == 201:
            logger.info('Successfully send the data to server.')
        else:
            logger.warning(f'Fail to send the data to server. Error status code: {res.status_code}')
