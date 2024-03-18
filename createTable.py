#createTable.py
'''
生成markdown表格和文档
'''
import csv
# import subprocess
# from useRSSHubapi import get_rss_feed

# def get_rss_feed(address):
#     """调用useRSShubapi.py脚本获取RSS feed"""
#     result = subprocess.run(['python', 'useRSSHubapi.py', address], capture_output=True, text=True)
#     return result.stdout.strip()
title='''
# 中文播客列表

## 目录

- [播客列表](#播客列表)
- [如何提交](#如何提交)

## 播客列表

> 欢迎联系我。微信：qq1030353305   email：yihancao1001@gmail.com  QQ:1030353305
'''
end='''
## 如何提交

1. 在 [./podcasts.csv](./podcasts.csv) 尾部添加一行，填入播客的 名称、URL、RSS以及标签
2. 提交 PR
3. (自动) PR 被 merge 之后 README 通过 [./createTable.py](./create.py) 生成

## 感谢

https://github.com/timqian/chinese-independent-blogs
'''
def read_csv(file_path):
    """读取CSV文件内容"""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        # reader = csv.reader(csvfile)
        # data = list(reader)
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data

# def write_csv(file_path, data):
#     """将更新后的数据写回CSV文件"""
#     with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(data)

def generate_markdown_table(data):
    """根据数据生成Markdown表格"""
    # headers = data[0]
    # rows = data[1:]
    # markdown = '| ' + ' | '.join(headers) + ' |\n'
    # markdown += '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'
    # for row in rows:
    #     markdown += '| ' + ' | '.join(row) + ' |\n'
    # return markdown
        # 处理标题行
    headers = data[0][:1] + data[0][2:]  # 删除第二列
    markdown = '| ' + ' | '.join(headers) + ' |\n'
    markdown += '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'
    
    # 处理数据行
    for row in data[1:]:
        name, link = row[:2]
        rest = row[2:]
        name_with_link = f"[{name}]({link})"  # 将名称变为超链接
        markdown_row = [name_with_link] + rest
        markdown += '| ' + ' | '.join(markdown_row) + ' |\n'
    return markdown




def generate_markdown_document(markdown_table, title="标题", end="结尾"):
    """生成包含标题和结尾的完整Markdown文档"""
    document = f"{title}\n\n{markdown_table}\n\n{end}"
    return document

def main(csv_file_path):
    data = read_csv(csv_file_path)

    # # 检查并更新RSS feed
    # for i, row in enumerate(data[1:], start=1):  # 跳过标题行
    #     if not row[2].strip():  # 如果RSS feed为空
    #         rss_feed = get_rss_feed(row[1])
    #         data[i][2] = rss_feed  # 更新RSS feed列

    # write_csv(csv_file_path, data)


    markdown_table = generate_markdown_table(data)
    markdown_document = generate_markdown_document(markdown_table, title, end) # 你可以在这里修改标题和结尾
    print(markdown_document)
    # print (title)
    # print(end)
    
    # 将生成的Markdown文档写入文件
    with open('README.md', 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_document)


if __name__ == '__main__':
    csv_file_path = 'podcasts.csv'  # 将'podcasts.csv'替换为你的CSV文件名
    main(csv_file_path)




