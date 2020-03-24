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
visual_block.Visual_Block_Total_Block(14)

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

# -*- 打开信息表文档
try:
    visual_block.Visual_Block_Info("打开信息表文档", 1, 0, "正在执行")

    import rpa.excel

    rpa_36308c_excel = rpa.excel.open(
        r"C:\\Users\\Administrator\\Desktop\\all_test\\orientation-master-69c44478cbf4319c878dd001239880dc717ac6fb\\rpa\\精进五道题\\题目二\\学历表.xlsx",
        visible=True, readonly=False, pass_word="", wps=True)

except Exception as e:
    visual_block.Visual_Block_Info("打开信息表文档", 1, 2, e)

    log.error("[%s] %s", "打开信息表文档", e.message)
    raise e

# -*- 新建学籍信息结果表
try:
    visual_block.Visual_Block_Info("新建学籍信息结果表", 2, 0, "正在执行")

    import rpa.excel

    rpa_b47b06_excel = rpa.excel.create(visible=True, wps=True)

except Exception as e:
    visual_block.Visual_Block_Info("新建学籍信息结果表", 2, 2, e)

    log.error("[%s] %s", "新建学籍信息结果表", e.message)
    raise e

# -*- 启动浏览器
try:
    visual_block.Visual_Block_Info("启动浏览器", 3, 0, "正在执行")

    option = ChromeOptions()
    prefs = {'safebrowsing.enabled': True}
    option.add_experimental_option('prefs', prefs)
    rpa_8bbb7f_browser = Chrome(option)

except Exception as e:
    visual_block.Visual_Block_Info("启动浏览器", 3, 2, e)

    log.error("[%s] %s", "启动浏览器", e.message)
    raise e

# -*- 浏览器窗口操作
try:
    visual_block.Visual_Block_Info("浏览器窗口操作", 4, 0, "正在执行")

    rpa_8bbb7f_browser.max_window()

except Exception as e:
    visual_block.Visual_Block_Info("浏览器窗口操作", 4, 2, e)

    log.error("[%s] %s", "浏览器窗口操作", e.message)
    raise e

# -*- 打开网页
try:
    visual_block.Visual_Block_Info("打开网页", 5, 0, "正在执行")

    rpa_4d2c6a_webpage = rpa_8bbb7f_browser.create("https://www.chsi.com.cn/")

except Exception as e:
    visual_block.Visual_Block_Info("打开网页", 5, 2, e)

    log.error("[%s] %s", "打开网页", e.message)
    raise e

