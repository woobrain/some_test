# -*- coding:utf-8 -*-

from rpa import Chrome, IE, log, ChromeOptions, update_panel
from rpa.visual_block.visual_block import VisualBlock
import sys, os

__taskId = None
try:
    import getopt

    opts, _ = getopt.getopt(sys.argv[2:], '-h-t:', ['help', 'taskId='])
    for k, v in opts:
        if k in ('-t', '--taskId'):
            __taskId = v
except Exception as e:
    pass
try:
    import pywinauto
except:
    pass

visual_block = VisualBlock(taskId=__taskId)
visual_block.Visual_Block_Total_Block(24)

# -*- 参数面板
try:

    PANEL_VARS = {
    }

except Exception as e:
    log.error("[%s] %s", "参数面板", e.message)

# -*- 传入的JSON
try:

    update_panel(sys.argv, PANEL_VARS)

except Exception as e:
    log.error("[%s] %s", "传入的JSON", e.message)

# -*- 打开/新建 Excel 文档
try:
    visual_block.Visual_Block_Info("打开/新建 Excel 文档", 1, 0, "正在执行")

    import rpa.excel

    rpa_785890_excel = rpa.excel.create(visible=True, wps=True)

except Exception as e:
    visual_block.Visual_Block_Info("打开/新建 Excel 文档", 1, 2, e)

    log.error("[%s] %s", "打开/新建 Excel 文档", e.message)
    raise e

# -*- Excel行数
try:
    visual_block.Visual_Block_Info("Excel行数", 2, 0, "正在执行")

    row = 1

except Exception as e:
    visual_block.Visual_Block_Info("Excel行数", 2, 2, e)

    log.error("[%s] %s", "Excel行数", e.message)
    raise e

# -*- 自定义脚本
try:
    visual_block.Visual_Block_Info("自定义脚本", 3, 0, "正在执行")

    print type(row)

except Exception as e:
    visual_block.Visual_Block_Info("自定义脚本", 3, 2, e)

    log.error("[%s] %s", "自定义脚本", e.message)
    raise e

# -*- 启动浏览器
try:
    visual_block.Visual_Block_Info("启动浏览器", 4, 0, "正在执行")

    option = ChromeOptions()
    prefs = {'safebrowsing.enabled': True}
    option.add_experimental_option('prefs', prefs)
    rpa_51aa52_browser = Chrome(option)

except Exception as e:
    visual_block.Visual_Block_Info("启动浏览器", 4, 2, e)

    log.error("[%s] %s", "启动浏览器", e.message)
    raise e

# -*- 浏览器窗口操作
try:
    visual_block.Visual_Block_Info("浏览器窗口操作", 5, 0, "正在执行")

    rpa_51aa52_browser.max_window()

except Exception as e:
    visual_block.Visual_Block_Info("浏览器窗口操作", 5, 2, e)

    log.error("[%s] %s", "浏览器窗口操作", e.message)
    raise e

# -*- 打开网页
try:
    visual_block.Visual_Block_Info("打开网页", 6, 0, "正在执行")

    rpa_2ab734_webpage = rpa_51aa52_browser.create("http://idps2-demo.datagrand.net")

except Exception as e:
    visual_block.Visual_Block_Info("打开网页", 6, 2, e)

    log.error("[%s] %s", "打开网页", e.message)
    raise e

