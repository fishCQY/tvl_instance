# 学校:华南理工大学
# 姓名:陈秋余
# file: tag.py
# 开发时间:2025/1/18
import os
import csv
import cv2

# 使用 OpenCV 提取背景
def extract_background(tactile_path: str):
    # 使用 OpenCV 读取图像，假设背景提取通过模糊或其他方法来实现
    img = cv2.imread(tactile_path)
    if img is None:
        raise ValueError(f"Image at {tactile_path} could not be loaded.")
    # 模拟提取背景的简单方法：这里假设使用高斯模糊作为背景提取
    background = cv2.GaussianBlur(img, (21, 21), 0)

    return background


# 扩展标签处理
def get_caption_for_label(label: str):
    # 标签与分类的映射
    label_map = {
        '-1': 'Inconclusive',
        '0': 'Concrete',
        '1': 'Plastic',
        '2': 'Glass',
        '3': 'Wood',
        '4': 'Metal',
        '5': 'Brick',
        '6': 'Tile',
        '7': 'Leather',
        '8': 'Synthetic Fabric',
        '9': 'Natural Fabric',
        '10': 'Rubber',
        '11': 'Paper',
        '12': 'Tree',
        '13': 'Grass',
        '14': 'Soil',
        '15': 'Rock',
        '16': 'Gravel',
        '17': 'Sand',
        '18': 'Plants',
        '19': 'Others',
    }

    # 返回对应的 caption，若标签不存在则返回 'Unknown'
    return label_map.get(label.strip(), 'Unknown')


# 从 category_reference.txt 中加载类别参考
def load_category_references(category_file: str):
    category_map = {}
    with open(category_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            # 跳过空行
            if not line:
                continue

            # 处理标签和类别
            if ':' in line:
                try:
                    label, category = line.split(':')
                    label = label.strip()  # 去除标签中的空格
                    category = category.strip()  # 去除类别中的空格
                    category_map[label] = category
                except ValueError:
                    print(f"Warning: Skipping malformed line: {line}")
            # 如果行包含逗号，则按逗号分隔
            elif ',' in line:
                try:
                    label, category = line.split(',')
                    category_map[label.strip()] = category.strip()
                except ValueError:
                    print(f"Warning: Skipping malformed line: {line}")
            else:
                print(f"Warning: Skipping line with invalid format: {line}")

    return category_map


# 将 txt 数据转换为 CSV
def convert_txt_to_csv(txt_file: str, category_file: str, output_csv: str):
    category_map = load_category_references(category_file)

    # 打开txt文件读取数据
    with open(txt_file, 'r') as f:
        lines = f.readlines()

    data_rows = []
    for line in lines:
        # 处理每行数据
        filepath, label = line.strip().split(',')

        # 打印标签，检查它是否与 category_map 中的键匹配
        print(f"Processing label: {label.strip()}")  # 打印读取的标签

        # 获取 caption
        caption = get_caption_for_label(label.strip())  # 使用扩展的映射

        print(f"Caption: {caption}")  # 打印找到的 caption

        # 构建路径
        vision_path = os.path.join(os.path.dirname(filepath), 'vision', os.path.basename(filepath))
        tactile_path = os.path.join(os.path.dirname(filepath), 'tactile', os.path.basename(filepath))
        tactile_background_path = os.path.join(os.path.dirname(filepath), 'tactile',
                                               os.path.basename(filepath))  # 可以根据需要提取背景

        # 将数据添加到列表
        data_rows.append([vision_path, tactile_path, tactile_background_path, caption])

    # 写入CSV
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['url', 'tactile', 'tactile_background', 'caption'])  # 表头
        writer.writerows(data_rows)

    print(f"Data successfully written to {output_csv}")


# 主程序
def main():
    txt_file = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/filtered_label.txt'  # 输入的txt文件路径
    category_file = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/category_reference.txt'  # category_reference.txt路径
    output_csv = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/data1/output.csv'  # 输出的csv文件路径

    convert_txt_to_csv(txt_file, category_file, output_csv)


if __name__ == '__main__':
    main()
