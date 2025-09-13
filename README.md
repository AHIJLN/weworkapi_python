# 企业微信API Python SDK

[![Python Version](https://img.shields.io/badge/python-2.7%7C3.x-blue.svg)](https://www.python.org/)
[![WeWork API](https://img.shields.io/badge/WeWork-API-orange.svg)](https://work.weixin.qq.com/api/doc)

企业微信API的Python封装库，为开发者提供简单易用的企业微信API调用接口。由腾讯企业微信团队官方维护。

## 📋 项目简介

weworkapi_python 是腾讯企业微信团队开发的Python SDK，旨在简化开发者对企业微信API接口的调用。本库提供了完整的企业微信API封装，包括用户管理、部门管理、消息发送、应用管理等核心功能，支持企业内部应用和第三方服务商开发。

> **重要提示**：本库为官方示例代码，不保证完全无bug。生产环境使用请充分测试，一切以[官方API文档](https://work.weixin.qq.com/api/doc)为准。


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
