import codecs
# file = open(r'C:\Users\Administrator\Desktop\XDYWZHDYW.SQL','rb').read()
# decoder = codecs.getdecoder('utf-16-le')
# print(decoder(file)[0])
# open(r'C:\Users\Administrator\Desktop\新建文本文档.txt','wb').write(decoder(file)[0].encode('utf-8'))

a = codecs.open(r'C:\Users\Administrator\Desktop\XDYWZHDYW.SQL',mode='rb',encoding='utf-16-le')
# print(a.readlines())
with open(r'C:\Users\Administrator\Desktop\新建文本文档.txt','wb') as f:
    for i in a.readlines():
        if '\ufeff' in i:
            i = i.replace('\ufeff','')
        f.write(i.replace('\n','').encode('utf-8'))