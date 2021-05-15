import configparser
import os
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
from requests.exceptions import ProxyError
import src.config as config

base_url = "https://www.pixiv.net"
rank_url = "https://www.pixiv.net/ranking.php"
login_url = "https://accounts.pixiv.net/login"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    'referer': 'https://www.pixiv.net/'
}
req = requests.session()



# 以下代码暂时废弃（一脚踢google验证钢板上，除非有大佬能解决这个问题)
def account_login(proxies):
    print('该功能开发中...')
    '''
    print('正在尝试登录pixiv')
    data_re = req.get(login_url, headers=headers, proxies=proxies)
    login_soup = BeautifulSoup(data_re.text, 'lxml')
    config.read(config_path)
    pixiv_id = config['account']['pixiv_id']
    password = config['account']['password']
    post_key = login_soup.find('input')['value']
    data = {
        'pixiv_id': pixiv_id,
        'password': password,
        'post_key': post_key
    }
    data_re = req.post("https://accounts.pixiv.net/api/login?lang=zh", data=data, headers=headers, proxies=proxies)
    print(data_re.test)
    config['cookie']['device_token'] = data_re.cookies['device_token']
    config['cookie']['PHPSESSID'] = data_re.cookies['PHPSESSID']
    '''


def cookies_login():
    headers['cookie'] = config.cookie.encode('utf-8')
    return


def ask_url(url):
    html = req.get(url, headers=headers)#, proxies=proxies)
    return html
