

## 前言
这是个基于ChatGPT4生成的脚本，本人零代码基础，代码是跑通了但估计是用脸在跑的

## 功能实现
实现cubox订阅rss

## 效果预览
![image](https://github.com/712346867/ttrss-cubox/assets/35997541/faaaebf0-0b64-4e0a-92d6-987e676a9f79)


## 配置（更改代码中的以下信息）
cubox_api_key = 'Cubox API 密钥'  # Cubox API 密钥
rss_url = 'RSS 源 URL'  # RSS 源 URL
cubox_folder = '文件夹名称'  # Cubox 文件夹名称

## 其他说明
- 本代码部署到replit上，实现每3分钟检查一次，保持全天候在线运行
- 初次运行会创建一个processed_links.txt文件，用于储存记录查重
  
