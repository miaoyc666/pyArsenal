#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File name    : __init__.py
Author       : miaoyc
Create date  : 2023/10/21 19:23
Description  :
"""

import os
from boto3.session import Session
from botocore.config import Config


class S3Agent(object):
    def __init__(self, aws_access_key_id, aws_secret_access_key, endpoint_url, bucket):
        self.session = Session(aws_access_key_id, aws_secret_access_key)
        self.url = endpoint_url
        self.s3_client = self.session.client('s3', endpoint_url=self.url)
        self.bucket = bucket

    def connect_test(self):
        config = Config(connect_timeout=2, retries=dict(max_attempts=0))
        test_client = self.session.client('s3', endpoint_url=self.url, config=config)
        try:
            test_client.list_buckets()
            return True
        except:
            return False

    def upload_file(self, local_file, s3_key):
        try:
            self.s3_client.put_object(
                Bucket=self.bucket,
                Key=s3_key,
                Body=open(local_file, 'rb').read())
            return True
        except Exception as e:
            print("upload file error %s " % str(e))
            return False

    def upload_content(self, content, s3_key):
        try:
            self.s3_client.put_object(
                Key=s3_key,
                Body=content,
            )
            return True
        except Exception as e:
            print("upload content error %s " % str(e))
            return False

    def upload_file_streaming(self, fp, s3_key):
        try:
            self.s3_client.put_object(Bucket=self.bucket, Key=s3_key, Body=fp.read())
            return True
        except Exception as e:
            print("upload file streaming error %s " % str(e))
            return False

    def get_all_files(self, local_dir):
        list_files = []
        for lists in os.listdir(local_dir):
            lists = '/'.join([local_dir, lists])
            if os.path.isdir(lists):
                list_files.extend(self.get_all_files(lists))
            else:
                list_files.append(lists)
        return list_files

    def download_file_bin(self, s3_key):
        try:
            resp = self.s3_client.get_object(Bucket=self.bucket, Key=s3_key)
            return resp['Body'].read()
        except Exception as e:
            print("download bin failed: %s" % str(e))
            return False

    def is_exist(self, file_key):
        try:
            self.s3_client.head_object(Bucket=self.bucket, Key=file_key)
            return True
        except:
            return False
