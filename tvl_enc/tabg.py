# 学校:华南理工大学
# 姓名:陈秋余
# file: tabg.py
# 开发时间:2025/1/19
import os
import cv2


# 提取背景图像并保存
def extract_background(tactile_path: str, save_dir: str, output_name: str):
    # 读取图像
    img = cv2.imread(tactile_path)
    if img is None:
        raise ValueError(f"Image at {tactile_path} could not be loaded.")

    # 使用高斯模糊提取背景
    background = cv2.GaussianBlur(img, (21, 21), 0)

    # 构建保存路径
    background_filename = os.path.join(save_dir, output_name)

    # 保存背景图像
    cv2.imwrite(background_filename, background)

    return background_filename


# 获取目录下每个子目录的第一张tactile图片
def process_subdirectories(data1_dir: str):
    # 遍历 data1 目录中的子目录
    for sub_dir in os.listdir(data1_dir):
        sub_dir_path = os.path.join(data1_dir, sub_dir)

        # 确保是目录
        if os.path.isdir(sub_dir_path):
            tactile_dir = os.path.join(sub_dir_path, 'tactile')

            # 确保 tactile 文件夹存在
            if os.path.exists(tactile_dir):
                # 获取 tactile 文件夹中的第一个图片文件
                tactile_images = [f for f in os.listdir(tactile_dir) if f.endswith('.jpg')]
                if tactile_images:
                    # 选择第一张图片
                    first_tactile_image = tactile_images[0]
                    tactile_image_path = os.path.join(tactile_dir, first_tactile_image)

                    # 提取背景并保存
                    background_filename = extract_background(tactile_image_path, sub_dir_path, 'tactile_background.jpg')
                    print(f"Background image saved: {background_filename}")

                    # 这里可以更新 CSV 或做进一步处理
                    # 如果需要保存路径，可以将其保存在某个文件中
                    tactile_background_relative_path = os.path.join(sub_dir, 'tactile_background.jpg')
                    print(f"Tactile background relative path: {tactile_background_relative_path}")
                else:
                    print(f"No tactile images found in {tactile_dir}")
            else:
                print(f"tactile directory does not exist in {sub_dir_path}")
        else:
            print(f"Skipping {sub_dir_path}, as it's not a directory.")


# 主程序
def main():
    data1_dir = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/data1'  # data1 的路径
    csv_file = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset/hct/data1/output.csv'  # CSV 文件路径
    process_subdirectories(data1_dir)


if __name__ == '__main__':
    main()
