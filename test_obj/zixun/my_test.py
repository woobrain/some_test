import requests
import re
from bs4 import BeautifulSoup
# res = requests.get('http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/lastest/rptid/637018000571/index.phtml')
res = requests.get('https://cj.sina.com.cn/articles/view/1704103183/65928d0f02001lsce?from=finance')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
if 1 == 1:
    html_str1 = soup.select('.article')
    css_sci = '.article script'
    css_sty = '.article style'
    if html_str1 == []:
        html_str1 = soup.select('.article-body')
        if html_str1 == []:
            html_str1 = soup.select('.m-atc-original')
        else:
            css_sci = '.article-body script'
            css_sty = '.article-body style'
    script_all = len(soup.select(css_sci))
    style_all = len(soup.select(css_sty))
    if script_all != 0:
        for i in range(script_all):
            html_str1[0].script.extract()
    if style_all != 0:
        for i in range(style_all):
            html_str1[0].style.extract()
    html_str = str(html_str1[0])

    if '特别声明：以上文章内容仅代表作者本人观点' in html_str:
        html_str = re.split(r'<p\s*\S*>特别声明：以上文章内容仅代表作者本人观点',html_str)[0]
    if '免责声明：本信息由新浪财经从公开信息中摘录' in html_str:
        html_str = re.split(r'<p\s*\S*>免责声明：本信息由新浪财经从公开信息中摘录',html_str)[0]
    if '新民网出于传递企业资讯的目的刊登此文' in html_str:
        html_str = re.split(r'<p\s*\S*>新民网出于传递企业资讯的目的刊登此文',html_str)[0]
    # content_str = html_str1[0].get_text("\n")
    # print(html_str)
    content_str = html_str1[0].text
    content_str = re.sub('\n{2,}','',content_str)
    if content_str == '':
        print(1)
    # # content_str = re.sub('\s{2,3}','\n',content_str)
    if '特别声明：以上文章内容仅代表作者本人观点' in content_str:
        content_str = content_str.split('特别声明：以上文章内容仅代表作者本人观点')[0]
    if '免责声明：本信息由新浪财经从公开信息中摘录' in content_str:
        content_str = content_str.split('免责声明：本信息由新浪财经从公开信息中摘录')[0]
    if '新民网出于传递企业资讯的目的刊登此文' in content_str:
        content_str = content_str.split('新民网出于传递企业资讯的目的刊登此文')[0]
    print(content_str)
