#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re


def extract(file_path):
    with open(file_path, 'r') as f:
        # print f.read()
        result = re.findall('\n[^\n]*?((?:来源：|原标题：)(?:.|\n)+?)(?:\n\w|\()', f.read(), flags=re.DOTALL + re.MULTILINE)
        print(len(result))
        if len(result) > 0:
            print(result[0])

if __name__ == '__main__':

    file_path = './html1.txt'
    extract(file_path)




