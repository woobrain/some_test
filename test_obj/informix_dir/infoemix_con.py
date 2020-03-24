import IfxPyDbi
ConStr = "SERVER=infor99;DATABASE=db0;HOST=127.0.0.1;SERVICE=27988;UID=informix;PWD=980120;"

try:
    # netstat -a | findstr  9088
    conn = IfxPyDbi.connect(ConStr, "", "")
except Exception as e:
    print('ERROR: Connect failed')
    print(e)
    quit()