#-*- coding: utf-8 -*-
import zipfile
import os

def an_garcode(dir_names):
    os.chdir(dir_names)
    for temp_name in os.listdir('..'):
        # print(temp_name)
        try:
            new_name = temp_name.encode('cp437').decode("gbk")
            os.rename(temp_name, new_name)
            # print(temp_name)
            temp_name = new_name
            # print(temp_name)
        except:
            new_name = temp_name.encode('utf-8').decode('utf-8')
            temp_name = new_name
        if os.path.isdir(temp_name):
            an_garcode(temp_name)
            os.chdir('../..')


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)

    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        a = fz.extractall(dst_dir,fz.infolist())
    #     for file in fz.infolist():
    #         a = fz.extract(file, dst_dir)
    # else:
    #     print('This is not zip')
a = 'C:\\Users\\Administrator\\Desktop\\poc用例.zip'
unzip_file(a,'C:\\Users\\Administrator\\Desktop\\DOC\\')

an_garcode('C:\\Users\\Administrator\\Desktop\\DOC\\')