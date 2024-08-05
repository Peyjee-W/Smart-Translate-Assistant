import os
from datetime import datetime

def init_file():
    # 获取当前日期和时间
    date_str = datetime.now().strftime("%Y-%m-%d")
    time_str = datetime.now().strftime("%H-%M-%S")

    # 定义大文件夹和文件路径
    base_folder = "Translations"
    os.makedirs(base_folder, exist_ok=True)  # 确保创建大文件夹
    file_name = f"translations_{date_str}_{time_str}.txt"
    file_path = os.path.join(base_folder, file_name)

    # 创建文件并写入初始信息
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"翻译记录 - 日期: {date_str} 时间: {time_str}\n")
        file.write("=======================================\n\n")
    return file_path

def append_translation(file_path, original, translation):
    # 将原文和译文追加保存到同一个文件中
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("原文:\n")
        file.write(original + "\n\n")
        file.write("译文:\n")
        file.write(translation + "\n")
        file.write("---------------------------------------\n")
