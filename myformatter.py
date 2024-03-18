#myformatter.py
#podcasts.csv格式处理
import csv
from useRSSHubapi import get_rss_feed  # 确保这个函数可用，根据你的实际情况可能需要调整导入路径

def update_rss_feed(file_path):
    """读取CSV文件，更新空的RSS feed，并处理tags格式"""
    updated_data = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == 0:  # 标题行
                updated_data.append(row)
                continue
            if not row:  # 跳过空行
                continue
            if len(row) != 4:  # 确保每行有四列数据
                continue

            # 处理tags，将分号替换为英文分号，并去除空格
            if row[3]:
                tags = row[3].strip().replace('；', ';')
                tags = [tag.strip() for tag in tags.split(';')]
                row[3] = '; '.join([tag for tag in tags if tag])

            # 检查并更新RSS feed
            if not row[2].strip():  # 如果RSS feed为空
                rss_feed = get_rss_feed(row[1])
                row[2] = rss_feed  # 更新RSS feed列

            updated_data.append(row)

    # 将更新后的数据写回CSV文件
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(updated_data)

if __name__ == '__main__':
    csv_file_path = 'podcasts.csv'
    update_rss_feed(csv_file_path)










# from useRSSHubapi import get_rss_feed
# with open('podcasts.csv', 'r', encoding=r'utf-8') as f:
#     file_content = f.read()

# lines = file_content.split('\n')

# content = lines[0] + '\n'

# for line in lines[1:]:
#     line = line.strip()
#     if not line:
#         continue

#     parts = line.split(',')
#     if len(parts) != 4:
#         continue
#     parts = [part.strip() for part in parts]

#     if parts[3]:
#         parts[3] = parts[3].strip().replace('；', ';')
#         tags = parts[3].split(';')
#         tags = [tag.strip() for tag in tags]
#         parts[3] = '; '.join([tag for tag in tags if tag])
#         content += ', '.join(parts) + '\n'

# with open('podcasts.csv', 'w', encoding=r'utf-8') as f:
#     f.write(content)
