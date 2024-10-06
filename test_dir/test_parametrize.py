import sys
import json
from time import sleep
import pytest
from os.path import dirname, abspath
from page.baiduTest_page import BaiduPAGE
base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)

#
# @pytest.mark.parametrize(
#     "name, search_key",
#     [
#         ("1", "Selenium"),
#         ("2", "pytest文档"),
#         ("3", "pytest-html")
#     ],
#     ids=["case1", "case2", "case3"]
# )
# def test_baidu_search(name, search_key, browser, base_url):
#     """
#     名称：百度搜索参数化
#     步骤：
#     1、打开浏览器
#     2、输入关键字
#     3、点击搜索按钮
#     检查点：
#     * 检查页面标题是否包含关键字。
#     """
#     page = BaiduPAGE(browser)
#     page.open(base_url)
#     page.search_input = search_key
#     page.search_button.click()
#     sleep(2)
#     assert browser.title == search_key + "_百度搜索"


def get_data(file_path):
    """
    读取文件参数化
    """
    data = []
    with(open(file_path, "r")) as f:
        dict_data = json.loads(f.read())
        for i in dict_data:
            data.append(tuple(i.values()))
    return data


@pytest.mark.parametrize(
    "name, search_key",
    get_data(base_path + "/test_dir/data/data_file.json")
)
def test_baidu_search(name, search_key, browser, base_url):
    """
    读取文件参数化
    """
    page = BaiduPAGE(browser)
    page.open(base_url)
    page.search_input = search_key
    page.search_button.click()
    sleep(2)
    assert browser.title == str(search_key) + "_百度搜索"
