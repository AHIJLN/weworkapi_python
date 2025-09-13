#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
from WXBizMsgCrypt import WXBizMsgCrypt
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

# 使用新生成的配置
TOKEN = "RkfXLVUoIrY"                                        # 新Token
ENCODING_AES_KEY = "cGbWuqbP6JbqqzofIKNoCuIUAqqnoi6NCvzXB1libMs"  # 新AESKey
CORP_ID = "wweb4d62f7030ca905"                              # 您的企业ID

# 初始化加密类
qy_api = [WXBizMsgCrypt(TOKEN, ENCODING_AES_KEY, CORP_ID)]

@app.route('/')
def index():
    return "WeWork Bot Server Running!"

@app.route('/hook_path', methods=['GET', 'POST'])
def hook_path():
    if request.method == 'GET':
        # 获取验证参数
        msg_signature = request.args.get('msg_signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')
        
        # 检查参数
        if not all([msg_signature, timestamp, nonce, echostr]):
            print(f"\n⚠️ 空参数请求，忽略")
            return "invalid parameters"
        
        print(f"\n{'='*60}")
        print(f"🔔 收到企业微信验证请求")
        print(f"{'='*60}")
        print(f"来源IP: {request.remote_addr}")
        print(f"msg_signature: {msg_signature}")
        print(f"timestamp: {timestamp}")
        print(f"nonce: {nonce}")
        print(f"echostr: {echostr[:30]}...")
        
        try:
            # 验证URL
            ret, reply_echostr = qy_api[0].VerifyURL(msg_signature, timestamp, nonce, echostr)
            
            if ret != 0:
                print(f"❌ 验证失败! 错误码: {ret}")
                if ret == -40001:
                    print("   签名验证失败")
                elif ret == -40005:
                    print("   企业ID不匹配")
                print(f"{'='*60}\n")
                return "failed"
            
            print(f"✅ 验证成功!")
            print(f"返回: {reply_echostr}")
            print(f"{'='*60}\n")
            return reply_echostr
            
        except Exception as e:
            print(f"❌ 异常: {str(e)}")
            print(f"{'='*60}\n")
            return "error"
    
    elif request.method == 'POST':
        # 处理消息（暂时返回success）
        return "success"

@app.route('/test')
def test():
    return f"""
    <h1>企业微信机器人配置</h1>
    <hr>
    <p><b>Token:</b> {TOKEN}</p >
    <p><b>EncodingAESKey:</b> {ENCODING_AES_KEY[:20]}...</p >
    <p><b>企业ID:</b> {CORP_ID}</p >
    <hr>
    <p>状态: ✅ 服务运行中</p >
    """

if __name__ == '__main__':
    print(f"\n{'='*60}")
    print("🚀 企业微信机器人服务启动")
    print(f"{'='*60}")
    print(f"📝 新配置信息：")
    print(f"   Token: {TOKEN}")
    print(f"   EncodingAESKey: {ENCODING_AES_KEY}")
    print(f"   企业ID: {CORP_ID}")
    print(f"{'='*60}")
    print("⏳ 等待企业微信验证...")
    print("💡 请在企业微信后台保存配置")
    print(f"{'='*60}\n")
    
    app.run(host='0.0.0.0', port=8066, debug=True)

