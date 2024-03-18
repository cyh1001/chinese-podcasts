#使用RSShub API，目前仅限小宇宙。输入播客id，返回播客的RSS订阅地址。
import requests
from xml.etree import ElementTree

def extract_podcast_id(url: str) -> str:
    """
    从给定的播客链接中提取播客ID。

    参数:
    url (str): 播客的完整链接。

    返回:
    str: 播客ID。
    """
    # 确保URL以斜杠结束，便于处理
    if not url.endswith('/'):
        url += '/'
    
    # 分割URL以获取各个部分
    parts = url.split('/')
    
    # 假设播客ID总是在倒数第二个位置
    podcast_id = parts[-2]
    
    return podcast_id

# # 示例用法
# url = "https://www.xiaoyuzhoufm.com/podcast/5e7eb85d418a84a0465eda82"
# podcast_id = extract_podcast_id(url)
# print(podcast_id)

def get_rss_feed(link: str) -> str:
    """
    根据提供的小宇宙FM播客链接，使用RSShub API获取并返回播客的RSS订阅地址。

    参数:
        podcast_id (str): 播客的ID。

    返回:
        str: RSS订阅源地址，如果未找到则返回空字符串。
    """
    podcast_id = extract_podcast_id(link)
    # 构建请求URL
    url = f'https://rsshub.app/xiaoyuzhou/podcast/{podcast_id}'

    # 发起GET请求
    response = requests.get(url, headers={'accept': '*/*'})

    # 检查响应状态码
    if response.status_code == 200:
        try:
            # 解析XML响应
            root = ElementTree.fromstring(response.content)
            # 查找<atom:link>元素，获取其href属性作为RSS订阅地址
            namespace = {'atom': 'http://www.w3.org/2005/Atom'}
            rss_link_element = root.find('.//atom:link', namespace)
            if rss_link_element is not None:
                return rss_link_element.attrib['href']
            else:
                return ""  # 如果找不到<atom:link>元素，返回空字符串
        except ElementTree.ParseError:
            print('Failed to parse XML response.')
            return ""  # 解析XML失败时返回空字符串
    else:
        print('Failed to retrieve data:', response.status_code)
        return ""  # 请求失败时返回空字符串

# # 示例用法
# link = 'https://www.xiaoyuzhoufm.com/podcast/5e7eb85d418a84a0465eda82 '
# rss_feed = get_rss_feed(link)
# print(rss_feed)

















# # 小宇宙FM播客的ID
# podcast_id = '5e7eb85d418a84a0465eda82'

# # 构建请求URL
# url = f'https://rsshub.app/xiaoyuzhou/podcast/{podcast_id}'

# # 发起GET请求
# response = requests.get(url, headers={'accept': '*/*'})

# # 检查响应状态码
# if response.status_code == 200:
#     # 打印响应内容，这里假设响应是文本格式
#     print(response.text)
#     with open('1.md', 'w', encoding='utf-8') as file:
#         file.write(response.text)
# else:
#     print('Failed to retrieve data:', response.status_code)
