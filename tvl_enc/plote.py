# 学校:华南理工大学
# 姓名:陈秋余
# file: plote.py
# 开发时间:2025/1/19
import matplotlib.pyplot as plt
import json
import numpy as np
# 读取log.txt并解析数据
log_file = '/root/autodl-tmp/tvl/tvl_instance/tvl_enc/output_dir/log.txt'

# 初始化数据存储容器
epochs = []
train_lr = []
train_loss = []
train_tactile_vision = []
train_tactile_vision_acc1 = []
train_tactile_vision_acc5 = []
train_average_acc1 = []
train_average_acc5 = []

# 逐行读取并解析JSON数据
with open(log_file, 'r') as f:
    for line in f:
        data = json.loads(line.strip())  # 解析每行JSON数据
        epochs.append(data["epoch"])
        train_lr.append(data["train_lr"])
        train_loss.append(data["train_loss"])
        train_tactile_vision.append(data["train_tactile_vision"])
        train_tactile_vision_acc1.append(data["train_tactile_vision_acc1"])
        train_tactile_vision_acc5.append(data["train_tactile_vision_acc5"])
        train_average_acc1.append(data["train_average_acc1"])
        train_average_acc5.append(data["train_average_acc5"])

# 定义一个滑动平均函数
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# 设定窗口大小，通常窗口大小选择较小的值（比如5或10）
window_size = 5

# 计算平滑后的数据
train_loss_smoothed = moving_average(train_loss, window_size)
train_lr_smoothed = moving_average(train_lr, window_size)
train_tactile_vision_smoothed = moving_average(train_tactile_vision, window_size)
train_average_acc1_smoothed = moving_average(train_average_acc1, window_size)

# 计算平滑数据后对应的epochs
epochs_smoothed = epochs[:len(train_loss_smoothed)]  # 对应平滑数据的epoch范围

# 创建子图
fig, axes = plt.subplots(4, 1, figsize=(10, 12))  # 4行1列的子图

# 绘制 train_loss
axes[0].plot(epochs_smoothed, train_loss_smoothed, color='tab:red', label='train_loss', linestyle='-', marker='o')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('train_loss')
axes[0].set_title('Train Loss (Smoothed)')
axes[0].legend()

# 绘制 train_lr
axes[1].plot(epochs_smoothed, train_lr_smoothed, color='tab:green', label='train_lr', linestyle='--', marker='s')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('train_lr')
axes[1].set_title('Learning Rate (train_lr) (Smoothed)')
axes[1].legend()

# 绘制 train_tactile_vision
axes[2].plot(epochs_smoothed, train_tactile_vision_smoothed, color='tab:orange', label='train_tactile_vision', linestyle='--', marker='^')
axes[2].set_xlabel('Epoch')
axes[2].set_ylabel('train_tactile_vision')
axes[2].set_title('Tactile Vision Loss (Smoothed)')
axes[2].legend()

# 绘制 train_average_acc1
axes[3].plot(epochs_smoothed, train_average_acc1_smoothed, color='tab:blue', label='train_average_acc1', linestyle='-', marker='x')
axes[3].set_xlabel('Epoch')
axes[3].set_ylabel('train_average_acc1')
axes[3].set_title('Train Accuracy (Average Acc1) (Smoothed)')
axes[3].legend()

# 调整布局以避免重叠
plt.tight_layout()

# 显示图形
plt.show()


# 初始化数据存储容器
epochs = []
train_lr = []
train_loss = []
train_tactile_vision = []
train_tactile_vision_acc1 = []
train_tactile_vision_acc5 = []
train_average_acc1 = []
train_average_acc5 = []

# 逐行读取并解析JSON数据
with open(log_file, 'r') as f:
    for line in f:
        data = json.loads(line.strip())  # 解析每行JSON数据
        epochs.append(data["epoch"])
        train_lr.append(data["train_lr"])
        train_loss.append(data["train_loss"])
        train_tactile_vision.append(data["train_tactile_vision"])
        train_tactile_vision_acc1.append(data["train_tactile_vision_acc1"])
        train_tactile_vision_acc5.append(data["train_tactile_vision_acc5"])
        train_average_acc1.append(data["train_average_acc1"])
        train_average_acc5.append(data["train_average_acc5"])

# 定义一个滑动平均函数
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# 设定窗口大小，通常窗口大小选择较小的值（比如5或10）
window_size = 5

# 计算平滑后的数据
train_loss_smoothed = moving_average(train_loss, window_size)
train_lr_smoothed = moving_average(train_lr, window_size)
train_tactile_vision_smoothed = moving_average(train_tactile_vision, window_size)
train_average_acc1_smoothed = moving_average(train_average_acc1, window_size)

# 计算平滑数据后对应的epochs
epochs_smoothed = epochs[:len(train_loss_smoothed)]  # 对应平滑数据的epoch范围

# 创建子图
fig, axes = plt.subplots(4, 1, figsize=(10, 12))  # 4行1列的子图

# 绘制 train_loss
axes[0].plot(epochs_smoothed, train_loss_smoothed, color='tab:red', label='train_loss', linestyle='-', marker='o')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('train_loss')
axes[0].set_title('Train Loss (Smoothed)')
axes[0].legend()

# 绘制 train_lr
axes[1].plot(epochs_smoothed, train_lr_smoothed, color='tab:green', label='train_lr', linestyle='--', marker='s')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('train_lr')
axes[1].set_title('Learning Rate (train_lr) (Smoothed)')
axes[1].legend()

# 绘制 train_tactile_vision
axes[2].plot(epochs_smoothed, train_tactile_vision_smoothed, color='tab:orange', label='train_tactile_vision', linestyle='--', marker='^')
axes[2].set_xlabel('Epoch')
axes[2].set_ylabel('train_tactile_vision')
axes[2].set_title('Tactile Vision Loss (Smoothed)')
axes[2].legend()

# 绘制 train_average_acc1
axes[3].plot(epochs_smoothed, train_average_acc1_smoothed, color='tab:blue', label='train_average_acc1', linestyle='-', marker='x')
axes[3].set_xlabel('Epoch')
axes[3].set_ylabel('train_average_acc1')
axes[3].set_title('Train Accuracy (Average Acc1) (Smoothed)')
axes[3].legend()

# 调整布局以避免重叠
plt.tight_layout()

# 显示图形
plt.show()
