import requests
from lxml import html


class NBANewsFetcher:
    def __init__(self, url):
        self.base_url = url

    @staticmethod
    def get_news_content(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            tree = html.fromstring(response.content)

            title_xpath = '//h1[@class="story_art_title"]//text()'
            author_xpath = '//div[@id="shareBar"]/div[2]/div/text()'
            date_xpath = '//div[@class="shareBar__info--author"]/span//text()'
            content_xpath = '//div[@id="story_body_content"]//p//text()'

            title = tree.xpath(title_xpath)
            author = tree.xpath(author_xpath)
            date = tree.xpath(date_xpath)
            content = tree.xpath(content_xpath)

            return {
                'title': title[0].strip() if title else 'Missing',
                'author': author[0].strip() if author else 'Missing',
                'date': date[0].strip() if date else None,
                'content': '\n'.join([para.strip() for para in content if para.strip()])
            }

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_latest_news_list(self, xpath_exp, num_news=10):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()

            tree = html.fromstring(response.content)
            news_container = tree.xpath(xpath_exp)

            if not news_container:
                print(f"No element found with the provided XPath expression.")
                return None

            news_elements = news_container[0].xpath('.//a')

            news_list = []
            for element in news_elements[:num_news]:
                result = element.values()
                title = result[1]
                link = result[0]
                news_list.append({
                    'title': title,
                    'link': link
                })

            return news_list

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
