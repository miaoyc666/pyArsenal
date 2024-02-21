#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : test_md5.py
Author       : miaoyc
Create time  : 2024/2/2 14:21
Update time  : 2024/2/2 14:21
Description  : 
"""

"""
usage:
python -m unittest test_md5.Test
python -m unittest test_md5.Test.test_gen_md5
"""

from unittest import TestCase
from md5 import gen_md5


class Test(TestCase):
    def test_gen_md5(self):
        x = gen_md5("123445")
        self.assertEqual("4739c5c11d833bb199c16ff95a92b267", x)
