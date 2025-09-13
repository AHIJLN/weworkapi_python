# 企业微信API Python SDK

[![Python Version](https://img.shields.io/badge/python-2.7%7C3.x-blue.svg)](https://www.python.org/)
[![WeWork API](https://img.shields.io/badge/WeWork-API-orange.svg)](https://work.weixin.qq.com/api/doc)

企业微信API的Python封装库，为开发者提供简单易用的企业微信API调用接口。由腾讯企业微信团队官方维护。

## 📋 项目简介

weworkapi_python 是腾讯企业微信团队开发的Python SDK，旨在简化开发者对企业微信API接口的调用。本库提供了完整的企业微信API封装，包括用户管理、部门管理、消息发送、应用管理等核心功能，支持企业内部应用和第三方服务商开发。

> **重要提示**：本库为官方示例代码，不保证完全无bug。生产环境使用请充分测试，一切以[官方API文档](https://work.weixin.qq.com/api/doc)为准。

## ✨ 功能特性

### 🔧 核心功能
- **用户管理** - 创建、获取、更新、删除用户信息
- **部门管理** - 部门的增删改查操作
- **标签管理** - 用户标签的管理和操作
- **消息发送** - 支持文本、图片、文件等多种消息类型
- **应用管理** - 企业应用的配置和管理
- **菜单管理** - 自定义菜单的创建和管理

### 🛡️ 安全特性
- **消息加解密** - 支持XML和JSON格式的消息加解密
- **Access Token管理** - 自动获取和刷新访问令牌
- **多版本支持** - 同时支持Python 2.7和Python 3.x

### 📊 高级功能
- **打卡数据** - 获取员工打卡记录
- **审批数据** - 企业审批流程数据获取
- **发票管理** - 电子发票信息处理
- **群聊管理** - 企业群聊的创建和管理
- **小程序集成** - 企业微信小程序相关接口

## 🚀 安装说明

### 环境要求
- Python 2.7 或 Python 3.x
- requests 库
- pycrypto 库（用于消息加解密功能）

### 安装依赖
```bash
# 安装基础依赖
pip install requests

# 安装加解密依赖（用于回调消息处理）
pip install pycrypto
```

> **加密依赖说明**：如果遇到 `ImportError: No module named 'Crypto'` 错误，请访问 [pycrypto官方网站](https://www.dlitz.net/software/pycrypto/) 下载并按照文档安装。

### 下载项目
```bash
git clone https://github.com/AHIJLN/weworkapi_python.git
cd weworkapi_python
```

## 🎯 快速开始

### 1. 配置企业信息
首先，需要在企业微信管理后台获取相关配置信息：

```python
# 企业ID - 在"我的企业"页面获取
CORP_ID = "your_corp_id"

# 应用Secret - 在对应应用页面获取
APP_SECRET = "your_app_secret"
```

### 2. 基本使用示例
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append("api/src/")

from CorpApi import CorpApi, CORP_API_TYPE

# 初始化API客户端
api = CorpApi(CORP_ID, APP_SECRET)

try:
    # 发送文本消息
    response = api.httpCall(
        CORP_API_TYPE['MESSAGE_SEND'],
        {
            "touser": "user_id",           # 接收用户ID
            "agentid": 1000002,           # 应用ID
            "msgtype": "text",            # 消息类型
            "text": {
                "content": "Hello, 企业微信!"  # 消息内容
            }
        }
    )
    print("消息发送成功:", response)
    
except Exception as e:
    print("发送失败:", e)
```

## 📚 API文档

### 主要类说明

#### CorpApi
企业微信API的主要接口类，提供所有企业微信API的调用方法。

```python
class CorpApi(AbstractApi):
    def __init__(self, corpid, secret):
        """
        初始化企业微信API客户端
        
        Args:
            corpid (str): 企业ID
            secret (str): 应用Secret
        """
```

#### AbstractApi
API基础抽象类，处理HTTP请求、token管理等底层逻辑。

### 主要API类型

#### 用户管理 API
```python
# 创建用户
api.httpCall(CORP_API_TYPE['USER_CREATE'], user_data)

# 获取用户信息
api.httpCall(CORP_API_TYPE['USER_GET'], {'userid': 'zhangsan'})

# 更新用户
api.httpCall(CORP_API_TYPE['USER_UPDATE'], user_data)

# 删除用户
api.httpCall(CORP_API_TYPE['USER_DELETE'], {'userid': 'zhangsan'})
```

#### 消息发送 API
```python
# 发送文本消息
api.httpCall(CORP_API_TYPE['MESSAGE_SEND'], {
    "touser": "user_id",
    "agentid": app_id,
    "msgtype": "text",
    "text": {"content": "消息内容"}
})
```

#### 部门管理 API
```python
# 创建部门
api.httpCall(CORP_API_TYPE['DEPARTMENT_CREATE'], dept_data)

# 获取部门列表
api.httpCall(CORP_API_TYPE['DEPARTMENT_LIST'], {})
```

## ⚙️ 配置说明

### 获取企业微信配置参数

1. **企业ID (CORP_ID)**
   - 登录企业微信管理后台
   - 进入"我的企业" → "企业信息"
   - 复制"企业ID"

2. **应用Secret (APP_SECRET)**
   - 进入"应用管理" → 选择对应应用
   - 查看"Secret"信息

3. **特殊应用配置**
   - 通讯录同步：需要开启API接口同步
   - 打卡应用：在基础应用中的打卡应用获取
   - 审批应用：在基础应用中的审批应用获取

### 配置文件示例
在 `api/examples/TestConf.py` 中配置你的企业信息：

```python
# api/examples/TestConf.py
TestConf = {
    # 企业的ID，在管理端->"我的企业" 可以看到
    "CORP_ID": "ww55ca070cb9b7eb22",  # 请替换为你的企业ID

    # "通讯录同步"应用的secret, 开启API接口同步后可获取
    "CONTACT_SYNC_SECRET": "your_contact_sync_secret",

    # 某个自建应用的ID及secret, 在管理端 -> 企业应用 -> 自建应用中获取
    "APP_ID": 1000002,
    "APP_SECRET": "your_app_secret",

    # 打卡应用的ID及secret（基础应用 -> 打卡 -> API）
    "CHECKIN_APP_ID": 3010011,
    "CHECKIN_APP_SECRET": "your_checkin_secret",

    # 审批应用的ID及secret（基础应用 -> 审批 -> API）
    "APPROVAL_APP_ID": 3010040,
    "APPROVAL_APP_SECRET": "your_approval_secret",
}
```

> **安全提示**：请勿将真实的secret信息提交到版本控制系统中。建议使用环境变量或单独的配置文件管理敏感信息。

## 💡 示例代码

### 用户管理示例
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append("../src/")

from CorpApi import CorpApi, CORP_API_TYPE, ApiException
from TestConf import TestConf

# 初始化API（使用通讯录同步应用的secret）
api = CorpApi(TestConf['CORP_ID'], TestConf['CONTACT_SYNC_SECRET'])

try:
    # 创建用户
    response = api.httpCall(
        CORP_API_TYPE['USER_CREATE'],
        {
            'userid': 'zhangsan',
            'name': 'zhangsanfeng',
            'mobile': '131488888888',
            'email': 'zhangsan@company.com',
            'department': 1,  # 部门ID
        }
    )
    print("用户创建成功:", response)
    
    # 获取用户信息
    user_info = api.httpCall(
        CORP_API_TYPE['USER_GET'],
        {'userid': 'zhangsan'}
    )
    print("用户信息:", user_info)
    
    # 删除用户
    delete_response = api.httpCall(
        CORP_API_TYPE['USER_DELETE'],
        {'userid': 'zhangsan'}
    )
    print("用户删除成功:", delete_response)
    
except ApiException as e:
    print("API错误:", e.errCode, e.errMsg)
except Exception as e:
    print("其他错误:", e)
```

## 📁 项目结构

```
weworkapi_python/
├── api/                          # API接口模块
│   ├── examples/                 # 使用示例
│   │   ├── UserTest.py          # 用户管理示例
│   │   ├── MessageTest.py       # 消息发送示例
│   │   ├── AppChatTest.py       # 群聊管理示例
│   │   ├── MiniprogramTest.py   # 小程序示例
│   │   └── TestConf.py          # 配置文件示例
│   └── src/                     # 核心源码
│       ├── AbstractApi.py       # API基础类
│       ├── CorpApi.py          # 企业微信API
│       ├── ServiceCorpApi.py   # 服务商企业API
│       └── ServiceProviderApi.py # 服务提供商API
├── callback/                    # 回调消息处理（Python2, XML）
├── callback_python3/           # 回调消息处理（Python3, XML）
├── callback_json/              # 回调消息处理（Python2, JSON）
├── callback_json_python3/      # 回调消息处理（Python3, JSON）
├── conf.py                     # 全局配置
└── README.md                   # 项目文档
```

## 🛠️ 开发调试

### 调试模式
```python
# 在 conf.py 中设置
DEBUG = True  # 开启后会打印请求URL和参数
```

### 错误处理
企业微信API调用可能遇到的常见错误：

```python
import sys
sys.path.append("../src/")

from CorpApi import CorpApi, CORP_API_TYPE, ApiException
from TestConf import TestConf

api = CorpApi(TestConf['CORP_ID'], TestConf['APP_SECRET'])

try:
    response = api.httpCall(CORP_API_TYPE['USER_GET'], {'userid': 'test'})
    print("成功:", response)
    
except ApiException as e:
    # 处理企业微信API特定错误
    if e.errCode == 60111:
        print("错误: 用户不存在")
    elif e.errCode == 40014:
        print("错误: access_token不合法")
    elif e.errCode == 42001:
        print("错误: access_token超时，自动刷新后重试")
    else:
        print(f"API错误: {e.errCode} - {e.errMsg}")
        
except Exception as e:
    print(f"其他错误: {e}")
```

**常见错误码说明：**
- `40014`: access_token不合法 - 令牌无效或已过期
- `42001`: access_token超时 - 令牌已超时，SDK会自动刷新
- `60111`: userid不存在 - 指定的用户ID不存在
- `60112`: userid不合法 - 用户ID格式不正确

---

⭐ 如果这个项目对你有帮助，请给它一个星标！
