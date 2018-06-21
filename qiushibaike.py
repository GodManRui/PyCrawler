from pymongo import MongoClient
import requests
from lxml import etree

client = MongoClient("127.0.0.1", 27017)
collection = client["duanzi"]["qiushibaike"]


def get_url_list():
    url_list = []
    url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
    for i in range(1, 14):
        url_list.append(url_temp.format(i))
    return url_list


def parse_url(url):
    headers = {
        "User-Agnet": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4091.2 Safari/537.36"}
    r = requests.get(url, headers=headers, timeout=5)
    html_str = r.content.decode()
    html = etree.HTML(html_str)
    return html


def get_content_list(html):
    div_list = html.xpath("//div[@id='content-left']/div")
    content_list = []
    for div in div_list:
        item = {}
        item["author_img"] = div.xpath("./div[@class='author clearfix']/a[1]/img/@src")
        if len(item["author_img"]) > 0:  # 获取用户头像图片
            item["author_img"] = "https://" + item["author_img"][0]
        else:
            item["author_img"] = None
        item["author_name"] = div.xpath("./div[@class='author clearfix']//h2/text()")
        if len(item["author_name"]) > 0:  # 获取用户名
            item["author_name"] = item["author_name"][0]
        else:
            item["author_name"] = None
        content_list.append(item)
    return content_list


def save_content_list(content_list):
    for content in content_list:
        print("*" * 5, content)
        collection.insert(content)
        print("保存成功")


def run():
    url_list = get_url_list()
    for url in url_list:
        html = parse_url(url)
        content_list = get_content_list(html)
        save_content_list(content_list)


if __name__ == '__main__':
    run()
