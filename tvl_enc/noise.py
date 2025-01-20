# 学校:华南理工大学
# 姓名:陈秋余
# file: noise.py
# 开发时间:2025/1/20
import os
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import random

# 添加噪声的函数
def add_noise(image, noise_type='brightness'):
    """
    向图像添加噪声，支持多种噪声类型：'brightness', 'contrast', 'defocus_blur', 'impulse_noise'
    """
    if noise_type == 'brightness':
        enhancer = ImageEnhance.Brightness(image)
        factor = random.uniform(0.5, 1.5)  # 随机变化亮度
        return enhancer.enhance(factor)

    elif noise_type == 'contrast':
        enhancer = ImageEnhance.Contrast(image)
        factor = random.uniform(0.5, 1.5)  # 随机变化对比度
        return enhancer.enhance(factor)

    elif noise_type == 'defocus_blur':
        radius = random.uniform(1, 5)  # 随机选择模糊程度
        return image.filter(ImageFilter.GaussianBlur(radius))

    elif noise_type == 'impulse_noise':
        img_array = np.array(image)
        noise = np.random.randn(*img_array.shape) * 30  # 使用正态分布噪声
        noisy_img = img_array + noise
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
        return Image.fromarray(noisy_img)

    else:
        raise ValueError(
            "Unsupported noise type. Choose from: 'brightness', 'contrast', 'defocus_blur', 'impulse_noise'.")


# 加载并处理图像
def process_images(input_dir):
    # 获取输入文件夹中的所有图像文件
    image_files = [f for f in os.listdir(input_dir) if f.endswith(('jpg', 'png', 'jpeg'))]

    # 对每张图像应用噪声并保存
    for image_file in image_files:
        image_path = os.path.join(input_dir, image_file)
        image = Image.open(image_path)

        # 随机选择噪声类型
        noise_types = ['brightness', 'contrast', 'defocus_blur', 'impulse_noise']
        chosen_noise = random.choice(noise_types)

        # 添加噪声
        noisy_image = add_noise(image, noise_type=chosen_noise)

        # 保存加噪后的图像，直接覆盖原图像
        noisy_image.save(image_path)
        print(f"Processed and replaced: {image_file}")


# 主函数
def main():
    # 设置路径
    root_folder = '/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tvl_dataset'  # 替换为tvl_dataset的路径
    data_folders = ['ssvtp/images_rgb']  # 需要处理的文件夹路径列表

    for data_folder in data_folders:
        # 获取data文件夹路径
        data_folder_path = os.path.join(root_folder, data_folder)

        # 遍历子目录中的vision文件夹
        for subdir in os.listdir(data_folder_path):
            subdir_path = os.path.join(data_folder_path, subdir)
            vision_folder = os.path.join(subdir_path)

            # 确保vision文件夹存在
            if os.path.exists(vision_folder):
                # 处理图像并直接覆盖原vision文件夹中的图像
                process_images(vision_folder)
            else:
                print(f"Vision folder does not exist for {subdir_path}")


# 运行主函数
main()
