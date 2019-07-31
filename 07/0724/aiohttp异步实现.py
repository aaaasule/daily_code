# -*- coding:utf-8 -*-
from aiohttp import ClientSession
import asyncio

tasks = []
url = 'https://www.baidu.com/{}'
async def  hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello(url))

"""
高并发：
    响应时间：系统对请求作出响应的时间
    吞吐量：单位时间内处理的请求数量
    QPS（每秒查询率）：每秒响应请求数
    并发用户数：同时承载正常使用系统功能的用户数量

提升系统并发能力：
    垂直拓展：提升单机处理能力，
        (1)、增强单机硬件性能，例如，增加cpu核数、升级网卡、升级硬盘、扩充硬盘容量、扩充系统内存。
        （2）、提升单机架构性能，例如，使用cache来减少IO次数、使用一部来增加单服务吞吐量、使用无锁数据结构来减少响应时间。
        
    水平拓展：只要增加服务器数量，就能线性扩充系统性能，水平扩展对系统架构设计是有要求的，如何在架构各层进行可水平扩展的设计，以及互联网公司架构各层常见的水平扩展实践。
    
Python解决高并发的几种方式
    1、HTML页面静态化
    2、图片服务器分离
    3、使用缓存
    4、数据库集群、库表散列
    5、使用负载均衡的方法（简单的配置可以用nginx来配置负载均衡，只需要设置如下代码
     upstream djangoserver {  
             server 192.168.72.49:8080;  
             server 192.168.72.49:8081;  
          } 
    6、镜像
    7、CDN加速技术
    ）
    
    
    
    
    


"""