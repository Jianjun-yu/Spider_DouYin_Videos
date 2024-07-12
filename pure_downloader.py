import requests
import os
import urllib.request

def download_video(account_name,video_url: str,save_folder='D:/save_video', file_name: str = None):
    """
    下载视频
    :param video_url: 视频地址
    :param file_name: 视频保存文件名: 默认为空
    :return:
    """
    save_folder = f"{save_folder}/{account_name}"
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    real_file_name = f"{save_folder}/{file_name}"
    #print(f"下载url:{video_url}\n保存文件名:{real_file_name}")
    if os.path.exists(real_file_name):
        os.remove(real_file_name)
    urllib.request.urlretrieve(video_url, real_file_name)


def download_images(account_name,image_list:list,image_dir:str=None,save_folder='D:/save_video'):
    """
    下载图片
    :param image_list: 图片地址
    :param file_name: 图片目录: 默认为空
    :return:
    """
    parent_folder = f"{save_folder}/{account_name}"
    if not os.path.exists(parent_folder):
        os.mkdir(parent_folder)
    save_folder = f"{save_folder}/{account_name}/{image_dir}"
    num=1
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    for image_url in image_list:
        num+=1
        real_file_name = f"{save_folder}/{num}.jpeg"
        if os.path.exists(real_file_name):
            os.remove(real_file_name)
        urllib.request.urlretrieve(image_url, real_file_name)