# 学校:华南理工大学
# 姓名:陈秋余
# file: contact2.py
# 开发时间:2025/1/19


import os
import json

# 获取 tactile 目录下的所有图片路径并格式化为 JSON 格式
def generate_tactile_json(tactile_dir: str, contact_json_path: str):
    tactile_images = []

    # 遍历 tactile 目录中的图片
    for root, dirs, files in os.walk(tactile_dir):
        for file in files:
            # 只处理图片文件（假设为 .jpg 格式）
            if file.endswith('.jpg'):
                relative_path = os.path.relpath(os.path.join(root, file), tactile_dir)
                # 添加前缀 '20220515_135653/tactile/'
                tactile_images.append('20220515_135653/tactile/' + relative_path.replace("\\", "/"))

    # 构建所需的 JSON 格式
    tactile_json = {"tactile": tactile_images}

    # 读取 contact.json 文件
    try:
        with open(contact_json_path, 'r') as f:
            contact_data = json.load(f)
        tactile_json["contact"] = contact_data  # 将 contact.json 中的内容合并到生成的 JSON 数据中
    except json.JSONDecodeError:
        print(f"Error: {contact_json_path} is not a valid JSON file or is empty.")
        tactile_json["contact"] = []  # 如果文件无效或为空，使用空列表填充 "contact" 字段
    except FileNotFoundError:
        print(f"Error: {contact_json_path} not found.")
        tactile_json["contact"] = []  # 如果文件不存在，使用空列表填充 "contact" 字段

    # 输出结果为 JSON 文件
    output_json_path = os.path.join(tactile_dir, 'tactile_data.json')
    with open(output_json_path, 'w') as f:
        json.dump(tactile_json, f, indent=4)

    print(f"tactile data JSON has been saved to: {output_json_path}")


# 主程序
def main():
    tactile_dir = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/data1'  # tactile 文件夹路径
    contact_json_path = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/data1/contact.json'  # contact.json 文件路径
    generate_tactile_json(tactile_dir, contact_json_path)


if __name__ == '__main__':
    main()
