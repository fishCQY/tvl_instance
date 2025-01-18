# 学校:华南理工大学
# 姓名:陈秋余
# file: get_test.py
# 开发时间:2025/1/19
import csv
import random

# 从 output.csv 中提取 20% 的数据行并保存为 test.csv
def extract_20_percent_data(input_csv: str, output_csv: str):
    # 读取现有的 CSV 文件内容
    rows = []
    with open(input_csv, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # 获取表头
    header = rows[0]

    # 提取数据部分
    data_rows = rows[1:]

    # 随机选取 20% 的数据
    test_size = int(len(data_rows) * 0.2)
    test_data = random.sample(data_rows, test_size)

    # 将表头与提取的 20% 数据合并
    test_data.insert(0, header)

    # 将提取的数据写入 test.csv
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(test_data)

    print(f"20% data has been extracted and saved to {output_csv}")


# 主程序
def main():
    input_csv = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/data1/output.csv'  # 原始 CSV 文件路径
    output_csv = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/data1/test.csv'  # 保存的 CSV 文件路径
    extract_20_percent_data(input_csv, output_csv)


if __name__ == '__main__':
    main()
