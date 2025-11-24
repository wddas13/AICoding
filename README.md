# Flask 反馈与任务管理系统

一个基于 Flask 的后端 API 系统，提供用户反馈管理和待办任务管理功能。

## ✨ 功能特性

- 📝 **用户反馈管理** - 提交、查看、回复用户反馈
- ✅ **待办任务管理** - 创建、更新、删除待办事项
- 🔐 **管理员认证** - JWT 令牌认证
- 📄 **分页查询** - 灵活的分页参数配置
- 🔒 **CORS 支持** - 跨域资源共享配置

## 🚀 一键部署到 Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/feedback-app)

点击上方按钮即可一键部署到 Railway！

### 部署步骤

1. **点击部署按钮** - 授权 Railway 访问你的 GitHub
2. **添加数据库** - Railway 会提示添加 PostgreSQL 数据库
3. **配置环境变量** - 设置必需的环境变量（见下方）
4. **自动部署** - Railway 自动构建并部署应用

## 📋 环境变量配置

### 必需变量

| 变量名 | 说明 | 获取方式 |
|--------|------|----------|
| `DATABASE_URI` | 数据库连接字符串 | Railway 自动提供：`${{Postgres.DATABASE_URL}}` |
| `SECRET_KEY` | Flask 密钥 | 运行 `python generate_keys.py` |
| `JWT_SECRET_KEY` | JWT 密钥 | 运行 `python generate_keys.py` |
| `ADMIN_USERNAME` | 管理员用户名 | 自定义（建议：admin） |
| `ADMIN_PASSWORD` | 管理员密码 | 自定义（必须设置强密码） |

### 生成安全密钥

```bash
python generate_keys.py
```

复制输出的密钥到 Railway 环境变量中。

### 可选变量

```bash
PAGINATION_DEFAULT_PAGE=1      # 默认页码
PAGINATION_DEFAULT_SIZE=10     # 每页条数
PAGINATION_MAX_SIZE=100        # 最大每页条数
```

## 🛠️ 本地开发

### 1. 安装依赖

```bash
cd feedback_app
pip install -r requirements.txt
```

### 2. 配置环境变量

参考 `ENV_TEMPLATE.txt` 设置本地环境变量。

### 3. 运行应用

```bash
python app.py
```

应用将在 http://localhost:5000 启动。

## 📚 API 文档

### 反馈管理 API

- `GET /api/feedback` - 获取反馈列表
- `POST /api/feedback` - 提交新反馈
- `GET /api/feedback/<id>` - 获取单个反馈详情
- `PUT /api/feedback/<id>/reply` - 回复反馈（需认证）

### 任务管理 API

- `GET /api/tasks` - 获取任务列表
- `POST /api/tasks` - 创建新任务
- `GET /api/tasks/<id>` - 获取任务详情
- `PUT /api/tasks/<id>` - 更新任务
- `DELETE /api/tasks/<id>` - 删除任务
- `PUT /api/tasks/<id>/toggle` - 切换任务完成状态

### 管理员 API

- `POST /api/admin/login` - 管理员登录
- `GET /api/admin/feedback` - 获取所有反馈（需认证）

详细文档请查看：
- [接口文档.md](接口文档.md)
- [待办事项API文档.md](待办事项API文档.md)
- [待办事项前端对接文档.md](待办事项前端对接文档.md)

## 🏗️ 技术栈

- **框架**: Flask 2.3+
- **数据库**: PostgreSQL (生产) / SQLite (开发)
- **ORM**: Flask-SQLAlchemy
- **认证**: Flask-JWT-Extended
- **CORS**: Flask-CORS
- **WSGI 服务器**: Gunicorn

## 📁 项目结构

```
feedback_app/
├── app.py              # 应用入口
├── config.py           # 配置文件
├── extensions.py       # Flask 扩展初始化
├── models/             # 数据模型
│   ├── feedback.py     # 反馈模型
│   └── task.py         # 任务模型
├── routes/             # 路由处理
│   ├── feedback_api.py # 反馈 API
│   ├── task_api.py     # 任务 API
│   └── admin_api.py    # 管理员 API
├── services/           # 业务逻辑
│   ├── feedback_service.py
│   ├── task_service.py
│   └── admin_service.py
└── utils/              # 工具函数
    ├── auth.py         # 认证装饰器
    ├── pagination.py   # 分页工具
    └── validators.py   # 数据验证
```

## 🔧 部署配置文件

- `Procfile` - Railway/Heroku 启动配置
- `railway.json` - Railway 平台配置
- `runtime.txt` - Python 版本声明
- `.railwayignore` - 部署忽略文件
- `.gitignore` - Git 忽略配置

## 📖 详细部署指南

查看 [Railway部署指南.md](Railway部署指南.md) 获取完整的部署步骤和常见问题解答。

## 💰 成本估算

使用 Railway 部署：
- **免费额度**: $5/月
- **预计成本**: $5-20/月（小型应用）
- **优势**: 比 Heroku 便宜 75%

## 🆘 常见问题

### 部署失败？

1. 检查日志中的错误信息
2. 确认所有环境变量已正确设置
3. 验证数据库连接是否正常

### 数据库连接失败？

确保 `DATABASE_URI` 设置为：
```
${{Postgres.DATABASE_URL}}
```

### 应用无法访问？

1. 检查服务是否已成功部署
2. 等待健康检查通过（约1-2分钟）
3. 查看 Railway 日志排查问题

## 📞 技术支持

- [Railway 文档](https://docs.railway.app/)
- [Flask 文档](https://flask.palletsprojects.com/)
- [项目 Issues](https://github.com/your-repo/issues)

## 📄 许可证

MIT License

---

**快速开始**: 点击上方 "Deploy on Railway" 按钮，3分钟完成部署！ 🚀

