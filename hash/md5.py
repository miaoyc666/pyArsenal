#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : md5.py
Author       : miaoyc
Create time  : 2024/1/31 16:02
Update time  : 2024/2/21 16:29
Description  :
"""

import hashlib


def gen_md5(data):
    """
    生成字符串的md5
    :param data:
    :return:
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.md5(data).hexdigest()


def file_md5(file_path):
    """
    计算文件的md5
    :param file_path:
    :return:
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
