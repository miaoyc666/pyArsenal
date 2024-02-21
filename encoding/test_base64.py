#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : test_base64.py
Author       : miaoyc
Create time  : 2024/2/20 23:31
Update time  : 2024/2/20 23:31
Description  : 
"""

"""
usage:
python -m unittest test_base64.Test
python -m unittest test_base64.Test.test_base64_encode
"""

from unittest import TestCase
from .base64 import base64_decode, base64_encode


class Test(TestCase):
    def test_base64_encode(self):
        x = base64_encode("miaoyc")
        self.assertEqual(x, "bWlhb3lj".encode())

    def test_base64_decode(self):
        x = base64_decode("bWlhb3lj")
        self.assertEqual(x, "miaoyc")
