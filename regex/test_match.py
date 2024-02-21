#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : test_match.py
Author       : miaoyc
Create time  : 2024/2/21 16:36
Update time  : 2024/2/21 16:36
Description  : 
"""

from unittest import TestCase
from match import is_md5, is_base64


class Test(TestCase):
    def test_is_md5(self):
        x = is_md5("976282a740c57f734394c0ffa220ab74")
        self.assertEqual(True, x)
        x = is_md5("976282a740c57f734394c0")
        self.assertEqual(False, x)

    def test_is_base64(self):
        x = is_base64("bWlhb3lj")
        self.assertEqual(True, x)
        x = is_base64("bWlhb3l!")
        self.assertEqual(False, x)
