# Railway 部署指南

## 📋 准备工作

在部署到 Railway 之前，请确保：
- ✅ 代码已推送到 GitHub/GitLab/Bitbucket 仓库
- ✅ 项目已包含所需的配置文件（已自动生成）
- ✅ 注册 Railway 账号：https://railway.app

## 🚀 快速部署步骤

### 1. 创建新项目

1. 访问 [Railway Dashboard](https://railway.app/dashboard)
2. 点击 **"New Project"**
3. 选择 **"Deploy from GitHub repo"**
4. 授权 Railway 访问你的 GitHub 仓库
5. 选择 `AICoding` 仓库

### 2. 添加 PostgreSQL 数据库

1. 在项目画布中，点击 **"+ New"**
2. 选择 **"Database"** → **"Add PostgreSQL"**
3. Railway 会自动创建数据库并生成连接字符串

### 3. 配置环境变量

在 Railway 项目设置中添加以下环境变量：

#### 必需变量

| 变量名 | 说明 | 示例值 |
|--------|------|--------|
| `DATABASE_URI` | 数据库连接字符串 | `${{Postgres.DATABASE_URL}}` |
| `SECRET_KEY` | Flask 密钥 | 生成随机字符串 |
| `JWT_SECRET_KEY` | JWT 密钥 | 生成随机字符串 |
| `ADMIN_USERNAME` | 管理员用户名 | `admin` |
| `ADMIN_PASSWORD` | 管理员密码 | `your_secure_password` |

#### 可选变量

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `PAGINATION_DEFAULT_PAGE` | `1` | 默认页码 |
| `PAGINATION_DEFAULT_SIZE` | `10` | 每页条数 |
| `PAGINATION_MAX_SIZE` | `100` | 最大每页条数 |

#### 设置数据库连接

1. 在 Web Service 的 **Variables** 标签中
2. 添加变量：`DATABASE_URI`
3. 值设置为：`${{Postgres.DATABASE_URL}}`
   - Railway 会自动将这个引用替换为实际的数据库连接字符串

#### 生成安全密钥

在终端运行以下命令生成随机密钥：

```bash
# 生成 SECRET_KEY
python -c "import secrets; print(secrets.token_hex(32))"

# 生成 JWT_SECRET_KEY
python -c "import secrets; print(secrets.token_hex(32))"
```

### 4. 部署服务

1. Railway 会自动检测到项目配置并开始构建
2. 构建完成后，服务会自动部署
3. 点击 **"Generate Domain"** 获取公开访问地址

### 5. 验证部署

访问生成的域名，测试以下端点：

```bash
# 健康检查（反馈列表）
https://your-app.railway.app/api/feedback

# 管理员登录
curl -X POST https://your-app.railway.app/api/admin/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"your_password"}'
```

## 📁 已添加的配置文件

### 1. `Procfile`
定义启动命令：
```
web: gunicorn --chdir feedback_app --bind 0.0.0.0:$PORT app:app
```

### 2. `railway.json`
Railway 平台配置，包括：
- 构建命令
- 启动命令
- 健康检查配置
- 重启策略

### 3. `.railwayignore`
指定部署时忽略的文件：
- 缓存文件 (`__pycache__`)
- 本地数据库文件 (`*.db`)
- 测试文件
- IDE 配置文件

### 4. `feedback_app/requirements.txt`
已添加生产环境依赖：
- `gunicorn` - WSGI HTTP 服务器
- `psycopg2-binary` - PostgreSQL 数据库驱动

## 🔧 高级配置

### 自定义域名

1. 在 Railway 项目设置中选择 **"Settings"**
2. 找到 **"Domains"** 部分
3. 点击 **"Add Custom Domain"**
4. 添加你的域名并按提示配置 DNS

### 扩展配置

Railway 支持以下扩展选项：
- **自动扩展**：根据流量自动调整资源
- **环境变量**：支持多环境配置（开发/生产）
- **健康检查**：自动监控服务状态
- **日志查看**：实时查看应用日志

### 监控和日志

1. 在 Railway Dashboard 中点击你的服务
2. 选择 **"Logs"** 标签查看实时日志
3. 选择 **"Metrics"** 标签查看性能指标

## 💰 费用估算

Railway 定价（2024年11月）：
- **免费额度**：$5/月使用额度
- **按用量付费**：超出部分按实际使用计费
- **预计成本**：小型应用约 $5-20/月

详细定价：https://railway.app/pricing

## 🔄 持续部署

配置完成后，每次推送到 GitHub 主分支：
1. Railway 自动检测代码更改
2. 自动构建新版本
3. 自动部署到生产环境
4. 零停机时间更新

## ⚠️ 注意事项

1. **数据库迁移**：首次部署时，Flask 会自动创建表结构
2. **环境变量安全**：不要在代码中硬编码敏感信息
3. **日志监控**：定期检查日志，确保服务正常运行
4. **备份策略**：定期备份 PostgreSQL 数据库

## 🆘 常见问题

### 部署失败

1. 检查日志中的错误信息
2. 确认所有环境变量已正确设置
3. 验证 `requirements.txt` 中的依赖版本

### 数据库连接失败

1. 确认 `DATABASE_URI` 环境变量已设置
2. 检查是否使用了 `${{Postgres.DATABASE_URL}}` 引用
3. 确保安装了 `psycopg2-binary`

### 应用无法访问

1. 检查服务是否已成功部署
2. 确认防火墙规则
3. 验证域名 DNS 配置（如果使用自定义域名）

## 📚 相关资源

- [Railway 官方文档](https://docs.railway.app/)
- [Flask 部署指南](https://flask.palletsprojects.com/en/latest/deploying/)
- [Gunicorn 文档](https://docs.gunicorn.org/)

## ✅ 部署检查清单

- [ ] 代码已推送到远程仓库
- [ ] Railway 项目已创建
- [ ] PostgreSQL 数据库已添加
- [ ] 所有环境变量已设置
- [ ] 服务已成功部署
- [ ] 域名已生成或配置
- [ ] API 端点测试通过
- [ ] 管理员账号可登录

---

部署完成！🎉 你的应用现在已经在 Railway 上运行了。

