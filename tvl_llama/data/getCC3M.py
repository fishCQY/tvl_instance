# 学校:华南理工大学
# 姓名:陈秋余
# file: getCC3M.py
# 开发时间:2025/1/18

import json
import csv
import os

# 假设 JSON 数据存储在 'metadata.json' 文件中
json_file_path = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/metadata.json'  # 请根据需要修改路径
csv_file_path = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/cc3m.csv'  # 输出的 CSV 文件路径

# 假设文件夹路径是 '/path/to/images'，你可以根据实际情况修改
folder_path = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/CC3M'  # 请根据需要修改路径

# 读取 JSON 文件
with open(json_file_path, 'r') as f:
    data = json.load(f)

# 打开 CSV 文件准备写入
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # 写入 CSV 文件的表头
    writer.writerow(['url', 'caption'])

    # 遍历 JSON 数据并提取 'image' 和 'caption'
    for item in data:
        # 获取 'image' 字段，并将文件夹路径与图像文件名拼接
        image_path = os.path.join(folder_path, item.get('image', ''))  # 获取 'image' 字段，若不存在则默认为空字符串
        caption = item.get('caption', '')  # 获取 'caption' 字段，若不存在则默认为空字符串

        # 写入每一行到 CSV 文件
        writer.writerow([image_path, caption])

print(f"Data has been saved to {csv_file_path}")

