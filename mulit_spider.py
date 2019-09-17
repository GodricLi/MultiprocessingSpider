import time
import requests
from multiprocessing.dummy import Pool

"""多线程爬虫简单演示"""
start = time.time()

headers = {
    'user_agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
url_list = ['https://wwww.baidu.com',
            'https://www.taobao.com',
            'https://www.lagou.com']


def get_data(url):
    print('开始下载：', url)
    time.sleep(2)
    response = requests.get(url=url, headers=headers)
    print('下载完成:', url)
    return response.text


# 实例化线程对象
pool = Pool(4)
# 将列表中的没一个元素传递给get_data()调用,返回一个元素为get_data()执行结果的列表
data = pool.map(get_data, url_list)

end = time.time()
print('Cost time:', end - start)
for i in range(len(data)):
    print(f'{url_list[i]}:数据长度{len(data[i])}')
