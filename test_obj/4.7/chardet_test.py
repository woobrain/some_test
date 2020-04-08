import chardet
geshi = chardet.detect(open(r'C:\Users\Administrator\Desktop\XDYWZHDYW.SQL','rb').read()).get('encoding')
with open(r'C:\Users\Administrator\Desktop\XDYWZHDYW.SQL','r',encoding=geshi) as f:
    print(f.read())