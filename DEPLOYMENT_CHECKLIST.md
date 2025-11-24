# 🚀 Railway 一键部署检查清单

## ✅ 部署前检查

### 1. 代码准备
- [x] 所有配置文件已创建
  - [x] `Procfile` - 启动配置
  - [x] `railway.json` - Railway 配置
  - [x] `runtime.txt` - Python 版本
  - [x] `.railwayignore` - 忽略文件
  - [x] `.gitignore` - Git 忽略
  - [x] `README.md` - 项目说明
  
- [x] 依赖文件已更新
  - [x] `feedback_app/requirements.txt` 包含生产依赖
  - [x] 添加了 `gunicorn` 
  - [x] 添加了 `psycopg2-binary`

- [x] 代码已优化
  - [x] `app.py` 支持 PORT 环境变量
  - [x] 配置支持环境变量
  - [x] 数据库自动初始化

### 2. 准备密钥
- [ ] 运行密钥生成器
  ```bash
  python generate_keys.py
  ```
- [ ] 复制生成的 `SECRET_KEY`
- [ ] 复制生成的 `JWT_SECRET_KEY`
- [ ] 设置安全的管理员密码

### 3. Git 仓库
- [ ] 代码已提交到 Git
  ```bash
  git add .
  git commit -m "准备 Railway 部署"
  ```
- [ ] 代码已推送到 GitHub/GitLab
  ```bash
  git push origin main
  ```

## 🔧 Railway 部署步骤

### 步骤 1: 创建项目
1. [ ] 访问 https://railway.app
2. [ ] 登录/注册账号
3. [ ] 点击 **"New Project"**
4. [ ] 选择 **"Deploy from GitHub repo"**
5. [ ] 选择你的仓库

### 步骤 2: 添加数据库
1. [ ] 点击 **"+ New"**
2. [ ] 选择 **"Database"** → **"Add PostgreSQL"**
3. [ ] 等待数据库创建完成

### 步骤 3: 配置环境变量
1. [ ] 点击 Web Service（你的应用）
2. [ ] 选择 **"Variables"** 标签
3. [ ] 添加以下变量：

#### 必需变量
```
DATABASE_URI = ${{Postgres.DATABASE_URL}}
SECRET_KEY = <从 generate_keys.py 复制>
JWT_SECRET_KEY = <从 generate_keys.py 复制>
ADMIN_USERNAME = admin
ADMIN_PASSWORD = <设置强密码>
```

#### 可选变量（使用默认值可不设置）
```
PAGINATION_DEFAULT_PAGE = 1
PAGINATION_DEFAULT_SIZE = 10
PAGINATION_MAX_SIZE = 100
```

### 步骤 4: 部署
1. [ ] Railway 自动开始构建
2. [ ] 查看 **"Deployments"** 标签监控进度
3. [ ] 等待部署成功（约2-3分钟）

### 步骤 5: 生成域名
1. [ ] 点击 **"Settings"** 标签
2. [ ] 找到 **"Domains"** 部分
3. [ ] 点击 **"Generate Domain"**
4. [ ] 复制生成的域名

## ✨ 部署后验证

### 1. 测试健康检查
```bash
curl https://your-app.railway.app/api/feedback
```
预期返回：包含 `items` 和 `pagination` 的 JSON 响应

### 2. 测试管理员登录
```bash
curl -X POST https://your-app.railway.app/api/admin/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"your_password"}'
```
预期返回：包含 `access_token` 的 JSON 响应

### 3. 测试创建反馈
```bash
curl -X POST https://your-app.railway.app/api/feedback \
  -H "Content-Type: application/json" \
  -d '{"username":"测试用户","email":"test@example.com","content":"测试反馈"}'
```
预期返回：包含 `id` 的 JSON 响应

### 4. 测试创建任务
```bash
curl -X POST https://your-app.railway.app/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"测试任务","description":"任务描述"}'
```
预期返回：包含任务详情的 JSON 响应

## 📊 监控和维护

### 查看日志
1. [ ] 在 Railway Dashboard 中选择服务
2. [ ] 点击 **"Logs"** 标签
3. [ ] 查看实时日志输出

### 查看指标
1. [ ] 点击 **"Metrics"** 标签
2. [ ] 监控 CPU、内存、请求量

### 更新应用
1. [ ] 本地修改代码
2. [ ] 提交并推送到 GitHub
   ```bash
   git add .
   git commit -m "更新说明"
   git push
   ```
3. [ ] Railway 自动检测并重新部署

## 🎯 部署成功标志

- [x] 服务状态显示为 **"Active"**
- [x] 健康检查通过（绿色对勾）
- [x] 可以通过域名访问 API
- [x] 数据库连接正常
- [x] 管理员登录成功
- [x] API 端点响应正常

## 🔍 故障排查

### 部署失败
- [ ] 查看 **"Deployments"** 中的构建日志
- [ ] 检查 `requirements.txt` 格式
- [ ] 验证 Python 版本兼容性

### 数据库连接失败
- [ ] 确认 `DATABASE_URI` 使用 `${{Postgres.DATABASE_URL}}`
- [ ] 检查 PostgreSQL 服务是否运行
- [ ] 查看日志中的具体错误信息

### 502 Bad Gateway
- [ ] 等待服务完全启动（需要1-2分钟）
- [ ] 检查健康检查配置
- [ ] 查看应用日志是否有错误

### 认证失败
- [ ] 确认环境变量 `SECRET_KEY` 和 `JWT_SECRET_KEY` 已设置
- [ ] 验证管理员用户名和密码
- [ ] 检查 JWT 令牌是否正确传递

## 📞 获取帮助

- Railway 文档: https://docs.railway.app/
- Railway 社区: https://discord.gg/railway
- 项目文档: README.md
- 详细指南: Railway部署指南.md

---

## 🎉 完成！

当所有检查项都打勾后，你的应用就成功部署到 Railway 了！

**你的应用地址**: https://your-app.railway.app

记得：
- 📝 保存好你的域名
- 🔐 妥善保管密钥和密码
- 📊 定期查看日志和指标
- 🔄 享受自动部署的便利！