# -*- 输入账号
try:
    visual_block.Visual_Block_Info("输入账号", 7, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_2ab734_webpage.add_element("rpa_193090", id="", css=".ant-row:nth-child(1) .ng-pristine", xpath=["//input"],
                                   frame=[])
    rpa_2ab734_webpage.switch_to_frame_by_path([])
    rpa_2ab734_webpage.get_element("rpa_193090", timeout=30).input("rpa_demo", simulate=True)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("输入账号", 7, 2, e)

    log.error("[%s] %s", "输入账号", e.message)
    raise e

# -*- 输入密码
try:
    visual_block.Visual_Block_Info("输入密码", 8, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_2ab734_webpage.add_element("rpa_296076", id="", css=".item-password .ng-pristine",
                                   xpath=["//input[@type='password']",
                                          "//nz-form-item[2]/nz-form-control/div/span/nz-input-group/input"], frame=[])
    rpa_2ab734_webpage.switch_to_frame_by_path([])
    rpa_2ab734_webpage.get_element("rpa_296076", timeout=30).input("123#@!EWQ", simulate=True)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("输入密码", 8, 2, e)

    log.error("[%s] %s", "输入密码", e.message)
    raise e

# -*- 登录
try:
    visual_block.Visual_Block_Info("登录", 9, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_2ab734_webpage.add_element("rpa_2f5443", id="", css=".ant-btn",
                                   xpath=["//button[@type='submit']", "//button", "//button[contains(.,'登录')]"],
                                   frame=[])
    rpa_2ab734_webpage.switch_to_frame_by_path([])
    from rpa import ElementClickMethod

    rpa_2ab734_webpage.get_element("rpa_2f5443", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("登录", 9, 2, e)

    log.error("[%s] %s", "登录", e.message)
    raise e

# -*- 文档抽取
try:
    visual_block.Visual_Block_Info("文档抽取", 10, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_2ab734_webpage.add_element("rpa_008b5b", id="", css=".ad-nav__selected > .ad-nav__sub-title",
                                   xpath=["//li[4]/a", "//a[contains(.,'文档抽取')]"], frame=[])
    rpa_2ab734_webpage.switch_to_frame_by_path([])
    from rpa import ElementClickMethod

    rpa_2ab734_webpage.get_element("rpa_008b5b", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("文档抽取", 10, 2, e)

    log.error("[%s] %s", "文档抽取", e.message)
    raise e

# -*- 新建抽取任务
try:
    visual_block.Visual_Block_Info("新建抽取任务", 11, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_2ab734_webpage.add_element("rpa_6652a8", id="", css=".ad-nav__selected:nth-child(1) > .ng-star-inserted",
                                   xpath=["//a[contains(text(),'新建抽取任务')]", "//a[contains(@href, '#/extracting/task')]",
                                          "//li[4]/ul/li/a", "//a[contains(.,'新建抽取任务')]"], frame=[])
    rpa_2ab734_webpage.switch_to_frame_by_path([])
    from rpa import ElementClickMethod

    rpa_2ab734_webpage.get_element("rpa_6652a8", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("新建抽取任务", 11, 2, e)

    log.error("[%s] %s", "新建抽取任务", e.message)
    raise e

# -*- 点击上传
try:
    visual_block.Visual_Block_Info("点击上传", 12, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_2ab734_webpage.add_element("rpa_6526cf", id="",
                                   css=".ng-star-inserted:nth-child(4) .ng-star-inserted:nth-child(1) .tag-type-operation > span:nth-child(1)",
                                   xpath=["//idps-tag-type-card-container[2]/div/idps-tag-type-card/div/div[2]/span"],
                                   frame=[])
    rpa_2ab734_webpage.switch_to_frame_by_path([])
    from rpa import ElementClickMethod

    rpa_2ab734_webpage.get_element("rpa_6526cf", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("点击上传", 12, 2, e)

    log.error("[%s] %s", "点击上传", e.message)
    raise e

# -*- 上传文件
try:
    visual_block.Visual_Block_Info("上传文件", 13, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_2ab734_webpage.add_element("rpa_ab46bf", id="", css="div > .ant-btn:nth-child(1)", xpath=[
        "//div[@id='cdk-overlay-20']/div/div[2]/div/div/div[2]/idps-extract-create-upload-drawer/div/nz-form-item[3]/nz-form-control/div/span/nz-upload/div/div/div/div/button",
        "//nz-upload/div/div/div/div/button", "//button[contains(.,'选择文件')]"], frame=[])
    rpa_2ab734_webpage.switch_to_frame_by_path([])
    from rpa import ElementClickMethod

    rpa_2ab734_webpage.get_element("rpa_ab46bf", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("上传文件", 13, 2, e)

    log.error("[%s] %s", "上传文件", e.message)
    raise e

# -*- 延时执行1
try:
    visual_block.Visual_Block_Info("延时执行1", 14, 0, "正在执行")

    from time import sleep

    sleep(1)

except Exception as e:
    visual_block.Visual_Block_Info("延时执行1", 14, 2, e)

    log.error("[%s] %s", "延时执行1", e.message)
    raise e

# -*- 控件操作
try:
    visual_block.Visual_Block_Info("控件操作", 15, 0, "正在执行")

    import rpa.element

    rpa_a4346d = rpa.element.input_text(child_type="Edit", parent=r"打开",
                                        text="C:\\Users\\Administrator\\Desktop\\采购合同样本00001.pdf", index=1,
                                        parent_class_type="#32770", window_type="win32")

except Exception as e:
    visual_block.Visual_Block_Info("控件操作", 15, 2, e)

    log.error("[%s] %s", "控件操作", e.message)
    raise e

# -*- 键盘操作
try:
    visual_block.Visual_Block_Info("键盘操作", 16, 0, "正在执行")

    import rpa.win32

    rpa.win32.key_send("Enter")

except Exception as e:
    visual_block.Visual_Block_Info("键盘操作", 16, 2, e)

    log.error("[%s] %s", "键盘操作", e.message)
    raise e

# -*- 点击确认
try:
    visual_block.Visual_Block_Info("点击确认", 17, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_2ab734_webpage.add_element("rpa_be1e64", id="", css=".ant-form-item-children > .ant-btn-primary", xpath=[
        "//div[@id='cdk-overlay-20']/div/div[2]/div/div/div[2]/idps-extract-create-upload-drawer/div/nz-form-item[4]/nz-form-control/div/span/a",
        "//span/a", "//a[contains(.,'确定')]"], frame=[])
    rpa_2ab734_webpage.switch_to_frame_by_path([])
    from rpa import ElementClickMethod

    rpa_2ab734_webpage.get_element("rpa_be1e64", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("点击确认", 17, 2, e)

    log.error("[%s] %s", "点击确认", e.message)
    raise e

# -*- bool
try:
    visual_block.Visual_Block_Info("bool", 18, 0, "正在执行")

    bool_a = True

except Exception as e:
    visual_block.Visual_Block_Info("bool", 18, 2, e)

    log.error("[%s] %s", "bool", e.message)
    raise e

# -*- 循环执行1
try:
    visual_block.Visual_Block_Info("循环执行1", 19, 0, "正在执行")

    while "1" == "1":

        # -*- 延时执行2
        try:
            from time import sleep

            sleep(1)

        except Exception as e:
            log.error("[%s] %s", "延时执行2", e.message)
            raise e

        # -*- 点击查看
        try:
            from time import sleep

            sleep(0)
            rpa_2ab734_webpage.add_element("rpa_cd5cda", id="",
                                           css=".ant-table-row:nth-child(1) > td:nth-child(8) > .ng-star-inserted:nth-child(1)",
                                           xpath=["(//a[contains(text(),'查看')])[6]", "//td[8]/a"], frame=[])
            rpa_2ab734_webpage.switch_to_frame_by_path([])
            from rpa import ElementClickMethod

            rpa_2ab734_webpage.get_element("rpa_cd5cda", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "点击查看", e.message)
            raise e

        # -*- 判断网页元素状态
        try:
            from time import sleep

            sleep(0)
            rpa_2ab734_webpage.add_element("rpa_de5ba5", id="", css=".collapse-header > span",
                                           xpath=["//div/span", "//span[contains(.,'抽取列表')]"], frame=[])
            rpa_2ab734_webpage.switch_to_frame_by_path([])
            rpa_a11a19_boolean = rpa_2ab734_webpage.get_element("rpa_de5ba5", timeout=30).is_visible()
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "判断网页元素状态", e.message)
            raise e

        # -*- 打印日志
        try:
            from rpa import log

            log.info("[%s] %s", "打印日志", rpa_a11a19_boolean)

        except Exception as e:
            log.error("[%s] %s", "打印日志", e.message)
            raise e

        # -*- 条件判断
        try:

            if rpa_a11a19_boolean == bool_a:

                # -*- 退出循环
                try:
                    break

                except Exception as e:
                    log.error("[%s] %s", "退出循环", e.message)
                    raise e
            else:

                # -*- 继续下次循环
                try:
                    continue

                except Exception as e:
                    log.error("[%s] %s", "继续下次循环", e.message)
                    raise e
        except Exception as e:
            log.error("[%s] %s", "条件判断", e.message)
            raise e
except Exception as e:
    visual_block.Visual_Block_Info("循环执行1", 19, 2, e)

    log.error("[%s] %s", "循环执行1", e.message)
    raise e

# -*- count
try:
    visual_block.Visual_Block_Info("count", 20, 0, "正在执行")

    count = 0

except Exception as e:
    visual_block.Visual_Block_Info("count", 20, 2, e)

    log.error("[%s] %s", "count", e.message)
    raise e

# -*- col_list
try:
    visual_block.Visual_Block_Info("col_list", 21, 0, "正在执行")

    import string

    col_list = [i for i in string.ascii_uppercase]

except Exception as e:
    visual_block.Visual_Block_Info("col_list", 21, 2, e)

    log.error("[%s] %s", "col_list", e.message)
    raise e

# -*- 循环执行
try:
    visual_block.Visual_Block_Info("循环执行", 22, 0, "正在执行")

    for rpa_f827b8_any in range(0, 1, 1):

        # -*- 延时执行
        try:
            from time import sleep

            sleep(1)

        except Exception as e:
            log.error("[%s] %s", "延时执行", e.message)
            raise e

        # -*- 获取网页元素
        try:
            from time import sleep

            sleep(0)
            rpa_2ab734_webpage.add_element("rpa_89310e", id="", css=".content-container",
                                           xpath=["//app-title-collapse/div[2]"], frame=[])
            rpa_2ab734_webpage.switch_to_frame_by_path([])
            rpa_51c12c_webelement = rpa_2ab734_webpage.get_element(element_name="rpa_89310e", index=0, timeout=30)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取网页元素", e.message)
            raise e

        # -*- 获取网页子元素
        try:
            from time import sleep

            sleep(0)
            rpa_51c12c_webelement.switch_to_frame()
            rpa_9cc34e_webelement = rpa_51c12c_webelement.children(index=None)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取网页子元素", e.message)
            raise e

        # -*- 创建变量
        try:
            a_list = rpa_9cc34e_webelement

        except Exception as e:
            log.error("[%s] %s", "创建变量", e.message)
            raise e

        # -*- 自定义脚本2
        try:
            a_list = a_list[:8]

        except Exception as e:
            log.error("[%s] %s", "自定义脚本2", e.message)
            raise e

        # -*- 循环子元素
        try:

            for rpa_d88d82_any in a_list:

                # -*- a
                try:
                    a = col_list[count]

                except Exception as e:
                    log.error("[%s] %s", "a", e.message)
                    raise e

                # -*- 写入/设置 Excel 内容1
                try:
                    import rpa.excel

                    rpa_785890_excel.get_sheet("").set_col_width(a, "30")

                except Exception as e:
                    log.error("[%s] %s", "写入/设置 Excel 内容1", e.message)
                    raise e

                # -*- 获取网页元素1
                try:
                    from time import sleep

                    sleep(0)
                    rpa_d88d82_any.switch_to_frame()
                    rpa_7aa00b_webelement = rpa_d88d82_any.children(index=0)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取网页元素1", e.message)
                    raise e

                # -*- 获取0
                try:
                    from time import sleep

                    sleep(0)
                    rpa_2ab734_webpage.switch_to_frame_by_path(rpa_7aa00b_webelement.frame)
                    rpa_418fed_string = rpa_7aa00b_webelement.text()
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取0", e.message)
                    raise e

                # -*- 字符串操作
                try:
                    rpa_646c48_string = rpa_418fed_string.split("\n")

                except Exception as e:
                    log.error("[%s] %s", "字符串操作", e.message)
                    raise e

                # -*- 创建变量1
                try:
                    shuzu = rpa_646c48_string

                except Exception as e:
                    log.error("[%s] %s", "创建变量1", e.message)
                    raise e

                # -*- 创建变量2
                try:
                    shuzu2 = shuzu[::2]

                except Exception as e:
                    log.error("[%s] %s", "创建变量2", e.message)
                    raise e

                # -*- 写入/设置 Excel 内容
                try:
                    import rpa.excel

                    rpa_785890_excel.get_sheet("").write(a, shuzu2, start_row=1, max=1000)

                except Exception as e:
                    log.error("[%s] %s", "写入/设置 Excel 内容", e.message)
                    raise e

                # -*- count_num + 1
                try:
                    rpa_310bdb = count + 1

                except Exception as e:
                    log.error("[%s] %s", "count_num + 1", e.message)
                    raise e

                # -*- 赋值操作1
                try:
                    count = rpa_310bdb

                except Exception as e:
                    log.error("[%s] %s", "赋值操作1", e.message)
                    raise e
        except Exception as e:
            log.error("[%s] %s", "循环子元素", e.message)
            raise e
except Exception as e:
    visual_block.Visual_Block_Info("循环执行", 22, 2, e)

    log.error("[%s] %s", "循环执行", e.message)
    raise e

# -*- 保存/关闭 Excel 文档
try:
    visual_block.Visual_Block_Info("保存/关闭 Excel 文档", 23, 0, "正在执行")

    import rpa.excel
    import os

    rpa_785890_excel.save(file=os.path.join("C:\\Users\\Administrator\\Desktop\\DOC", "hetong.xls"), pass_word="")

except Exception as e:
    visual_block.Visual_Block_Info("保存/关闭 Excel 文档", 23, 2, e)

    log.error("[%s] %s", "保存/关闭 Excel 文档", e.message)
    raise e

# -*- 退出程序
try:
    visual_block.Visual_Block_Info("退出程序", 24, 0, "正在执行")

    exit(0)

except Exception as e:
    visual_block.Visual_Block_Info("退出程序", 24, 2, e)

    log.error("[%s] %s", "退出程序", e.message)
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", e.message)
