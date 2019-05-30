import sys
sys.path.append('../')
import unittest
from testcases import demoCase
from utils import HTMLTestReportCN


if __name__ == "__main__":
    suite = unittest.TestSuite()
    test_cases = [demoCase.DemoTestCase("test_clickSomething"),demoCase.DemoTestCase("test_clickOneMorething")]
    suite.addTests(test_cases)
    filePath = 'F:\\HTMLTestReportCN.html'
    fp = open(filePath, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        # description='详细测试用例结果',
        tester='Findyou'
    )
    runner.run(suite)
    fp.close()
    print('执行完毕')
    exit()