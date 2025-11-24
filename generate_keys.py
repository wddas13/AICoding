#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成用于 Railway 部署的安全密钥
"""
import secrets
import sys
import io

# 设置 UTF-8 输出（Windows 兼容）
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 60)
print("Railway 部署密钥生成器")
print("=" * 60)
print()

# 生成 SECRET_KEY
secret_key = secrets.token_hex(32)
print("SECRET_KEY:")
print(secret_key)
print()

# 生成 JWT_SECRET_KEY
jwt_secret_key = secrets.token_hex(32)
print("JWT_SECRET_KEY:")
print(jwt_secret_key)
print()

print("=" * 60)
print("请将上述密钥复制到 Railway 环境变量中")
print("=" * 60)
print()
print("Railway 配置步骤：")
print("1. 进入 Railway 项目")
print("2. 选择你的服务")
print("3. 点击 'Variables' 标签")
print("4. 添加上述环境变量")
print()
print("提示：已生成 64 位十六进制密钥，安全性高！")
print()

