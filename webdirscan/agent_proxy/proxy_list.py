#创建代理池
import random

def get_proxy():
    proxy_list = [
        {'http':'119.53.136.53:8118'},
        {'http':'125.118.146.19:888'},
        {'.....'}
    ]

    return random.choice(proxy_list)
