# a = ['开票日期：2017年11月30日', '收款员：管理员']
# a = a[0].split('：')[1]
# import re
# a = ''.join(re.findall(r'\d+',a))
# print(a)

# import datetime
# a = datetime.datetime.strptime('2020年3月5日 12:00','%Y年%m月%d日 %H:%M').date()
# b = datetime.datetime.strptime('2020年3月4日 13:00','%Y年%m月%d日 %H:%M').date()
# print((a-b).days)

# import requests
# import re
# a = requests.get('https://finance.sina.com.cn/consume/qyzh/2020-03-06/doc-iimxxstf6875628.shtml')
# # print(a.content.decode('utf-8'))
# b = re.search(r'<!-- 原始正文begin --><!-- 原始正文end -->',a.content.decode('utf-8'))
# print(b)

import requests
from bs4 import BeautifulSoup
import re
res=requests.get('https://tousu.sina.com.cn/complaint/view/17348988666')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
content_html = str(soup.select('.ts-d-question')[0]) + '\n\n' + str(soup.select('.ts-d-steplist')[0])
article1=soup.select('.ts-d-question .article')[0].text + soup.select('.ts-d-question .ts-q-user')[0].text + soup.select('.ts-d-question .ts-q-list')[0].text
article2=soup.select('.ts-d-steplist')[0].text
article1 = re.sub('\n{2,}','\n',article1)
article2 = re.sub('\n{2,}','',article2)
article2 = re.sub('\s{2,}','\n',article2)
content = article1+article2

