import re
import csv
import requests
from bs4 import BeautifulSoup
# import datetime
import time
gongsi = '招商银行'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
            }
for v in range(1,6):
    res = requests.get('http://search.sina.com.cn/?q=%s&c=news&from=&col=&range=all&source=&country=&size=10&time=&dpc=0&a=&ps=0&pf=0&page=%d'%(gongsi,v),headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'lxml')
    content = soup.select('.box-result h2')
    for r in content:
        a = r.span.text.lstrip().rstrip().split(' ')
        source = a[0]
        fb_time = time.strptime(' '.join(a[1:]),'%Y-%m-%d %H:%M:%S')
        try:
            href_str = r.a['href']
            source_str = source
            if href_str != '':
                res = requests.get(href_str, timeout=5,headers=headers)
                res.encoding = 'utf-8'
                soup = BeautifulSoup(res.text, 'html.parser')
                content_str = ''
                html_str = ''
                html_str1 = ''
                article1 = ''
                article2 = ''
                script_all = 0
                style_all = 0
                if source_str == '黑猫投诉':
                    html_str = str(soup.select('.ts-d-question')[0]) + str(
                        soup.select('.ts-d-steplist')[0])
                    article1 = soup.select('.ts-d-question .article')[0].text + \
                               soup.select('.ts-d-question .ts-q-user')[0].text + \
                               soup.select('.ts-d-question .ts-q-list')[0].text
                    article2 = soup.select('.ts-d-steplist')[0].text
                    article1 = re.sub('\n{2,}', '\n', article1)
                    article2 = re.sub('\n{2,}', '', article2)
                    article2 = re.sub('\s{2,}', '\n', article2)
                    content_str = article1 + article2
                else:
                    html_str1 = soup.select('.article')
                    if html_str1 == []:
                        html_str1 = soup.select('.article-body')
                        if html_str1 == []:
                            html_str1 = soup.select('.m-atc-original')
                        else:
                            script_all = len(soup.select('.article-body script'))
                            style_all = len(soup.select('.article-body style'))
                    else:
                        script_all = len(soup.select('.article script'))
                        style_all = len(soup.select('.article style'))
                    for i in range(script_all):
                        html_str1[0].script.extract()
                    for i in range(style_all):
                        html_str1[0].style.extract()
                    html_str = str(html_str1[0])
                    if '特别声明：以上文章内容仅代表作者本人观点' in html_str:
                        html_str = re.split(r'<p\s*\S*>特别声明：以上文章内容仅代表作者本人观点', html_str)[0]
                    if '免责声明：本信息由新浪财经从公开信息中摘录' in html_str:
                        html_str = re.split(r'<p\s*\S*>免责声明：本信息由新浪财经从公开信息中摘录', html_str)[0]
                    content_str = html_str1[0].text
                    content_str = re.sub('\n{2,}', '', content_str)
                    # content_str = re.sub('\s{2,3}','\n',content_str)
                    if '特别声明：以上文章内容仅代表作者本人观点' in content_str:
                        content_str = content_str.split('特别声明：以上文章内容仅代表作者本人观点')[0]
                    if '免责声明：本信息由新浪财经从公开信息中摘录' in content_str:
                        content_str = content_str.split('免责声明：本信息由新浪财经从公开信息中摘录')[0]
                    if ('原 创 视 频' or '视频') in content_str:
                        print(['yc', href_str])
                        continue
                    if '自动播放' in content_str:
                        print(['zd', href_str])
                        continue

                with open(r'C:\\Users\\Administrator\\Desktop\\test.csv','a',newline='',encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    # 先写入columns_name
                    writer.writerow([r.a.text.lstrip().rstrip(),html_str,content_str,fb_time,source_str,gongsi])
        except Exception as e:
            print(r.a['href'])