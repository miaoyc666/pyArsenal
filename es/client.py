#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : client.py
Author       : miaoyc
Create date  : 2023/10/15 20:19
Description  : es client, ref: https://elasticsearch-dsl.readthedocs.io/en/latest/
"""

import ssl
from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Search

context = ssl._create_unverified_context()


class EsUtils(object):
    def __init__(self, es_hosts, http_auth, index, doc_type, url_prefix="", timeout=5, max_retries=2,
                 retry_on_timeout=True, ssl_context=context):
        self.es_client = Elasticsearch(
            es_hosts, http_auth=http_auth, url_prefix=url_prefix, timeout=timeout, max_retries=max_retries,
            retry_on_timeout=retry_on_timeout, ssl_context=ssl_context)
        self.index = index
        self.doc_type = doc_type

    def insert(self, data, _id='', refresh=False):
        actions = {
            'op_type': 'index',
            'index': self.index,
            'doc_type': self.doc_type,
            'body': data,
            'refresh': refresh,
        }
        if _id:
            actions['id'] = _id

        res = self.es_client.index(**actions)
        return res

    def update(self, data, _id='', refresh=False):
        res = self.es_client.update(index=self.index, doc_type=self.doc_type, id=_id, body=data, refresh=refresh)
        return res

    def update_by_query(self, data, refresh=False):
        res = self.es_client.update_by_query(index=self.index, doc_type=self.doc_type, body=data, refresh=refresh)
        return res

    def delete_by_id(self, _id):
        res = self.es_client.delete(index=self.index, doc_type=self.doc_type, id=_id)
        return res

    def delete_by_query(self, query):
        res = self.es_client.delete_by_query(index=self.index, doc_type=self.doc_type, body=query)
        return res

    def bulk_insert(self, data, _id='', refresh=False):
        actions = [
            {
                '_op_type': 'index',
                '_index': self.index,
                '_type': self.doc_type,
                '_source': data,
                'refresh': refresh,
            }
        ]
        if _id:
            actions[0]['_id'] = _id
        helpers.bulk(client=self.es_client, actions=actions)

    def bulk_update(self, data, _id='', refresh=False):
        actions = [
            {
                '_op_type': 'update',
                '_index': self.index,
                '_type': self.doc_type,
                '_source': data,
                'refresh': refresh,
            }
        ]
        if _id:
            actions[0]['_id'] = _id
        helpers.bulk(client=self.es_client, actions=actions)

    def scan(self, query, scroll="5m"):
        query_res = helpers.scan(
            client=self.es_client,
            query=query,
            scroll=scroll,
            index=self.index,
            doc_type=self.doc_type,
        )
        return query_res

    def search(self):
        return Search(index=self.index, doc_type=self.doc_type, using=self.es_client)


