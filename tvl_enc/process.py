# 学校:华南理工大学
# 姓名:陈秋余
# file: process.py
# 开发时间:2025/1/19

import os


def filter_labels(txt_file: str, output_txt: str):
    valid_lines = []

    # 读取原始 label.txt 文件
    with open(txt_file, 'r') as f:
        lines = f.readlines()

    # 遍历每一行
    for line in lines:
        line = line.strip()
        # 获取文件路径部分
        filepath, label = line.split(',')
        # 获取文件的上一级目录
        parent_dir = os.path.basename(os.path.dirname(filepath))

        # 检查上一级目录是否为 '20220515_135653'
        if parent_dir == '20220515_135653':
            valid_lines.append(line)

    # 将筛选后的有效条目写入新文件
    with open(output_txt, 'w') as f:
        f.write('\n'.join(valid_lines) + '\n')

    print(f"Filtered labels written to {output_txt}")


# 主程序
def main():
    txt_file = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/label.txt'  # 输入的txt文件路径
    output_txt = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/filtered_label.txt'  # 输出的筛选后的txt文件路径

    filter_labels(txt_file, output_txt)


if __name__ == '__main__':
    main()

