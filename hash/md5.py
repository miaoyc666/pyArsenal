#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : md5.py
Author       : miaoyc
Create time  : 2024/1/31 16:02
Update time  : 2024/1/31 16:02
Description  :
"""

import base64
import hashlib


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def file_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def base64_encode(s):
    return base64.b64encode(s.encode('utf-8'))


def base64_decode(s):
    return base64.b64decode(s).decode('utf-8')


def md5_base64_byte(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    # 二进制数据字符串值
    md5_str = m.digest()
    b64_str = base64.b64encode(md5_str)
    return md5_str, b64_str.decode('utf-8')


def md5_base64_hex(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    # 十六进制数据字符串值
    md5_str = m.hexdigest()
    b64_str = base64.b64encode(md5_str.encode('utf-8'))
    return md5_str, b64_str.decode('utf-8')
