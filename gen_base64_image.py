#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
File name    : __init__.py
Author       : miaoyc
Create time  : 2020/8/7 20:49
Update time  : 2024/2/21 20:49
Description  : 图片转换为base64编码
"""

import sys
import base64


def convert_2_base64(file_path):
    with open(file_path, 'rb') as f:
        ls_f = base64.b64encode(f.read())
    return ls_f


def run():
    if len(sys.argv) != 2:
        print("example: python gen_base64_image.py file_path")
        sys.exit(1)
    file_path = sys.argv[1]
    print(convert_2_base64(file_path))


if __name__ == '__main__':
    run()
