# pyArsenal

[English](./README_EN.md) | [中文](./README_CN.md)

一个全面的 Python 工具库，提供加密、哈希、编码、数据库操作等常用工具函数。

## 项目介绍

pyArsenal 是一个可复用的 Python 工具和实用程序集合，旨在简化常见的编程任务。它包括数据加密、哈希计算、编码解码、正则表达式、数据库操作以及其他必要的工具模块。

## 快速开始

### 作为 Git 子模块安装

```bash
git submodule add git@github.com:miaoyc666/pyArsenal.git
git submodule init
git submodule update
```

### 更新子模块

```bash
git submodule update --remote
```

## 模块说明

### 核心工具

| 模块 | 说明 | 链接 |
|------|------|------|
| **编码工具** | Base64 编码/解码工具 | [encoding](encoding) |
| **哈希函数** | MD5 和 SHA256 哈希函数 | [hash](hash) |
| **正则表达式** | 正则表达式匹配工具 | [regex](regex) |
| **日期时间** | 日期和时间操作工具 | [xdatetime](xdatetime) |

### 安全加密

| 模块 | 说明 | 链接 |
|------|------|------|
| **AES 加密** | AES 加密和解密 | [aes](aes) |
| **图像编码** | 图像 Base64 编码 | [gen_base64_image.py](gen_base64_image.py) |

### 数据库操作

| 模块 | 说明 | 链接 |
|------|------|------|
| **MySQL** | MySQL 数据库工具 | [mysql](mysql) |
| ├─ **PyMySQL** | PyMySQL 实现示例 | [pymysql/demo.py](mysql/pymysql/demo.py) |
| ├─ **SQLAlchemy** | SQLAlchemy ORM 示例 | [sqlalchemy/demo.py](mysql/sqlalchemy/demo.py) |
| **MongoDB** | MongoDB 数据库工具 | [mongo](mongo) |

### 云服务集成

| 模块 | 说明 | 链接 |
|------|------|------|
| **S3** | AWS S3 客户端工具 | [s3](s3) |
| **Elasticsearch** | Elasticsearch 客户端工具 | [es](es) |
| **邮件服务** | 邮件发送工具 | [xemail](xemail) |

### 网络工具

| 模块 | 说明 | 链接 |
|------|------|------|
| **IP 地址** | 获取服务器网卡 IP 地址 | [network](network) |

### 其他工具

| 模块 | 说明 | 链接 |
|------|------|------|
| **YAML** | YAML 文件读写工具 | [yaml](yaml) |
| **定时任务** | 任务调度工具 | [job_schedule.py](job_schedule.py) |
| **文件下载** | 文件下载工具 | [download](download) |

## 主要特性

- ✨ **易于使用**: 简洁直观的 API 设计
- 🔒 **安全第一**: 包含加密和哈希工具
- 📊 **数据库支持**: 支持多种数据库后端（MySQL、MongoDB）
- ☁️ **云服务集成**: AWS S3 和 Elasticsearch 支持
- 📦 **模块化设计**: 独立的模块，灵活使用
- 🔄 **跨平台**: 同时提供 Python 和 Go 版本

## 使用示例

### 编码示例

```python
from encoding import base64

# 编码字符串
encoded = base64.encode("Hello World")
print(encoded)

# 解码字符串
decoded = base64.decode(encoded)
print(decoded)
```

### 哈希示例

```python
from hash import md5, sha256

# MD5 哈希
hash_md5 = md5.hash_string("password123")
print(hash_md5)

# SHA256 哈希
hash_sha256 = sha256.hash_string("password123")
print(hash_sha256)
```

### AES 加密示例

```python
from aes import AesSecurity

aes = AesSecurity()
encrypted = aes.encrypt("sensitive data")
decrypted = aes.decrypt(encrypted)
```

### 正则表达式示例

```python
from regex import match

# 邮箱验证
email = "user@example.com"
if match.is_email(email):
    print("有效的邮箱")
```

### 网络工具 - 获取服务器 IP 示例

```python
from network import get_server_ips, get_all_ips

# 获取所有有效的服务器 IP 地址
# 自动过滤掉回环地址、本地链接地址和 Docker 网桥地址
ips = get_server_ips()
print(f"服务器 IP: {ips}")
# 输出: ['192.168.1.100', '10.0.0.50']

# 获取详细的 IP 信息（包含被过滤的 IP）
all_ips_info = get_all_ips()
print(f"有效 IP: {all_ips_info['valid_ips']}")
print(f"被排除的 IP: {all_ips_info['excluded_ips']}")
# 被排除的 IP: ['127.0.0.1', '::1', '169.254.x.x', '172.17.x.x']
```

**被过滤的 IP 类型：**
- 回环地址: `127.0.0.1`, `::1`
- 链接本地地址: `169.254.x.x`, `fe80::/10`
- Docker 网桥: `172.17.0.0/16`
- 组播地址

**保留的 IP 类型：**
- 私有网段: `192.168.x.x`, `10.x.x.x`, `172.16.x.x - 172.31.x.x`
- 所有网卡的有效 IP 地址

## 相关项目

- [goArsenal](https://github.com/miaoyc666/goArsenal) - 本库的 Go 语言版本
- [rd-manual](https://github.com/miaoyc666/rd-manual) - 参考文档库

## 文档链接

- [Python 基础命令](https://github.com/miaoyc666/rd-manual/blob/main/Python/README.md)
- [AES 加密实现 (Go 版)](https://github.com/miaoyc666/goArsenal/blob/master/aes/aes.go)

## 依赖要求

各个模块可能有特定的依赖。常见的依赖包括：

- `pycryptodome` - AES 加密功能
- `PyMySQL` - MySQL 数据库操作
- `SQLAlchemy` - ORM 功能
- `elasticsearch-py` - Elasticsearch 集成
- `boto3` - AWS S3 操作
- `PyYAML` - YAML 文件处理

## 安装依赖

```bash
# 核心工具
pip install pycryptodome

# 数据库
pip install PyMySQL sqlalchemy

# 云服务
pip install boto3 elasticsearch

# 其他工具
pip install PyYAML
```

## 许可证

MIT

## 作者

[miaoyc](https://github.com/miaoyc666)