# -*- 点击学历查询
try:
    visual_block.Visual_Block_Info("点击学历查询", 6, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_4d2c6a_webpage.add_element("rpa_9e8c51", id="", css=".width1000 > li:nth-child(3) > a",
                                   xpath=["//a[contains(text(),'学历查询')]", "//a[contains(@href, '/xlcx/index.jsp')]",
                                          "//li[3]/a", "//a[contains(.,'学历查询')]"], frame=[])
    rpa_4d2c6a_webpage.switch_to_frame_by_path([])
    from rpa import ElementClickMethod

    rpa_4d2c6a_webpage.get_element("rpa_9e8c51", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("点击学历查询", 6, 2, e)

    log.error("[%s] %s", "点击学历查询", e.message)
    raise e

# -*- 点击零散查询
try:
    visual_block.Visual_Block_Info("点击零散查询", 7, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_4d2c6a_webpage.add_element("rpa_9e8c51", id="", css=".m_f_div:nth-child(2) .btn_blue",
                                   xpath=["(//a[contains(text(),'查询')])[6]", "//div[@id='leftH']/div[2]/div[2]/div/a",
                                          "(//a[contains(@href, '/xlcx/lscx/query.do')])[2]",
                                          "//div[2]/div[2]/div[2]/div/a"], frame=[])
    rpa_4d2c6a_webpage.switch_to_frame_by_path([])
    from rpa import ElementClickMethod

    rpa_4d2c6a_webpage.get_element("rpa_9e8c51", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("点击零散查询", 7, 2, e)

    log.error("[%s] %s", "点击零散查询", e.message)
    raise e

# -*- 读取/获取 Excel 内容
try:
    visual_block.Visual_Block_Info("读取/获取 Excel 内容", 8, 0, "正在执行")

    import rpa.excel

    rpa_56813d_array_any = rpa_36308c_excel.get_sheet("").read()

except Exception as e:
    visual_block.Visual_Block_Info("读取/获取 Excel 内容", 8, 2, e)

    log.error("[%s] %s", "读取/获取 Excel 内容", e.message)
    raise e

# -*- 创建新列表
try:
    visual_block.Visual_Block_Info("创建新列表", 9, 0, "正在执行")

    a_list = rpa_56813d_array_any

except Exception as e:
    visual_block.Visual_Block_Info("创建新列表", 9, 2, e)

    log.error("[%s] %s", "创建新列表", e.message)
    raise e

# -*- 切片
try:
    visual_block.Visual_Block_Info("切片", 10, 0, "正在执行")

    a_list = a_list[1:]

except Exception as e:
    visual_block.Visual_Block_Info("切片", 10, 2, e)

    log.error("[%s] %s", "切片", e.message)
    raise e

# -*- Bool
try:
    visual_block.Visual_Block_Info("Bool", 11, 0, "正在执行")

    a = True

except Exception as e:
    visual_block.Visual_Block_Info("Bool", 11, 2, e)

    log.error("[%s] %s", "Bool", e.message)
    raise e

# -*- Bool1
try:
    visual_block.Visual_Block_Info("Bool1", 12, 0, "正在执行")

    b = False

except Exception as e:
    visual_block.Visual_Block_Info("Bool1", 12, 2, e)

    log.error("[%s] %s", "Bool1", e.message)
    raise e

# -*- Excel行数
try:
    visual_block.Visual_Block_Info("Excel行数", 13, 0, "正在执行")

    row = 1

except Exception as e:
    visual_block.Visual_Block_Info("Excel行数", 13, 2, e)

    log.error("[%s] %s", "Excel行数", e.message)
    raise e

# -*- 循环执行
try:
    visual_block.Visual_Block_Info("循环执行", 14, 0, "正在执行")

    for rpa_202c35_any in a_list:

        # -*- 创建变量接受信息
        try:
            num_name = rpa_202c35_any

        except Exception as e:
            log.error("[%s] %s", "创建变量接受信息", e.message)
            raise e

        # -*- 获取学号
        try:
            rpa_d43b73_array_any = num_name[0]

        except Exception as e:
            log.error("[%s] %s", "获取学号", e.message)
            raise e

        # -*- 获取姓名
        try:
            rpa_8791bc = num_name[1]

        except Exception as e:
            log.error("[%s] %s", "获取姓名", e.message)
            raise e

        # -*- 填写学号
        try:
            from time import sleep

            sleep(0)
            rpa_4d2c6a_webpage.add_element("rpa_b2fe4c", id="zsbh", css="#zsbh", xpath=["//input[@id='zsbh']",
                                                                                        "//form[@id='queryForm']/table/tbody/tr/td[2]/input",
                                                                                        "//input"], frame=[])
            rpa_4d2c6a_webpage.switch_to_frame_by_path([])
            rpa_4d2c6a_webpage.get_element("rpa_b2fe4c", timeout=30).input(rpa_d43b73_array_any, simulate=True)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "填写学号", e.message)
            raise e

        # -*- 填写姓名
        try:
            from time import sleep

            sleep(0)
            rpa_4d2c6a_webpage.add_element("rpa_b2fe4c", id="xm", css="#xm", xpath=["//input[@id='xm']",
                                                                                    "//form[@id='queryForm']/table/tbody/tr[2]/td[2]/input",
                                                                                    "//tr[2]/td[2]/input"], frame=[])
            rpa_4d2c6a_webpage.switch_to_frame_by_path([])
            rpa_4d2c6a_webpage.get_element("rpa_b2fe4c", timeout=30).input(rpa_8791bc, simulate=True)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "填写姓名", e.message)
            raise e

        # -*- 判断是否输入验证码
        try:

            while "1" == "1":

                # -*- 延时执行
                try:
                    from time import sleep

                    sleep(1)

                except Exception as e:
                    log.error("[%s] %s", "延时执行", e.message)
                    raise e

                # -*- 判断网页元素状态
                try:
                    from time import sleep

                    sleep(0)
                    rpa_4d2c6a_webpage.add_element("rpa_168acb", id="mphone_messagesend_btn",
                                                   css="#mphone_messagesend_btn",
                                                   xpath=["//input[@id='mphone_messagesend_btn']",
                                                          "//form[@id='vcode_fm']/table/tbody/tr[2]/td[2]/input[2]",
                                                          "//input[2]"], frame=[])
                    rpa_4d2c6a_webpage.switch_to_frame_by_path([])
                    rpa_d5ac1e_boolean = rpa_4d2c6a_webpage.get_element("rpa_168acb", timeout=30).is_visible()
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "判断网页元素状态", e.message)
                    raise e

                # -*- 打印日志1
                try:
                    from rpa import log

                    log.info("[%s] %s", "打印日志1", rpa_d5ac1e_boolean)

                except Exception as e:
                    log.error("[%s] %s", "打印日志1", e.message)
                    raise e

                # -*- 条件判断
                try:

                    if rpa_d5ac1e_boolean == a:

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
            log.error("[%s] %s", "判断是否输入验证码", e.message)
            raise e

        # -*- 判断验证手机号是否成功
        try:

            while "1" == "1":

                # -*- 延时执行1
                try:
                    from time import sleep

                    sleep(1)

                except Exception as e:
                    log.error("[%s] %s", "延时执行1", e.message)
                    raise e

                # -*- 获取网页元素2
                try:
                    from time import sleep

                    sleep(0)
                    rpa_4d2c6a_webpage.add_element("rpa_440842", id="cxcxxl-btn", css="#cxcxxl-btn",
                                                   xpath=["//input[@id='cxcxxl-btn']", "//input"], frame=[])
                    rpa_4d2c6a_webpage.switch_to_frame_by_path([])
                    rpa_8e96ab = rpa_4d2c6a_webpage.get_element(element_name="rpa_440842", index=0, timeout=30)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取网页元素2", e.message)
                    raise e

                # -*- 条件判断1
                try:
                    sleep(30)
                    if rpa_8e96ab != 1:

                        # -*- 写入未成功姓名
                        try:
                            import rpa.excel

                            rpa_b47b06_excel.get_sheet("").write("A" + str("1"), rpa_8791bc)

                        except Exception as e:
                            log.error("[%s] %s", "写入未成功姓名", e.message)
                            raise e

                        # -*- 写入无
                        try:
                            import rpa.excel

                            rpa_b47b06_excel.get_sheet("").write("B" + str("1") + ":" + "M" + str("1"), '无')

                        except Exception as e:
                            log.error("[%s] %s", "写入无", e.message)
                            raise e

                        # -*- num_py
                        try:
                            rpa_b87d1a = rpa_d43b73_array_any

                        except Exception as e:
                            log.error("[%s] %s", "num_py", e.message)
                            raise e

                        # -*- 类型转换
                        try:
                            rpa_acd2cc = str(rpa_b87d1a)

                        except Exception as e:
                            log.error("[%s] %s", "类型转换", e.message)
                            raise e

                        # -*- 字符串操作
                        try:
                            rpa_afb9ed = "'" + rpa_acd2cc

                        except Exception as e:
                            log.error("[%s] %s", "字符串操作", e.message)
                            raise e

                        # -*- 打印日志2
                        try:
                            from rpa import log

                            log.info("[%s] %s", "打印日志2", "")

                        except Exception as e:
                            log.error("[%s] %s", "打印日志2", e.message)
                            raise e

                        # -*- 写入编号
                        try:
                            import rpa.excel

                            rpa_b47b06_excel.get_sheet("").write("N" + str("1"), rpa_afb9ed)

                        except Exception as e:
                            log.error("[%s] %s", "写入编号", e.message)
                            raise e

                        # -*- 写入是否成功判断2
                        try:
                            import rpa.excel

                            rpa_b47b06_excel.get_sheet("").write("O" + str("1"), '否')

                        except Exception as e:
                            log.error("[%s] %s", "写入是否成功判断2", e.message)
                            raise e

                        # -*- 写入是否成功判断1
                        try:
                            import rpa.excel

                            rpa_b47b06_excel.get_sheet("").write("O" + str("1"), '否')

                        except Exception as e:
                            log.error("[%s] %s", "写入是否成功判断1", e.message)
                            raise e
                    else:

                        # -*- 继续下次循环1
                        try:
                            continue

                        except Exception as e:
                            log.error("[%s] %s", "继续下次循环1", e.message)
                            raise e
                except Exception as e:
                    log.error("[%s] %s", "条件判断1", e.message)
                    raise e
        except Exception as e:
            log.error("[%s] %s", "判断验证手机号是否成功", e.message)
            raise e
except Exception as e:
    visual_block.Visual_Block_Info("循环执行", 14, 2, e)

    log.error("[%s] %s", "循环执行", e.message)
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", e.message)
