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
visual_block.Visual_Block_Total_Block(13)

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

    rpa_7218a5_excel = rpa.excel.open(
        r"C:\\Users\\Administrator\\Desktop\\all_test\\orientation-master-69c44478cbf4319c878dd001239880dc717ac6fb\\rpa\\精进五道题\\题目一\\王老师学生表.xlsx",
        visible=True, readonly=False, pass_word="", wps=True)

except Exception as e:
    visual_block.Visual_Block_Info("打开/新建 Excel 文档", 1, 2, e)

    log.error("[%s] %s", "打开/新建 Excel 文档", e.message)
    raise e

# -*- 启动浏览器
try:
    visual_block.Visual_Block_Info("启动浏览器", 2, 0, "正在执行")

    from rpa import IEOptions

    option = IEOptions()
    rpa_d13413_browser = IE(option)

except Exception as e:
    visual_block.Visual_Block_Info("启动浏览器", 2, 2, e)

    log.error("[%s] %s", "启动浏览器", e.message)
    raise e

# -*- 浏览器窗口操作
try:
    visual_block.Visual_Block_Info("浏览器窗口操作", 3, 0, "正在执行")

    rpa_d13413_browser.max_window()

except Exception as e:
    visual_block.Visual_Block_Info("浏览器窗口操作", 3, 2, e)

    log.error("[%s] %s", "浏览器窗口操作", e.message)
    raise e

# -*- 打开网页
try:
    visual_block.Visual_Block_Info("打开网页", 4, 0, "正在执行")

    rpa_8feedc_webpage = rpa_d13413_browser.create("about:blank")

except Exception as e:
    visual_block.Visual_Block_Info("打开网页", 4, 2, e)

    log.error("[%s] %s", "打开网页", e.message)
    raise e

# -*- 鼠标点击
try:
    visual_block.Visual_Block_Info("鼠标点击", 5, 0, "正在执行")

    import rpa.win32

    rpa.win32.mouse_click(x=206, y=37, button="left", count=1, duration=0.1)

except Exception as e:
    visual_block.Visual_Block_Info("鼠标点击", 5, 2, e)

    log.error("[%s] %s", "鼠标点击", e.message)
    raise e

# -*- 延时执行2
try:
    visual_block.Visual_Block_Info("延时执行2", 6, 0, "正在执行")

    from time import sleep

    sleep(1)

except Exception as e:
    visual_block.Visual_Block_Info("延时执行2", 6, 2, e)

    log.error("[%s] %s", "延时执行2", e.message)
    raise e

# -*- 键盘操作
try:
    visual_block.Visual_Block_Info("键盘操作", 7, 0, "正在执行")

    import rpa.win32

    rpa.win32.input_texts("C:\Users\Administrator\Desktop\题目一\index.html")

except Exception as e:
    visual_block.Visual_Block_Info("键盘操作", 7, 2, e)

    log.error("[%s] %s", "键盘操作", e.message)
    raise e

# -*- enter
try:
    visual_block.Visual_Block_Info("enter", 8, 0, "正在执行")

    import rpa.win32

    rpa.win32.key_send("Enter")

except Exception as e:
    visual_block.Visual_Block_Info("enter", 8, 2, e)

    log.error("[%s] %s", "enter", e.message)
    raise e

# -*- 延时执行1
try:
    visual_block.Visual_Block_Info("延时执行1", 9, 0, "正在执行")

    from time import sleep

    sleep(1)

except Exception as e:
    visual_block.Visual_Block_Info("延时执行1", 9, 2, e)

    log.error("[%s] %s", "延时执行1", e.message)
    raise e

