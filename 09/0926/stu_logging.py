# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: stu_logging.py
@time: 2019/9/26 11:03
"""

"""
logging模块中日志级别及其含义
日志级别        权重      含义
CRITICAL       50       严重错误，表示软件已经不能在运行下去了
ERROR          40       发生了严重的错误，必须马上处理
WARNING        30       应用程序可容忍这些错误，软件正常工作，不过它们应该被检查及修复，否则会发生问题
INFO           20       证明事情按预期工作，突出强调应用程序的运行过程
DEBUG          10       详细信息，只有开发人员调试程序时才需要关注的事情

"""
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(name)s : %(levelname)s : %(message)s', filename="./logger.log")
logger = logging.getLogger(__name__)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")