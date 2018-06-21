from lxml import etree
from pymongo import MongoClient
text = '''<div> <ul>
            <li class="item-1"><a>first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a>
            </ul></div>
          '''
html = etree.HTML(text)
# print(html)
# element转换成字符串
# print(etree.tostring(html).decode())
href_temp = html.xpath("//li[@class='item-1']/a/@href")
# print(href_temp)
text_temp = html.xpath("//li[@class='item-1']/a/text()")
# print(text_temp)

for href in href_temp:
    item = {}
    item["href"] = href
    item["title"] = text_temp[(href_temp.index(href))]
    print(item)
print('#' * 20)
temp_li = html.xpath("//li[@class='item-1']")
for li in temp_li:
    item = {}
    href = li.xpath("./a/@href")
    if len(href) > 0:
        item["href"] = href[0];
    else:
        item["href"] = None;
    item["title"] = li.xpath("./a/text()")
    if len(item["title"]) > 0:
        item["title"] = item["title"][0]
    else:
        item["title"] = None
    print(item)




item = [{'href': 'link4.html', 'title': 'fourth item'}, {'href': 'link4.html', 'title': 'fourth item'}]
print(type(item))
con = MongoClient("127.0.0.1", 27017)
db = con["local"]
list = db['startup_log']
list.insert(item)