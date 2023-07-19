# Wistia视频下载教程 – 不需要任何下载软件或者浏览器插件
# 从comsol视频中获取 "复制链接和缩略图"  得到 MP4链接
# https://www.waimaob2c.com/wistia-download
# 兔子Lee 2023年7月20日
import webbrowser

import fun2find_comsol_video as myfun

# comsol 带有视频的地址
# url_comsol = "https://cn.comsol.com/support/learning-center/article/Modeling-Electromagnetic-Coils-8381/112"
url_comsol = input('请输入comsol网址\n')

# 从comsol中找到关键字
video_code = myfun.find_key_code_in_comsol(url_comsol)
# 视频关键字与wistia组合    并返回网页源码
wistia_source = myfun.find_wistia_source(video_code)
# 从wistia的网页源码找到.mp4文件地址
wistia_mp4 = myfun.find_word_between_two_key(wistia_source)

webbrowser.open(wistia_mp4)
print('\n\n------------------------------------------------------------')
input("程序已执行完毕----\n已经在浏览器打开视频源文件，请及时下载---\n按任意键结束\n")



