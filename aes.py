#!/usr/local/bin/python3

"""
File name    : aes.py
Author       : miaoyc
Create date  : 2022/9/16 15:02
Description  : aes加解密示例
"""

"""
需要安装python包如下
pip install pycryptodome
"""

import base64

from Crypto.Cipher import AES
from Crypto.Util import Padding
from Crypto.Util.py3compat import bchr

AES_SECRET_KEY = "miaoyc@@aes@@key"
IV = "1234567890123456"


class AesSecurity(object):
    """
    Aes加密类，定义常用加解密方法
    """

    block_size = 16

    def __init__(self):
        pass

    def __pad(self, text):
        """填充方式，加密内容必须为16字节的倍数，若不足则使用self.iv进行填充"""
        amount_to_pad = self.block_size - (len(text) % self.block_size)
        pad = bchr(0)
        return text.encode("utf-8") + pad * amount_to_pad

    def __unpad(self, text):
        pad = ord(text[-1])
        return text[:-pad]

    def getAES(self, key, data, mode=AES.MODE_ECB, style='pkcs7'):
        """AES加密
        :param key: 秘钥key
        :param data: 未加密数据
        :param mode: 加密模式
            :var MODE_ECB: :ref:`Electronic Code Book (ECB) <ecb_mode>`
            :var MODE_CBC: :ref:`Cipher-Block Chaining (CBC) <cbc_mode>`
            :var MODE_CFB: :ref:`Cipher FeedBack (CFB) <cfb_mode>`
            :var MODE_OFB: :ref:`Output FeedBack (OFB) <ofb_mode>`
            :var MODE_CTR: :ref:`CounTer Mode (CTR) <ctr_mode>`
            :var MODE_OPENPGP:  :ref:`OpenPGP Mode <openpgp_mode>`
            :var MODE_EAX: :ref:`EAX Mode <eax_mode>`

        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用

        :param block_size: 填充block大小：默认为8
        :param style: 填充算法：‘pkcs7’(default),‘iso7816’or‘x923’
        :return: 加密结果 byte string
        """

        _data = Padding.pad(data.encode('utf-8'), block_size=AES.block_size, style=style)
        _key = self.__pad(text=key)
        cipher = AES.new(_key, mode=mode)
        return base64.b64encode(cipher.encrypt(_data)).decode("utf-8")

    def decodeAES(self, key, data, mode=AES.MODE_ECB, style="pkcs7"):
        entrydata = base64.b64decode(data.encode("utf-8"))
        _data = Padding.pad(entrydata, block_size=AES.block_size, style=style)
        _key = self.__pad(text=key)
        cipher = AES.new(_key, mode=mode)
        return Padding.unpad(cipher.decrypt(_data)[:int(len(cipher.decrypt(_data)) / 16 - 1) * 16],
                             AES.block_size).decode("utf-8")


if __name__ == '__main__':
    security = AesSecurity()
    security.block_size = 32
    entrydata = security.getAES(key="1111111", data="86-123456789")
    print(entrydata)
    detrydata = security.decodeAES(key="1111111", data=entrydata)
    print(detrydata)

    security.block_size = 16
    entrydata = security.getAES(key="1111111", data="86-123456789")
    print(entrydata)
    detrydata = security.decodeAES(key="1111111", data=entrydata)
    print(detrydata)