# -*- 点击学生查询
try:
    visual_block.Visual_Block_Info("点击学生查询", 10, 0, "正在执行")

    from time import sleep

    sleep(0)
    rpa_8feedc_webpage.add_element("rpa_2f62a9", id="", css="", xpath=["//UL/LI[3]/A"], frame=[])
    rpa_8feedc_webpage.switch_to_frame_by_path([])
    from rpa import ElementClickMethod

    rpa_8feedc_webpage.get_element("rpa_2f62a9", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
    sleep(0)

except Exception as e:
    visual_block.Visual_Block_Info("点击学生查询", 10, 2, e)

    log.error("[%s] %s", "点击学生查询", e.message)
    raise e

# -*- 创建王老师
try:
    visual_block.Visual_Block_Info("创建王老师", 11, 0, "正在执行")

    name_wang = "王老师"

except Exception as e:
    visual_block.Visual_Block_Info("创建王老师", 11, 2, e)

    log.error("[%s] %s", "创建王老师", e.message)
    raise e

# -*- Excel行数
try:
    visual_block.Visual_Block_Info("Excel行数", 12, 0, "正在执行")

    row = 3

except Exception as e:
    visual_block.Visual_Block_Info("Excel行数", 12, 2, e)

    log.error("[%s] %s", "Excel行数", e.message)
    raise e

# -*- 循环执行
try:
    visual_block.Visual_Block_Info("循环执行", 13, 0, "正在执行")

    for rpa_54a33b_any in range(0, 1, 1):

        # -*- 延时执行
        try:
            from time import sleep

            sleep(1)

        except Exception as e:
            log.error("[%s] %s", "延时执行", e.message)
            raise e

        # -*- 获取所有信息
        try:
            from time import sleep

            sleep(0)
            rpa_8feedc_webpage.add_element("rpa_d3d216", id="", css="", xpath=["//TBODY", "//TBODY"], frame=[0])
            rpa_8feedc_webpage.switch_to_frame_by_path([0])
            rpa_b3ec96 = rpa_8feedc_webpage.get_element(element_name="rpa_d3d216", index=0, timeout=30)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取所有信息", e.message)
            raise e

        # -*- 获取子信息
        try:
            from time import sleep

            sleep(0)
            rpa_b3ec96.switch_to_frame()
            rpa_cd1687 = rpa_b3ec96.children(index=None)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取子信息", e.message)
            raise e

        # -*- 遍历信息
        try:

            for rpa_895527_any in rpa_cd1687:

                # -*- 获取老师名字元素
                try:
                    from time import sleep

                    sleep(0)
                    rpa_895527_any.switch_to_frame()
                    rpa_706ea8_webelement = rpa_895527_any.children(index=5)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取老师名字元素", e.message)
                    raise e

                # -*- 获取老师名字内容
                try:
                    from time import sleep

                    sleep(0)
                    rpa_8feedc_webpage.switch_to_frame_by_path(rpa_706ea8_webelement.frame)
                    rpa_d75c25_string = rpa_706ea8_webelement.text()
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取老师名字内容", e.message)
                    raise e

                # -*- 条件判断
                try:

                    if rpa_d75c25_string == name_wang:

                        # -*- 获取学号元素
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_895527_any.switch_to_frame()
                            rpa_c3b63c_webelement = rpa_895527_any.children(index=0)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取学号元素", e.message)
                            raise e

                        # -*- 获取学号内容
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_8feedc_webpage.switch_to_frame_by_path(rpa_c3b63c_webelement.frame)
                            rpa_bfe64b_string = rpa_c3b63c_webelement.text()
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取学号内容", e.message)
                            raise e

                        # -*- 获取姓名元素
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_895527_any.switch_to_frame()
                            rpa_82ff14 = rpa_895527_any.children(index=1)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取姓名元素", e.message)
                            raise e

                        # -*- 获取姓名内容
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_8feedc_webpage.switch_to_frame_by_path(rpa_82ff14.frame)
                            rpa_b2afc2 = rpa_82ff14.text()
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取姓名内容", e.message)
                            raise e

                        # -*- 获取身份证元素
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_895527_any.switch_to_frame()
                            rpa_c04553 = rpa_895527_any.children(index=3)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取身份证元素", e.message)
                            raise e

                        # -*- 获取身份证内容
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_8feedc_webpage.switch_to_frame_by_path(rpa_c04553.frame)
                            rpa_ddc72b = rpa_c04553.text()
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取身份证内容", e.message)
                            raise e

                        # -*- 写入学号
                        try:
                            import rpa.excel

                            rpa_7218a5_excel.get_sheet("").write("A" + str(row), rpa_bfe64b_string)

                        except Exception as e:
                            log.error("[%s] %s", "写入学号", e.message)
                            raise e

                        # -*- 写入姓名
                        try:
                            import rpa.excel

                            rpa_7218a5_excel.get_sheet("").write("B" + str(row), rpa_b2afc2)

                        except Exception as e:
                            log.error("[%s] %s", "写入姓名", e.message)
                            raise e

                        # -*- 设置列宽
                        try:
                            import rpa.excel

                            rpa_7218a5_excel.get_sheet("").set_col_width("C" + str(row), "30")

                        except Exception as e:
                            log.error("[%s] %s", "设置列宽", e.message)
                            raise e

                        # -*- 写入/设置 Excel 内容
                        try:
                            import rpa.excel

                            rpa_7218a5_excel.get_sheet("").set_formula("C" + str(row), "=")

                        except Exception as e:
                            log.error("[%s] %s", "写入/设置 Excel 内容", e.message)
                            raise e

                        # -*- 写入身份证号
                        try:
                            import rpa.excel

                            rpa_7218a5_excel.get_sheet("").write("C" + str(row), rpa_ddc72b)

                        except Exception as e:
                            log.error("[%s] %s", "写入身份证号", e.message)
                            raise e

                        # -*- 数学运算
                        try:
                            rpa_df8980_number = row + 1

                        except Exception as e:
                            log.error("[%s] %s", "数学运算", e.message)
                            raise e

                        # -*- row += 1
                        try:
                            row = rpa_df8980_number

                        except Exception as e:
                            log.error("[%s] %s", "row += 1", e.message)
                            raise e

                        # -*- 下一次循环1
                        try:
                            continue

                        except Exception as e:
                            log.error("[%s] %s", "下一次循环1", e.message)
                            raise e
                    else:

                        # -*- 下一次循环
                        try:
                            continue

                        except Exception as e:
                            log.error("[%s] %s", "下一次循环", e.message)
                            raise e
                except Exception as e:
                    log.error("[%s] %s", "条件判断", e.message)
                    raise e
        except Exception as e:
            log.error("[%s] %s", "遍历信息", e.message)
            raise e
except Exception as e:
    visual_block.Visual_Block_Info("循环执行", 13, 2, e)

    log.error("[%s] %s", "循环执行", e.message)
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", e.message)
