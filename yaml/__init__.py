#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : __init__.py
Author       : miaoyc
Create date  : 2023/11/16 18:49
Description  : 
"""

import yaml


def load_yaml(file_path):
    with open(file_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


def modify(file_path, key, value):
    config = load_yaml(file_path)
    config[key] = value
    with open(file_path, 'w') as file:
        yaml.dump(config, file)

