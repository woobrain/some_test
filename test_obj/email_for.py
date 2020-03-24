# -*- coding:utf-8 -*-
import email
import imaplib
import string


def SaveAttachImap(mail_host,
                   mail_port):  # login the imap server ,retrive the  new mails ,and download the attachments.

    M = imaplib.IMAP4_SSL(mail_host, mail_port)

    M.login('1050643094@qq.com', 'xyhtbkvfvgzzbefj')

    M.select('INBOX', False)

    typ, data = M.search(None, 'UNSEEN')

    try:

        typ, data = M.fetch(data[0].split()[-1], '(RFC822)')

        msg = email.message_from_string(data[0][1].decode('utf-8'))

        for par in msg.walk():

            name = par.get_filename()

            if name:
                dstdir = 'C:\\Users\\Administrator\\Desktop\\DOC\\' + name
                # dstdir = dstdir.encode('utf-8')
                data = par.get_payload(decode=True)
                try:
                    f = open(dstdir, 'wb')  # 注意一定要用wb来打开文件，因为附件一般都是二进制文件
                except:
                    print('open  file name error')
                else:
                    f.write(data)
                    f.close()
    except Exception as e:
        print('got msg error: %s' % e)

    M.close()
    M.logout()

SaveAttachImap('imap.qq.com', 993)
