# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: stu_click.py
@time: 2019/9/27 10:50
"""
"""使用click解析命令行参数"""
import click

@click.command() # 使函数hello成为命令行接口
@click.option('--count', default=1, help='xxx') # 增加命令行选项
@click.option('--name', prompt='your name', help='xxx') # 指定prompt参数时，当你没有输入需要的参数时，click会在交互模式下提示我们输入
def hello(count,name):
    for i in range(count):
        click.echo('Hello {}!'.format(name))

if __name__ == '__main__':

    hello()

"""
option常用的设置参数如下
    default 设置命令行参数默认值
    help 参数说明
    type 参数类型 
    prompt 当在命令行中没有输入相应的参数时， 会根据prompt提示用户输入
    nargs 指定命令行参数接受的个数
"""

"""
python stu_click.py --count=14 --name=John
"""