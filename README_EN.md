# pyArsenal

[English](./README_EN.md) | [中文](./README_CN.md)

A comprehensive Python toolkit library providing commonly used utilities for encryption, hashing, encoding, database operations, and more.

## Overview

pyArsenal is a collection of reusable Python widgets and utilities designed to simplify common programming tasks. It includes modules for data encryption, hashing, encoding, regular expressions, database operations, and other essential utilities.

## Quick Start

### Installation as Git Submodule

```bash
git submodule add git@github.com:miaoyc666/pyArsenal.git
git submodule init
git submodule update
```

### Update Submodule

```bash
git submodule update --remote
```

## Modules

### Core Utilities

| Module | Description | Link |
|--------|-------------|------|
| **Encoding** | Base64 encoding/decoding utilities | [encoding](encoding) |
| **Hash** | MD5 and SHA256 hashing functions | [hash](hash) |
| **Regex** | Regular expression matching utilities | [regex](regex) |
| **DateTime** | Date and time manipulation tools | [xdatetime](xdatetime) |

### Security & Cryptography

| Module | Description | Link |
|--------|-------------|------|
| **AES** | AES encryption and decryption | [aes](aes) |
| **Base64 Image** | Image encoding as base64 | [gen_base64_image.py](gen_base64_image.py) |

### Database Operations

| Module | Description | Link |
|--------|-------------|------|
| **MySQL** | MySQL database utilities | [mysql](mysql) |
| ├─ **PyMySQL** | PyMySQL implementation example | [pymysql/demo.py](mysql/pymysql/demo.py) |
| ├─ **SQLAlchemy** | SQLAlchemy ORM example | [sqlalchemy/demo.py](mysql/sqlalchemy/demo.py) |
| **MongoDB** | MongoDB utilities | [mongo](mongo) |

### Cloud Services

| Module | Description | Link |
|--------|-------------|------|
| **S3** | AWS S3 client utilities | [s3](s3) |
| **Elasticsearch** | ES client utilities | [es](es) |
| **Email** | Email sending utilities | [xemail](xemail) |

### Network Utilities

| Module | Description | Link |
|--------|-------------|------|
| **IP Address** | Get server IP addresses from network interfaces | [network](network) |

### Additional Utilities

| Module | Description | Link |
|--------|-------------|------|
| **YAML** | YAML file read/write utilities | [yaml](yaml) |
| **Job Schedule** | Job scheduling utilities | [job_schedule.py](job_schedule.py) |
| **Download** | File download utilities | [download](download) |

## Key Features

- ✨ **Easy to Use**: Simple and intuitive API design
- 🔒 **Security First**: Includes encryption and hashing utilities
- 📊 **Database Support**: Multiple database backends (MySQL, MongoDB)
- ☁️ **Cloud Integration**: AWS S3 and Elasticsearch support
- 📦 **Modular**: Independent modules for flexible usage
- 🔄 **Cross-Platform**: Available in both Python and Go versions

## Usage Examples

### Encoding Example

```python
from encoding import base64

# Encode a string
encoded = base64.encode("Hello World")
print(encoded)

# Decode a string
decoded = base64.decode(encoded)
print(decoded)
```

### Hashing Example

```python
from hash import md5, sha256

# MD5 hash
hash_md5 = md5.hash_string("password123")
print(hash_md5)

# SHA256 hash
hash_sha256 = sha256.hash_string("password123")
print(hash_sha256)
```

### AES Encryption Example

```python
from aes import AesSecurity

aes = AesSecurity()
encrypted = aes.encrypt("sensitive data")
decrypted = aes.decrypt(encrypted)
```

### Regex Example

```python
from regex import match

# Email validation
email = "user@example.com"
if match.is_email(email):
    print("Valid email")
```

### Network - Get Server IP Example

```python
from network import get_server_ips, get_all_ips

# Get all valid server IP addresses
# Automatically filters out loopback, link-local, and Docker bridge IPs
ips = get_server_ips()
print(f"Server IPs: {ips}")
# Output: ['192.168.1.100', '10.0.0.50']

# Get detailed IP information including excluded IPs
all_ips_info = get_all_ips()
print(f"Valid IPs: {all_ips_info['valid_ips']}")
print(f"Excluded IPs: {all_ips_info['excluded_ips']}")
# Excluded IPs: ['127.0.0.1', '::1', '169.254.x.x', '172.17.x.x']
```

**Filtered IP Types:**
- Loopback: `127.0.0.1`, `::1`
- Link-local: `169.254.x.x`, `fe80::/10`
- Docker bridge: `172.17.0.0/16`
- Multicast addresses

**Preserved IP Types:**
- Private networks: `192.168.x.x`, `10.x.x.x`, `172.16.x.x - 172.31.x.x`
- Valid server IPs from any NIC

## Related Projects

- [goArsenal](https://github.com/miaoyc666/goArsenal) - Golang version of this library
- [rd-manual](https://github.com/miaoyc666/rd-manual) - Reference documentation

## Documentation

- [Python Basic Commands](https://github.com/miaoyc666/rd-manual/blob/main/Python/README.md)
- [AES Implementation (Go)](https://github.com/miaoyc666/goArsenal/blob/master/aes/aes.go)

## Requirements

Each module may have specific dependencies. Common requirements include:

- `pycryptodome` - For AES encryption
- `PyMySQL` - For MySQL database operations
- `SQLAlchemy` - For ORM functionality
- `elasticsearch-py` - For Elasticsearch integration
- `boto3` - For AWS S3 operations
- `PyYAML` - For YAML file handling

## Installation of Dependencies

```bash
# Core utilities
pip install pycryptodome

# Database
pip install PyMySQL sqlalchemy

# Cloud services
pip install boto3 elasticsearch

# Other utilities
pip install PyYAML
```

## License

MIT

## Author

[miaoyc](https://github.com/miaoyc666)

