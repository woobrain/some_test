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
visual_block.Visual_Block_Total_Block(11)

# -*- 参数面板
try:

    PANEL_VARS = {
    }

except Exception as e:
    log.error("[%s] %s", "参数面板", str(e))

# -*- 传入的JSON
try:

    update_panel(sys.argv, PANEL_VARS)

except Exception as e:
    log.error("[%s] %s", "传入的JSON", str(e))

# -*- 打开/新建 Excel 文档
try:
    visual_block.Visual_Block_Info("打开/新建 Excel 文档", 1, 0, "正在执行")

    import rpa.excel

    rpa_c7be40_excel = rpa.excel.create(visible=True, wps=False)

except Exception as e:
    visual_block.Visual_Block_Info("打开/新建 Excel 文档", 1, 2, e)

    log.error("[%s] %s", "打开/新建 Excel 文档", str(e))
    raise e

# -*- 启动浏览器
try:
    visual_block.Visual_Block_Info("启动浏览器", 2, 0, "正在执行")

    option = ChromeOptions()
    prefs = {'safebrowsing.enabled': True}
    option.add_experimental_option('prefs', prefs)
    rpa_b56312_browser = Chrome(option)

except Exception as e:
    visual_block.Visual_Block_Info("启动浏览器", 2, 2, e)

    log.error("[%s] %s", "启动浏览器", str(e))
    raise e

# -*- 打开网页
try:
    visual_block.Visual_Block_Info("打开网页", 3, 0, "正在执行")

    rpa_0d164f_webpage = rpa_b56312_browser.create("https://www.51job.com/?from=baidupz")

except Exception as e:
    visual_block.Visual_Block_Info("打开网页", 3, 2, e)

    log.error("[%s] %s", "打开网页", str(e))
    raise e

# -*- 最大化
try:
    visual_block.Visual_Block_Info("最大化", 4, 0, "正在执行")

    rpa_b56312_browser.max_window()

except Exception as e:
    visual_block.Visual_Block_Info("最大化", 4, 2, e)

    log.error("[%s] %s", "最大化", str(e))
    raise e

