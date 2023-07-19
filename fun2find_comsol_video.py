# Author: Lee
# CreateTime: 2023/7/20

# import requests
from requests import get


def find_key_code_in_comsol(url_comsol):
    # 从comsol中找到关键字
    if url_comsol[:4] != 'http':
        print('输入有误\n')
        input("程序已暂停，按任意键结束\n")
        quit()
    # 包含视频关键字的 头 字符串
    video_code_head = 'https://fast.wistia.com/embed/medias/'
    # 请求网页源代码
    print('准备请求comsol网址源文件----')
    res = get(url_comsol).text
    print('已完成请求comsol网址源码------')
    # 如果连接有误 程序暂停
    if video_code_head not in res:
        print('没有找到视频关键字的头字符串\n')
        input("程序已暂停，按任意键结束\n")
        quit()

    # 找到视频的10位代码
    video_code_head_position = res.index(video_code_head)
    video_code = res[video_code_head_position + len(video_code_head):video_code_head_position + len(video_code_head) + 10]

    print('找到视频十位代码\n')
    return video_code


def find_wistia_source(video_code):
    # 视频关键字与wistia组合    并返回网页源码
    # wistia url 前后
    wistia_url = ('https://fast.wistia.net/embed/iframe/', '?videoFoam=true')
    print('完成视频关键字与wistia组合----\n正在访问wistia网页源码----')
    wistia_source = get(wistia_url[0] + video_code + wistia_url[1]).text
    print('返回带有视频的wistia网页源码\n')
    return wistia_source


def find_word_between_two_key(wistia_source):
    # 找到key1 与 key2 中的关键字
    # 思路 先找key2  key2后全删   反转字符串 找最近key1
    print('准备从wistia的网页源码找到.mp4文件地址---')
    key1 = 'https://embed-ssl.wistia.com/deliveries/'
    key2 = '.bin'

    # 寻找并舍去key2后面字符串
    pos_key2 = wistia_source.index(key2)
    wistia_source = wistia_source[:pos_key2]

    # 反转字符串的方法： wistia_source[::-1]
    r_key1 = key1[::-1]
    r_wistia_source = wistia_source[::-1]
    # 寻找并舍去key1 后面字符串
    pos_r_key1 = r_wistia_source.index(r_key1)
    r_wistia_source = r_wistia_source[:pos_r_key1 + len(key1)]
    # 恢复反转 拼接字符串
    wistia_source = r_wistia_source[::-1]
    wistia_mp4 = wistia_source + '.mp4'

    print('找到视频地址：' + wistia_mp4)
    return wistia_mp4


