# 待办事项 API 文档

## 接口概览

本文档描述待办事项管理 API 的使用方法。

### 基础 URL
```
http://localhost:5000/api
```

---

## 接口列表

### 1. 列出所有任务

**请求**
```
GET /tasks
```

**响应示例**
```json
{
  "msg": "success",
  "data": [
    {
      "id": 1,
      "title": "完成项目文档",
      "description": "编写 API 接口文档和使用说明",
      "status": "pending",
      "create_time": "2025-11-24T10:30:00",
      "update_time": "2025-11-24T10:30:00"
    },
    {
      "id": 2,
      "title": "学习 Flask",
      "description": "深入学习 Flask 框架",
      "status": "pending",
      "create_time": "2025-11-24T10:35:00",
      "update_time": "2025-11-24T10:35:00"
    }
  ]
}
```

---

### 2. 新增任务

**请求**
```
POST /tasks
Content-Type: application/json
```

**请求参数**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| title | string | 是 | 任务标题 |
| description | string | 否 | 任务描述 |

**请求示例**
```json
{
  "title": "完成项目文档",
  "description": "编写 API 接口文档和使用说明"
}
```

**响应示例**
```json
{
  "msg": "success",
  "data": {
    "id": 1,
    "title": "完成项目文档",
    "description": "编写 API 接口文档和使用说明",
    "status": "pending",
    "create_time": "2025-11-24T10:30:00"
  }
}
```

**错误响应示例**
```json
{
  "msg": "invalid",
  "errors": ["标题不能为空"]
}
```

---

### 3. 删除任务

**请求**
```
DELETE /tasks/<id>
```

**路径参数**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | integer | 是 | 任务 ID |

**请求示例**
```
DELETE /tasks/1
```

**成功响应**
```json
{
  "msg": "success"
}
```

**错误响应**
```json
{
  "msg": "error",
  "errors": ["任务不存在"]
}
```

---

## 使用示例

### cURL 示例

**列出所有任务**
```bash
curl http://localhost:5000/api/tasks
```

**新增任务**
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"完成项目文档","description":"编写 API 接口文档"}'
```

**删除任务**
```bash
curl -X DELETE http://localhost:5000/api/tasks/1
```

### Python 示例

```python
import requests

BASE_URL = "http://localhost:5000/api"

# 新增任务
response = requests.post(f"{BASE_URL}/tasks", json={
    "title": "完成项目文档",
    "description": "编写 API 接口文档"
})
print(response.json())

# 列出所有任务
response = requests.get(f"{BASE_URL}/tasks")
print(response.json())

# 删除任务
response = requests.delete(f"{BASE_URL}/tasks/1")
print(response.json())
```

---

## 启动应用

在项目根目录下运行：

```bash
cd feedback_app
python app.py
```

应用将在 `http://localhost:5000` 启动。

---

## 测试

运行测试脚本：

```bash
# 确保应用正在运行
python test_task_api.py
```

