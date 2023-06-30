import os
import requests
import feedparser
import time

# 从环境变量中获取 Cubox API 密钥、RSS 源 URL 和 Cubox 文件夹名称
cubox_api_key = 'https://cubox.pro/c/api/save/ehbo7xv0nn39ae'  # Cubox API 密钥
rss_url = 'http://23.94.122.242:181/public.php?op=rss&id=-2&is_cat=0&q=&key=n34v8t649cd4f2d03b5'  # RSS 源 URL
cubox_folder = 'Rss'  # Cubox 文件夹名称

# 文件路径
processed_links_file = 'processed_links.txt'

# 检查并创建 processed_links.txt 文件
if not os.path.isfile(processed_links_file):
    open(processed_links_file, 'w').close()

# 加载已处理的链接
processed_links = set()
with open(processed_links_file, 'r') as file:
    for line in file:
        processed_links.add(line.strip())


def post_to_cubox(title, url):
    # 构建 JSON 对象
    data = {
        "type": "url",
        "content": url,
        "title": title,
        "folder": cubox_folder
    }

    # 发送 POST 请求
    response = requests.post(cubox_api_key, json=data)

    # 检查响应
    if response.status_code == 200:
        print(f'Successfully posted {title} to Cubox')
    else:
        print(f'Failed to post {title} to Cubox: {response.text}')


def process_rss_feed():
    try:
        # 解析 RSS 源
        feed = feedparser.parse(rss_url)

        # 遍历 RSS 源中的每一项内容
        for entry in feed.entries:
            link = entry.link

            # 检查链接是否已经处理过，如果已处理过则跳过
            if link in processed_links:
                continue

            try:
                # 提取链接并进行容错处理
                post_to_cubox(entry.title, link)

                # 将链接添加到已处理集合中
                processed_links.add(link)
            except AttributeError:
                print(f'Failed to extract URL for entry: {entry}')
            except Exception as e:
                print(f'An error occurred while processing an entry: {e}')

        # 将已处理的链接保存到文件
        with open(processed_links_file, 'w') as file:
            for link in processed_links:
                file.write(f'{link}\n')

    except Exception as e:
        print(f'An error occurred while parsing the RSS feed: {e}')


# 主循环
while True:
    process_rss_feed()

    # 等待 3 分钟
    wait_time = 180  # 3 minutes
    while wait_time > 0:
        print(f'距下次采集时间: {wait_time} 秒')
        time.sleep(1)
        wait_time -= 1
