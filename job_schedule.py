#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : job_schedule.py
Create time  : 2024/3/18 20:02
Update time  : 2024/3/18 20:02
Description  : 定时任务
"""

import time
from datetime import datetime

import schedule


def job():
    print(current_time(), " 执行任务...")


def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 每天的特定时间执行
# schedule.every().day.at("10:30").do(job)

# 每小时执行一次
# schedule.every().hour.do(job)

# 每隔10分钟执行一次
# schedule.every(10).minutes.do(job)

# 每周的特定时间执行
schedule.every().monday.at("17:56").do(job)


# 每隔5秒执行一次
# schedule.every(5).seconds.do(job)


for job in schedule.jobs:
    print(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# job = schedule.every(10).minutes.do(job)
# schedule.cancel_job(job)
