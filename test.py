import requests
from lxml import etree

url = "http://www.testtao.cn/?p=6435"
headers = {
    "User-Agnet": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4091.2 Safari/537.36"}
r = requests.get(url, headers=headers, timeout=5)
html_str = r.content.decode()
html = etree.HTML(html_str)
div_list = html.xpath("//*[@href]/@href")
print(div_list)
