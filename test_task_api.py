"""
待办事项 API 测试脚本
使用方法：先启动 Flask 应用，然后运行此脚本
"""

import requests
import json

BASE_URL = "http://localhost:5000/api"


def test_add_task():
    """测试添加任务"""
    print("=== 测试添加任务 ===")
    data = {
        "title": "完成项目文档",
        "description": "编写 API 接口文档和使用说明"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=data)
    print(f"状态码: {response.status_code}")
    print(f"响应: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
    return response.json().get("data", {}).get("id")


def test_list_tasks():
    """测试列出所有任务"""
    print("\n=== 测试列出所有任务 ===")
    response = requests.get(f"{BASE_URL}/tasks")
    print(f"状态码: {response.status_code}")
    print(f"响应: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")


def test_delete_task(task_id):
    """测试删除任务"""
    print(f"\n=== 测试删除任务 (ID: {task_id}) ===")
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    print(f"状态码: {response.status_code}")
    print(f"响应: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")


if __name__ == "__main__":
    try:
        # 添加几个任务
        task_id_1 = test_add_task()
        
        data2 = {
            "title": "学习 Flask",
            "description": "深入学习 Flask 框架"
        }
        response2 = requests.post(f"{BASE_URL}/tasks", json=data2)
        task_id_2 = response2.json().get("data", {}).get("id")
        
        # 列出所有任务
        test_list_tasks()
        
        # 删除第一个任务
        if task_id_1:
            test_delete_task(task_id_1)
        
        # 再次列出所有任务，验证删除是否成功
        test_list_tasks()
        
    except requests.exceptions.ConnectionError:
        print("错误: 无法连接到服务器，请确保 Flask 应用正在运行 (python feedback_app/app.py)")
    except Exception as e:
        print(f"错误: {e}")