# -*- 填写输入框内容
try:
    visual_block.Visual_Block_Info("填写输入框内容", 5, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_0d164f_webpage.add_element("rpa_e87072", id="kwdselectid", css="#kwdselectid",
                                   xpath=["//input[@id='kwdselectid']", "//div[3]/div/div/div/div/p/input"], frame=[])
    rpa_0d164f_webpage.switch_to_frame_by_path([])
    rpa_0d164f_webpage.get_element("rpa_e87072", timeout=30).input("python", simulate=True)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("填写输入框内容", 5, 2, e)

    log.error("[%s] %s", "填写输入框内容", str(e))
    raise e

# -*- 点击网页元素
try:
    visual_block.Visual_Block_Info("点击网页元素", 6, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_0d164f_webpage.add_element("rpa_7bafba", id="", css="button:nth-child(2)",
                                   xpath=["//button[@onclick=\"kwdGoSearch($('#kwdselectid').val());\"]",
                                          "//div[3]/div/div/div/button", "//button[contains(.,'搜索')]"], frame=[])
    rpa_0d164f_webpage.switch_to_frame_by_path([])
    from rpa import ElementClickMethod

    rpa_0d164f_webpage.get_element("rpa_7bafba", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("点击网页元素", 6, 2, e)

    log.error("[%s] %s", "点击网页元素", str(e))
    raise e

# -*- Excel_row
try:
    visual_block.Visual_Block_Info("Excel_row", 7, 0, "正在执行")

    row = 1

except Exception as e:
    visual_block.Visual_Block_Info("Excel_row", 7, 2, e)

    log.error("[%s] %s", "Excel_row", str(e))
    raise e

# -*- 写入Excel
try:
    visual_block.Visual_Block_Info("写入Excel", 8, 0, "正在执行")

    sys.coinit_flags = 0
    a_dict = {
        'A': '职位',
        'B': '公司',
        'C': '地点',
        'D': '薪资',
        'E': '发布时间',
    }
    for k, v in a_dict.items():
        try:
            visual_block.Visual_Block_Info("写入/设置 Excel 内容", 7, 0, "正在执行")
            import rpa.excel

            rpa_c7be40_excel.get_sheet("").set_row_height(k + str("1"), "20")
            rpa_c7be40_excel.get_sheet("").set_col_width(k + str("1"), "30")
            rpa_c7be40_excel.get_sheet("").set_style(k + str(row), style="align", value="居中")
        except Exception as e:
            visual_block.Visual_Block_Info("写入/设置 Excel 内容", 7, 2, e)
            log.error("[%s] %s", "写入/设置 Excel 内容", e.message)
            raise e
        try:
            visual_block.Visual_Block_Info("写入/设置 Excel 内容", 7, 0, "正在执行")
            import rpa.excel

            rpa_c7be40_excel.get_sheet("").write(k + str("1"), v)
        except Exception as e:
            visual_block.Visual_Block_Info("写入/设置 Excel 内容", 7, 2, e)
            log.error("[%s] %s", "写入/设置 Excel 内容", e.message)
            raise e

except Exception as e:
    visual_block.Visual_Block_Info("写入Excel", 8, 2, e)

    log.error("[%s] %s", "写入Excel", str(e))
    raise e

# -*- 创建flag
try:
    visual_block.Visual_Block_Info("创建flag", 9, 0, "正在执行")

    flag = 0

except Exception as e:
    visual_block.Visual_Block_Info("创建flag", 9, 2, e)

    log.error("[%s] %s", "创建flag", str(e))
    raise e

# -*- 创建start_row
try:
    visual_block.Visual_Block_Info("创建start_row", 10, 0, "正在执行")

    start_row = 2

except Exception as e:
    visual_block.Visual_Block_Info("创建start_row", 10, 2, e)

    log.error("[%s] %s", "创建start_row", str(e))
    raise e

# -*- 循环执行1
try:
    visual_block.Visual_Block_Info("循环执行1", 11, 0, "正在执行")

    while "1" == "1":

        # -*- 获取网页元素1
        try:
            from time import sleep

            sleep(0)
            rpa_0d164f_webpage.add_element("rpa_228e4e", id="resultList", css="#resultList",
                                           xpath=["//div[@id='resultList']", "//div[2]/div[4]"], frame=[])
            rpa_0d164f_webpage.switch_to_frame_by_path([])
            rpa_5b65a6 = rpa_0d164f_webpage.get_element(element_name="rpa_228e4e", index=0, timeout=5)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取网页元素1", str(e))
            raise e

        # -*- 获取网页子元素1
        try:
            from time import sleep

            sleep(0)
            rpa_5b65a6.switch_to_frame()
            rpa_fb6503 = rpa_5b65a6.children(index=None)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取网页子元素1", str(e))
            raise e

        # -*- 得到总元素
        try:
            a_list = rpa_fb6503

        except Exception as e:
            log.error("[%s] %s", "得到总元素", str(e))
            raise e

        # -*- 得到所需所有信息元素
        try:
            a_list = a_list[3:len(a_list) - 9]

        except Exception as e:
            log.error("[%s] %s", "得到所需所有信息元素", str(e))
            raise e

        # -*- 创建job_list1
        try:
            job_list = []

        except Exception as e:
            log.error("[%s] %s", "创建job_list1", str(e))
            raise e

        # -*- 循环执行子元素1
        try:

            for rpa_0a04af in a_list:

                # -*- 获取网页元素内容1
                try:
                    from time import sleep

                    sleep(0)
                    rpa_0d164f_webpage.switch_to_frame_by_path(rpa_0a04af.frame)
                    rpa_51bc19 = rpa_0a04af.text()
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取网页元素内容1", str(e))
                    raise e

                # -*- 字符串操作1
                try:
                    rpa_fbcad4 = rpa_51bc19.split("\n")

                except Exception as e:
                    log.error("[%s] %s", "字符串操作1", str(e))
                    raise e

                # -*- 自定义脚本21
                try:
                    if len(rpa_fbcad4) != 5:
                        rpa_fbcad4.insert(-1, '')

                except Exception as e:
                    log.error("[%s] %s", "自定义脚本21", str(e))
                    raise e

                # -*- 数组操作1
                try:
                    job_list.append(rpa_fbcad4)

                except Exception as e:
                    log.error("[%s] %s", "数组操作1", str(e))
                    raise e
        except Exception as e:
            log.error("[%s] %s", "循环执行子元素1", str(e))
            raise e

        # -*- 行1
        try:
            rpa_90fd4a = len(job_list)

        except Exception as e:
            log.error("[%s] %s", "行1", str(e))
            raise e

        # -*- 列1
        try:
            col_str = chr(65 + len(job_list[0]) - 1)

        except Exception as e:
            log.error("[%s] %s", "列1", str(e))
            raise e

        # -*- 写入/设置 Excel 内容1
        try:
            import rpa.excel
            print(start_row)
            rpa_c7be40_excel.get_sheet("").write("A" + str(start_row) + ":" + col_str + str(rpa_90fd4a), job_list)

        except Exception as e:
            log.error("[%s] %s", "写入/设置 Excel 内容1", str(e))
            raise e

        # -*- 数学运算1
        try:
            rpa_aff34d = start_row + rpa_90fd4a

        except Exception as e:
            log.error("[%s] %s", "数学运算1", str(e))
            raise e

        # -*- 赋值操作1
        try:
            start_row = rpa_aff34d

        except Exception as e:
            log.error("[%s] %s", "赋值操作1", str(e))
            raise e

        # # -*- 打印日志
        # try:
        #     from rpa import log
        #
        #     log.info("[%s] %s", "打印日志", rpa_aff34d)
        #
        # except Exception as e:
        #     log.error("[%s] %s", "打印日志", str(e))
        #     raise e

        # -*- 异常处理
        try:
            try:

                # -*- 获取网页元素2
                try:
                    from time import sleep

                    sleep(0)
                    rpa_0d164f_webpage.add_element("rpa_1167b1", id="", css=".p_in > ul",
                                                   xpath=["//div[@id='resultList']/div[55]/div/div/div/ul",
                                                          "//div[55]/div/div/div/ul"], frame=[])
                    rpa_0d164f_webpage.switch_to_frame_by_path([])
                    rpa_cb1a9b_webelement = rpa_0d164f_webpage.get_element(element_name="rpa_1167b1", index=0,
                                                                           timeout=30)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取网页元素2", str(e))
                    raise e

                # -*- 获取网页元素3
                try:
                    from time import sleep

                    sleep(0)
                    rpa_cb1a9b_webelement.switch_to_frame()
                    rpa_35b5c7_webelement = rpa_cb1a9b_webelement.children(index=None)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取网页元素3", str(e))
                    raise e

                # -*- 创建变量1
                try:
                    hah_list = rpa_35b5c7_webelement

                except Exception as e:
                    log.error("[%s] %s", "创建变量1", str(e))
                    raise e

                # -*- 获取网页元素4
                try:
                    from time import sleep

                    sleep(0)
                    rpa_cb1a9b_webelement.switch_to_frame()
                    rpa_d71d5e_webelement = rpa_cb1a9b_webelement.children(index=len(hah_list) - 1)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取网页元素4", str(e))
                    raise e

                # -*- 获取网页元素5
                try:
                    from time import sleep

                    sleep(0)
                    rpa_d71d5e_webelement.switch_to_frame()
                    rpa_e1afa4_webelement = rpa_d71d5e_webelement.children(index=0)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取网页元素5", str(e))
                    raise e

                # -*- 获取href1
                try:
                    from time import sleep

                    sleep(0)
                    rpa_0d164f_webpage.switch_to_frame_by_path(rpa_e1afa4_webelement.frame)
                    rpa_bc0774_string = rpa_e1afa4_webelement.get_attr("href")
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取href1", str(e))
                    raise e

                # -*- 延时执行
                try:
                    from time import sleep

                    sleep(5)

                except Exception as e:
                    log.error("[%s] %s", "延时执行", str(e))
                    raise e

                # -*- 转到新网址
                try:
                    rpa_0d164f_webpage.navigate(rpa_bc0774_string)

                except Exception as e:
                    log.error("[%s] %s", "转到新网址", str(e))
                    raise e
            except Exception as e:

                # -*- 数学运算
                try:
                    rpa_b4c377_number = flag + 1

                except Exception as e:
                    log.error("[%s] %s", "数学运算", str(e))
                    raise e

                # -*- 赋值操作
                try:
                    flag = rpa_b4c377_number

                except Exception as e:
                    log.error("[%s] %s", "赋值操作", str(e))
                    raise e

                # -*- 退出循环
                try:
                    break

                except Exception as e:
                    log.error("[%s] %s", "退出循环", str(e))
                    raise e
            finally:
                pass

        except Exception as e:
            log.error("[%s] %s", "异常处理", str(e))
            raise e
except Exception as e:
    visual_block.Visual_Block_Info("循环执行1", 11, 2, e)

    log.error("[%s] %s", "循环执行1", str(e))
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", str(e))
