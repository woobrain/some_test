from lxml import etree
import requests

res = requests.get('https://tech.sina.com.cn/roll/2020-03-13/doc-iimxyqwa0088119.shtml')
soup = etree.HTML(res.content.decode('utf-8'))
c_html = soup.xpath('//div[@class="article-body main-body"]/script')
html = soup.xpath('//div[@class="article-body main-body"]')[0]
for i in c_html:
    html.remove(i)
# print(type(html[0]))
# print(c_html)
t = etree.tostring(html, encoding="utf-8", pretty_print=True)
# t1 = html.xpath('')
for i in html:
    print(i.text)
# print(type(t.decode('utf-8')))