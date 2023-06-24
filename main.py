import unittest
import os
from BeautifulReport import BeautifulReport
import yaml

# 测试环境
# Environ = "/env_config/Offline/"
# 线上环境
Environ = "/env_config/Online/config.yml"
DIR = os.path.dirname(os.path.abspath(__file__))  # 获取当前执行文件所在目录的绝对路径


def run(test_suite):
    # 定义输出的文件位置和名字
    filename = "report.html"
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description='测试报告', report_dir=DIR)


if __name__ == '__main__':
    testsuite = unittest.defaultTestLoader.discover(
        start_dir=DIR + '/testCase',
        pattern="test_*.py"
    )
    run(testsuite)



