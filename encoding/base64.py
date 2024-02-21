#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : base64.py
Author       : miaoyc
Create time  : 2024/2/20 23:31
Update time  : 2024/2/20 23:31
Description  : 
"""

import base64


def base64_encode(s):
    return base64.b64encode(s.encode('utf-8'))


def base64_decode(s):
    return base64.b64decode(s).decode('utf-8')
