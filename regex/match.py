#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : match.py
Author       : miaoyc
Create time  : 2024/2/21 16:36
Update time  : 2024/2/21 16:36
Description  : 
"""

import re

BASE64_REGEX = re.compile(r'^[-A-Za-z0-9+/]*={0,3}$')
MD5_REGEX = re.compile(r'^[0-9a-f]{32}$')


def is_md5(s):
    """
    Check if string is valid MD5
    :param s:
    :return:
    """
    return True if MD5_REGEX.match(s) else False


def is_base64(s):
    """
    Check if string is valid base64
    :param s:
    :return:
    """
    return True if BASE64_REGEX.match(s) else False
