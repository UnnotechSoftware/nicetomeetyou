"""
他是test_開頭，但是，不是單元測試
是我訪問 `https://tw-nba.udn.com/nba/index` 解析資料的測試
下面附上測試結果
All Records
Title: 落後20分大逆轉 灰狼淘汰衛冕軍殺進西決
Link: https://tw-nba.udn.com/nba/story/7002/7975352?from=udn_ch2000_menu_v2_main_index

Title: 幫康利搶七開湖？愛德華：我只想為自己贏
Link: https://tw-nba.udn.com/nba/story/7002/7973676?from=udn_ch2000_menu_v2_main_index

Title: 穆雷搶七求勝若渴 主帥：就像兩天沒進食
Link: https://tw-nba.udn.com/nba/story/7002/7973628?from=udn_ch2000_menu_v2_main_index

Title: 布朗森驟死戰傷退 溜馬連趕2戰淘汰尼克
Link: https://tw-nba.udn.com/nba/story/7002/7974996?from=udn_ch2000_menu_v2_main_index

Title: 華盛頓關鍵罰球建功 獨行俠逆轉雷霆晉級
Link: https://tw-nba.udn.com/nba/story/7002/7973711?from=udn_ch2000_menu_v2_main_index

Title: 季後賽關門戰14勝0敗 厄文續寫不敗傳說
Link: https://tw-nba.udn.com/nba/story/7002/7973848?from=udn_ch2000_menu_v2_main_index

Title: 重返西決 唐西奇：陣容才打5個月我們會更好
Link: https://tw-nba.udn.com/nba/story/7002/7973928?from=udn_ch2000_menu_v2_main_index

Title: 關鍵犯規變戰犯 亞歷山大：真希望時間倒流
Link: https://tw-nba.udn.com/nba/story/7002/7973964?from=udn_ch2000_menu_v2_main_index

Title: 神選菜鳥狂寫紀錄 唐西奇：沒他贏不了雷霆
Link: https://tw-nba.udn.com/nba/story/7002/7974049?from=udn_ch2000_menu_v2_main_index

Title: 東冠前兩戰繼續缺陣 波爾辛吉斯回歸倒數
Link: https://tw-nba.udn.com/nba/story/7002/7973561?from=udn_ch2000_menu_v2_main_index
"""

import requests
from lxml import html


class NBANewsFetcher:
    def __init__(self, url):
        self.base_url = url

    @staticmethod
    def get_news_content(self, url):
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
                'title': title[0].strip() if title else None,
                'author': author[0].strip() if author else None,
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


# Example usage:
if __name__ == "__main__":
    base_url = "https://tw-nba.udn.com/nba/index"
    xpath_expression = '//div[@id="focus"]'
    news_fetcher = NBANewsFetcher(base_url)
    latest_news = news_fetcher.get_latest_news_list(xpath_expression)
    if latest_news:
        print("All Records")
        for news in latest_news:
            print(f"Title: {news['title']}")
            print(f"Link: {news['link']}")
            result = news_fetcher.get_news_content(news['link'])
            print(f'Author: {result["author"]}')
            print(f'Date: {result["date"]}')
            print(f'Content: {result["content"]}\n')
    else:
        print("Failed to fetch the latest NBA news.")
