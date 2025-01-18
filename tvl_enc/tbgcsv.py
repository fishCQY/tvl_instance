import csv

# 更新 CSV 文件中的 tactile_background 列
def update_tactile_background(csv_file: str):
    # 读取现有的 CSV 文件内容
    rows = []
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # 获取标题行索引
    header = rows[0]
    tactile_background_idx = header.index('tactile_background')  # 找到 'tactile_background' 列

    # 遍历 CSV 文件中的每一行，更新 tactile_background 列
    for row in rows[1:]:
        # 将 tactile_background 列替换为固定的相对路径
        row[tactile_background_idx] = '20220515_135653/tactile_bg_latent.jpg'

    # 将更新后的数据写回 CSV 文件
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"CSV file updated successfully: {csv_file}")


# 主程序
def main():
    csv_file = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/data1/output.csv'  # CSV 文件路径
    update_tactile_background(csv_file)


if __name__ == '__main__':
    main()
