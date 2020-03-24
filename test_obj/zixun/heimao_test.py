# import re
#
# from bs4 import BeautifulSoup
# import requests
#
# a = requests.get('https://tousu.sina.com.cn/complaint/view/17349027988/')
# a.encoding = 'utf-8'
# soup = BeautifulSoup(a.text,'html.parser')
# #
# html_content = str(soup.select('.ts-d-question')[0]) + '\n\n' + str(soup.select('.ts-d-steplist')[0])
# print(html_content)
# art = soup.select('.ts-d-question>.ts-q-list li,.ts-d-steplist span')
# str_a = ''
# for i in art:
#     str_a += i.text + '\n'
# str_a = re.sub('\s{2,}',' ',str_a)
# print(str_a)
a = '视频码'
if '视频' in a:
    print('yc')