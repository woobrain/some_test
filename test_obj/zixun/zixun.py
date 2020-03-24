# -*- coding:utf-8 -*-
# zixun = '''['不要再妄自菲薄', '昆明已很不错', '昆明信息港', '2020-03-10', '14:39:04']'''
# zixun_list = zixun.split('\n')[0].split(' ')
# print(zixun_list[0])
# print(zixun_list[1])
# print(zixun_list[2]+' '+zixun_list[3])
# import datetime
# import time
# a = '2019-01-01 18:00:50'
# b = datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
# a = time.mktime(b.timetuple())
# print(a)
import requests
from bs4 import BeautifulSoup
import re

res = requests.get('http://henan.sina.com.cn/news/z/2020-03-12/detail-iimxxstf8365060.shtml')
# res = requests.get('https://k.sina.com.cn/article_1924738303_72b92cff02000qirs.html?from=astro')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
# html_content = soup.select('.article div,.article p[cms-style="font-L align-Justify"]')
# if html_content == []:
#     html_content = soup.select('.article-body div,.article-body p')
# html_str = ''
# for i in html_content:
#     html_str = html_str + str(i) + '\n'

# html_content = soup.select('.article div,.article p[cms-style="font-L align-Justify"]')
# if html_content == []:
#     html_content = soup.select('.article-body div,.article-body p')
# html_str = ''
# for i in html_content:
#     html_str = html_str + str(i) + '\n'
# print(html_str)

# html_content = soup.select('.article div,.article p[cms-style="font-L align-Justify"]')

# html_content = soup.select('.article')
# if html_content == []:
#     html_content = soup.select('.article-body')
# html_str = ''
# for i in html_content:
#     html_str = html_str + str(i) + '\n'
#
# if '特别声明：以上文章内容仅代表作者本人观点' in html_str:
#     html_str = re.split(r'<p\s*\S*>特别声明：以上文章内容仅代表作者本人观点',html_str)[0]
# print(html_str)

# str_a = ''
# content_str=soup.select('.article')
# if content_str == []:
#     content_str = soup.select('.article-body')
# for i in content_str:
#     i = i.text
#     i = re.sub('\s{1,2}','',i)
#     str_a += i + '\n'
# str_a = content_str[0].text
# str_a = re.sub('\s','\n',str_a)
# if '特别声明：以上文章内容仅代表作者本人观点' in str_a:
#     str_a = str_a.split('特别声明：以上文章内容仅代表作者本人观点')[0]
# print(str_a)

html_str1 = soup.select('.article')
if html_str1 == []:
    html_str1 = soup.select('.article-body')
# html_str = str(html_str1[0])
# print(html_str1[0].text)
# print(html_str)
# print(html_str[0])
# content_str = re.sub('\n', '', html_str.text)
# content_str = re.sub('\s{2,}', '\n', content_str)
# if content_str.startswith('\n'):
#     content_str = content_str[1::]script\s*\S*
# if content_str.endswith('\n'):
#     content_str = content_str[:len(content_str) - 1:]
# print(content_str)
# print(type(html_str1[0]))
# html_str = re.sub(r'<script.*[\s\S]*?</script>','',str(html_str1[0]))
# html_str = re.sub(r'<style.*[\s\S]*?</style>','',html_str)
# print(html_str)
# html_str = re.search(r'<script.*[\s\S]*?</script>',str(html_str1[0]))
# html_str = re.sub(r'<script\b[^>]*>[\s\S]*</script>','',str(html_str1[0]))
# print(html_str)
# print(html_str1[0].value)

content_str = re.sub('\n','',html_str1[0].text)
content_str = re.sub('\s{2,}','\n',content_str)
# if content_str.startswith('\n'):
#     content_str = content_str[1::]
# if content_str.endswith('\n'):
#     content_str = content_str[:len(content_str)-1:]
content_str = re.search(r'[^a-zA-Z|\S]*',content_str,re.S + re.M)
# pat=re.compile(r'[\u4e00-\u9fa5]+')
# content_str=pat.findall(content_str)
# if '特别声明：以上文章内容仅代表作者本人观点' in content_str:
#     content_str = content_str.split('特别声明：以上文章内容仅代表作者本人观点')[0]
print(content_str.group())

# article1 = re.sub('\n','',article1)
# article1 = re.sub('\s{2,}','\n',article1)
# if article1.startswith('\n'):
#     article1 = article1[1::]
# if article1.endswith('\n'):
#     article = article1[:len(article1)-1:]

# #
# #
# import logging
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
# logging.basicConfig(filename='my.log', level=logging.ERROR, format=LOG_FORMAT,datefmt=DATE_FORMAT)
# logging.error()

# import datetime
# # a = '2019年01月01日'
# a = datetime.date(year=2019,month=1,day=1)
# b = a + ' ' + '10:10:10'
# print(b)
# b = '2019年01月02日 10:10:10'
# b = datetime.datetime.strptime(b,'%Y年%m月%d日 %H:%M:%S').date()
#
# print(type((b - a).days))

# a = ['1/3年轻受访者表示教育并没有教会就业技能；IMA发布全球薪资调查结果', '|', '美通企业日报', '全球企业动态', '2020-03-12', '06:38:45']
# print(a[:3:])
