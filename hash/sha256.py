#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : sha256.py
Author       : miaoyc
Create time  : 2024/3/21 9:54
Update time  : 2024/3/21 9:54
Description  : 
"""

import hashlib
import io


def gen_sha256(data):
    """
    生成字符串的sha256
    :param data:
    :return:
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()


def file_sha256(file_path):
    """
    计算文件的sha256
    :param file_path:
    :return:
    """
    block_size = 65536
    hasher = hashlib.sha256()
    with io.open(file_path, mode='rb') as f:
        buf = f.read(block_size)
        while buf:
            hasher.update(buf)
            buf = f.read(block_size)
    return hasher.hexdigest()
