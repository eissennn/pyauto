import sys
import pytest
from time import sleep
from os.path import dirname, abspath
from page.baiduTest_page import BaiduPAGE
sys.path.insert(0, dirname(dirname(abspath(__file__))))


class TestSearch:
    """百度搜索"""
    # 创建测试函数test_baidu_search_case(),接收browser 和 base_url钩子函数。这两个函数需要在contest.py中定义
    def test_baidu_search_case(self, browser, base_url):
        """"
        名称：百度搜索"pytest"
        步骤：
        1、打开浏览器
        2、输入"pytest"关键字
        3、点击搜索按钮
        检查点：
        * 检查页面标题是否包含关键字。
        """
        page = BaiduPAGE(browser)
        page.open(base_url)
        page.search_input = "pytest"
        page.search_button.click()
        sleep(2)
        assert browser.title == "pytest_百度搜索"
        
#
# class TestSearchSettings:
#     """百度搜索设置"""
#
#     def test_baidu_search_setting(self, browser, base_url):
#         page = BaiduPAGE(browser)
#         page.open(base_url)
#         page.settings.click()
#         page.search_setting.click()
#         sleep(2)
#         page.saving_setting.click()
#         alert_text = page.get_alert_text
#         page.accept_alert()
#         assert alert_text == "已经记录下您的使用偏好"


if __name__ == "__main__":
    # pytest.main(["-v", "-s", "test_baidu_auto.py"])
    pytest.main(["-v", "-s", "test_baidu_auto.py::TestSearch::test_baidu_search_case"])
    # pytest.main(["-v", "-s", "test_baidu_auto.py::TestSearch"])
    # pytest.main(["-v", "-s", "test_baidu_auto.py::TestSearchSettings"])
