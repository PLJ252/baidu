import re

import requests
import random

ua = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36 OPR/63.0.3368.43',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/534.54.16 (KHTML, like Gecko) Version/5.1.4 Safari/534.54.16',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3739.400',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 QIHU 360EE',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36',

]
headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.baidu.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
def getTopRequest(bank,keyword,page,seasonTime):
    params = (
        ('wd', keyword+'%20%22'+bank+'%22'),
        ('pn', (page - 1) * 10),
        ('oq', keyword),
        ('tn', 'baiduhome_pg'),
        ('ie', 'utf-8'),
        ('rsv_idx', '2'),
        ('rsv_pq', 'd09ea91a000533ad'),
        ('rsv_t', 'a741enhrt8jcViHd/8Q+gb0DnCzjIbctyKmpOkRk6BibYwnyQXvHFSqrZtTKeUHQlE4s'),
        ('gpc','stf%3D'+str(seasonTime[0])+'%2C'+str(seasonTime[1])+'%7Cstftype%3D2')
    )
    headers['User-Agent'] = random.choice(ua)
    return requests.get('https://www.baidu.com/s', headers=headers, params=params)

def getUrl(bank,keyword,title,href: str):
    """extract special url"""
    try_count = 3
    while True:
        try_count -= 1
        # proxy = random.choice(pro)
        headers['User-Agent'] = random.choice(ua)
        headers['Referer'] = href
        retry_count = 2
        while retry_count > 0:
            try:
                r = requests.get(url=href, headers=headers, timeout=3,allow_redirects=False)
                if r.status_code == 302 and 'Location' in r.headers.keys():
                    url = r.headers['Location']
                    r = requests.get(url=url,headers = headers,timeout = 3)
                    r.encoding = 'utf-8'
                    pattern = re.compile(r'[^\u4e00-\u9fa5]')
                    chinese = re.sub(pattern, '', r.text)  # 替换字符串
                    n_1 = len(re.findall(bank, title))
                    n_1 += len(re.findall(bank,chinese))
                    n_2 = len(re.findall(keyword, chinese))
                    flagc = False
                    if n_1 > 0 and n_2 > 0:
                        flagc = True
                    return url, flagc
            except Exception:
                retry_count -= 1
        if try_count == 0: return '', False

