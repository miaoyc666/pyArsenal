#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
依赖：
yum install gcc-c++
pip3 install sqlalchemy
pip3 install mysql-connector-python
"""

MYSQL_HOST = '127.0.0.1'
USER = 'miaoyc'
PASSWORD = 'xxx'
DB = 'xxx'
PORT = 34579

# 创建数据库引擎
engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.format(USER, PASSWORD, MYSQL_HOST, PORT, DB))

# 创建会话工厂
Session = sessionmaker(bind=engine)

# 创建基础模型类
Base = declarative_base()

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
# 定义用户表模型
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))


# 创建表结构
Base.metadata.create_all(engine)


# 查询所有用户
session = Session()

def print_result(rows):
    for row in rows:
        print(row.name, row.email, row.password)

def query():
    rows = session.query(User).all()
    return rows

def insert(user_list):
    objects_list = []
    for name, email, password in user_list:
        objects_list.append(User(name=name, email=email, password=password))
    session.bulk_save_objects(objects_list)
    session.commit()

def delete(user_list):
    session.query(User).filter(User.name.in_(user_list)).delete(synchronize_session=False)
    session.commit()


if __name__ == '__main__':
    print("query!")
    print_result(query())
    print("insert!")
    insert([["miaoyc", "miaoyc@miaoyc.com", "xxxxxx"], ["miaoyc1", "miaoyc1@miaoyc.com", "xxxxxxy"]])
    print("query!")
    print_result(query())
    print("delete!")
    delete(["miaoyc", "miaoyc1"])
    print("query!")
    print_result(query())
