#-*- coding: utf-8 -*-
import zipfile
import os

def an_garcode(dir_names):
    os.chdir(dir_names)
    for temp_name in os.listdir('..'):
        try:
            new_name = temp_name.encode('cp437')
            new_name = new_name.decode("gbk")
            os.rename(temp_name, new_name)
            temp_name = new_name
        except:
            pass
        if os.path.isdir(temp_name):
            an_garcode(temp_name)
            os.chdir('../..')


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.infolist():
            a = fz.extract(file, dst_dir)
            if zipfile.is_zipfile(a):
                return unzip_file(a,dst_dir)
            # print(file)
    else:
        print('This is not zip')
a = 'C:\\Users\\Administrator\\Desktop\\新建文件夹.zip'
unzip_file(a,'C:\\Users\\Administrator\\Desktop\\DOC')

an_garcode('C:\\Users\\Administrator\\Desktop\\DOC')