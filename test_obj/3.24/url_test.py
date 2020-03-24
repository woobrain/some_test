import requests
# from PIL import Image
# from io import BytesIO
from bs4 import BeautifulSoup
import bs4
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Cookie':'BIDUPSID=AE63666E0D85B6B905C96532FC74A4F7; PSTM=1584581624; BAIDUID=AE63666E0D85B6B974095CA6D510EC74:FG=1; BD_UPN=12314753; BDUSS=U4eUpTNjdNbVV2NDRhMVB2fmJ-TWs5MXY0cDUwMHVpUzJpNTE5S2NTNkd3WnRlRVFBQUFBJCQAAAAAAAAAAAEAAAAKsR4hYTEwNTA2NDMwOTQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIY0dF6GNHReen; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=30963_1458_31122_21124_30839_30901_30823_31086_22157; COOKIE_SESSION=722_0_7_5_32_27_1_5_5_7_0_5_354_0_88_0_1585014038_0_1585013950%7C9%230_0_1585013950%7C1; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=2; sugstore=1; H_PS_645EC=1952a7AppbdQ%2Byc7a51JVwgz7CvGEb4Srq1Sm0FMChE2tV0abQYoEj9Ea5A; BDSVRTM=0',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
payloads = {'ie':'UTF-8','wd':'北京'}
res = requests.get('https://www.baidu.com/s',headers=headers,params=payloads)
# i = Image.open(BytesIO(res.content))
# i.show()
# i.save('demo.png')
# print(res.status_code)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
content = soup.select('#content_left')
for i in content[0].find_all('div'):
    print(i.contents)
    # print(bs4.element.Tag)
    # print(type(i))
    # if isinstance(type(i),bs4.element.Tag):
    #     print(i.text)
    # else:
    #     print(type(i))





# with open('demo.jpg','wb') as f:
    # for i in res.iter_content():
    #     f.write(i)