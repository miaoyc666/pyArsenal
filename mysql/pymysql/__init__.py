#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : __init__.py
Author       : miaoyc
Create date  : 2023/11/27 10:52
Description  : 
"""

"""
User表建表语句:
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

初始化数据：
INSERT INTO users (name, email, password)
VALUES
    ('John Doe', 'john.doe@example.com', 'password1'),
    ('Jane Smith', 'jane.smith@example.com', 'password2'),
    ('David Johnson', 'david.johnson@example.com', 'password3'),
    ('Sarah Brown', 'sarah.brown@example.com', 'password100');
"""

import os
import time
import pymysql
import traceback

MYSQL_HOST = '127.0.0.1'
USER = 'miaoyc'
PASSWORD = 'cee90b47903094dfaf7'
DB = 'testc'
PORT = 34579

db = pymysql.connect(host=MYSQL_HOST, user=USER, passwd=PASSWORD, db=DB, port=PORT)
cur = db.cursor()


def query(tb_name, limit=10):
    # 执行SQL查询
    sql = "SELECT * FROM {0} limit {1}".format(tb_name, limit)
    cur.execute(sql)

    # 获取查询结果
    rows = cur.fetchall()
    return rows
        
    
def insert(res_list_):
    pre_sql = "INSERT IGNORE INTO users(name, email, password) VALUES "
    for name, email, password in res_list_:
        tmp = '("{0}","{1}","{2}"),'.format(name, email, password)
        pre_sql += tmp
    sql = pre_sql[:-1] + ';'
    cur.execute(sql)
    db.commit()

def delete(user_name):
    # 执行SQL删除操作
    sql = "DELETE FROM users WHERE name = %s"
    cur.execute(sql, (user_name,))

    # 提交事务
    # conn.commit()




if __name__ == '__main__':
    query("users")
    insert([["miaoyc", "miaoyc@miaoyc.com", "xxxxxx"]])
    query("users")
    delete("miaoyc")
    query("users")
