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

# -*- 新建 Excel 文档
try:
    visual_block.Visual_Block_Info("新建 Excel 文档", 1, 0, "正在执行")

    import rpa.excel

    rpa_6a4539_excel = rpa.excel.create(visible=True, wps=True)

except Exception as e:
    visual_block.Visual_Block_Info("新建 Excel 文档", 1, 2, e)

    log.error("[%s] %s", "新建 Excel 文档", e.message)
    raise e

# -*- 设置列宽
try:
    visual_block.Visual_Block_Info("设置列宽", 2, 0, "正在执行")

    import rpa.excel

    rpa_6a4539_excel.get_sheet("").set_col_width("A" + str("1") + ":" + "M" + str("1"), "17")

except Exception as e:
    visual_block.Visual_Block_Info("设置列宽", 2, 2, e)

    log.error("[%s] %s", "设置列宽", e.message)
    raise e

# -*- 居中
try:
    visual_block.Visual_Block_Info("居中", 3, 0, "正在执行")

    import rpa.excel

    rpa_6a4539_excel.get_sheet("").set_style("A" + str("1") + ":" + "M" + str("1"), style="align", value="居中")

except Exception as e:
    visual_block.Visual_Block_Info("居中", 3, 2, e)

    log.error("[%s] %s", "居中", e.message)
    raise e

# -*- head_list
try:
    visual_block.Visual_Block_Info("head_list", 4, 0, "正在执行")

    head_list = ['发票代码', '发票号码', '开票日期', '校验码', '机器编号', '合计(小写)', '购买方名称', '购买方纳税人识别号', '购买方地址、电话', '购买方开户行及账号',
                 '销售方名称', '销售方纳税人识别号', '销售方地址、电话', '销售方开户行及账号']

except Exception as e:
    visual_block.Visual_Block_Info("head_list", 4, 2, e)

    log.error("[%s] %s", "head_list", e.message)
    raise e

# -*- 写入表头
try:
    visual_block.Visual_Block_Info("写入表头", 5, 0, "正在执行")

    import rpa.excel

    rpa_6a4539_excel.get_sheet("").write("A" + str("1") + ":" + "M" + str("1"), head_list)

except Exception as e:
    visual_block.Visual_Block_Info("写入表头", 5, 2, e)

    log.error("[%s] %s", "写入表头", e.message)
    raise e

# -*- 文件夹绝对路径
try:
    visual_block.Visual_Block_Info("文件夹绝对路径", 6, 0, "正在执行")

    a_path = "C:\\Users\\Administrator\\Desktop\\all_test\\orientation-master-69c44478cbf4319c878dd001239880dc717ac6fb\\rpa\\入门三道题\\第三题 附件\\fapiao_pics\\"

except Exception as e:
    visual_block.Visual_Block_Info("文件夹绝对路径", 6, 2, e)

    log.error("[%s] %s", "文件夹绝对路径", e.message)
    raise e

# -*- 获取文件列表
try:
    visual_block.Visual_Block_Info("获取文件列表", 7, 0, "正在执行")

    import rpa.file_folder

    rpa_e54673_array_string = rpa.file_folder.list_dir(path=a_path, dirtype="file", withpath=False, isext=True)

except Exception as e:
    visual_block.Visual_Block_Info("获取文件列表", 7, 2, e)

    log.error("[%s] %s", "获取文件列表", e.message)
    raise e

# -*- 接收文件列表
try:
    visual_block.Visual_Block_Info("接收文件列表", 8, 0, "正在执行")

    file_list = rpa_e54673_array_string

except Exception as e:
    visual_block.Visual_Block_Info("接收文件列表", 8, 2, e)

    log.error("[%s] %s", "接收文件列表", e.message)
    raise e

# -*- 得到新的文件列表
try:
    visual_block.Visual_Block_Info("得到新的文件列表", 9, 0, "正在执行")

    for i, v in enumerate(file_list):
        file_list[i] = v.decode('utf-8')
        if v.decode('utf-8').endswith('.png') or v.decode('utf-8').endswith('.jpg') or v.decode('utf-8').endswith(
                '.pdf'):
            pass
        else:
            file_list.pop(i)

except Exception as e:
    visual_block.Visual_Block_Info("得到新的文件列表", 9, 2, e)

    log.error("[%s] %s", "得到新的文件列表", e.message)
    raise e

# -*- 文件索引
try:
    visual_block.Visual_Block_Info("文件索引", 10, 0, "正在执行")

    count_num = 0

except Exception as e:
    visual_block.Visual_Block_Info("文件索引", 10, 2, e)

    log.error("[%s] %s", "文件索引", e.message)
    raise e

# -*- 启动浏览器
try:
    visual_block.Visual_Block_Info("启动浏览器", 11, 0, "正在执行")

    option = ChromeOptions()
    prefs = {'safebrowsing.enabled': True}
    option.add_experimental_option('prefs', prefs)
    rpa_6a9438_browser = Chrome(option)

except Exception as e:
    visual_block.Visual_Block_Info("启动浏览器", 11, 2, e)

    log.error("[%s] %s", "启动浏览器", e.message)
    raise e

# -*- 浏览器窗口最大化
try:
    visual_block.Visual_Block_Info("浏览器窗口最大化", 12, 0, "正在执行")

    rpa_6a9438_browser.max_window()

except Exception as e:
    visual_block.Visual_Block_Info("浏览器窗口最大化", 12, 2, e)

    log.error("[%s] %s", "浏览器窗口最大化", e.message)
    raise e

# -*- 创建None变量
try:
    visual_block.Visual_Block_Info("创建None变量", 13, 0, "正在执行")

    cre_none = None

except Exception as e:
    visual_block.Visual_Block_Info("创建None变量", 13, 2, e)

    log.error("[%s] %s", "创建None变量", e.message)
    raise e

# -*- 遍历文件列表
try:
    visual_block.Visual_Block_Info("遍历文件列表", 14, 0, "正在执行")

    for rpa_4b969d_any in range(0, 10, 1):

        # -*- 打开网页
        try:
            rpa_c7ad3a = rpa_6a9438_browser.create("https://inv-veri.chinatax.gov.cn/index.html")

        except Exception as e:
            log.error("[%s] %s", "打开网页", e.message)
            raise e

        # -*- 点击高级
        try:
            from time import sleep

            sleep(0)
            rpa_c7ad3a.add_element("rpa_a0e023", id="details-button", css="",
                                   xpath=['//*[@id="details-button"]', '/html/body/div/div[2]/button[3]'], frame=[])
            rpa_c7ad3a.switch_to_frame_by_path([])
            from rpa import ElementClickMethod

            rpa_c7ad3a.get_element("rpa_a0e023", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "点击高级", e.message)
            raise e

        # -*- 点击继续前往
        try:
            from time import sleep

            sleep(0)
            rpa_c7ad3a.add_element("rpa_63002a", id="proceed-link", css="",
                                   xpath=['//*[@id="proceed-link"]', '/html/body/div/div[3]/p[2]/a'], frame=[])
            rpa_c7ad3a.switch_to_frame_by_path([])
            from rpa import ElementClickMethod

            rpa_c7ad3a.get_element("rpa_63002a", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "点击继续前往", e.message)
            raise e

        # -*- 得到文件
        try:
            rpa_573c3d_array_any = file_list[count_num]

        except Exception as e:
            log.error("[%s] %s", "得到文件", e.message)
            raise e

        # -*- 文件的绝对路径
        try:
            rpa_9a3dec_string = a_path + rpa_573c3d_array_any

        except Exception as e:
            log.error("[%s] %s", "文件的绝对路径", e.message)
            raise e

        # -*- 发票抽取
        try:
            from rpa.ocr.ocr import OCR

            rpa_4c4ea6 = OCR().recognize(rpa_9a3dec_string, 'invoice')

        except Exception as e:
            log.error("[%s] %s", "发票抽取", e.message)
            raise e

        # -*- 接受日期
        try:
            s = rpa_4c4ea6.get("开票日期")

        except Exception as e:
            log.error("[%s] %s", "接受日期", e.message)
            raise e

        # -*- 创建日期变量
        try:
            date_fin = []

        except Exception as e:
            log.error("[%s] %s", "创建日期变量", e.message)
            raise e

        # -*- 转换日期
        try:
            year = s.split('年')[0]
            month = s.split('年')[1].split('月')[0]
            day = s.split('年')[1].split('月')[1].split('日')[0]
            date_fin = [year + month + day]

        except Exception as e:
            log.error("[%s] %s", "转换日期", e.message)
            raise e

        # -*- 最终日期
        try:
            date_end = date_fin

        except Exception as e:
            log.error("[%s] %s", "最终日期", e.message)
            raise e

        # -*- 切片日期
        try:
            rpa_d412c4 = date_end[0]

        except Exception as e:
            log.error("[%s] %s", "切片日期", e.message)
            raise e

        # -*- 填写发票代码
        try:
            from time import sleep

            sleep(0)
            rpa_c7ad3a.add_element("rpa_4ea5ea", id="fpdm", css="#fpdm",
                                   xpath=["//input[@id='fpdm']", "//div[@id='content2']/table/tbody/tr/td[2]/input",
                                          "//input"], frame=[])
            rpa_c7ad3a.switch_to_frame_by_path([])
            rpa_c7ad3a.get_element("rpa_4ea5ea", timeout=30).input(rpa_4c4ea6.get("发票代码"), simulate=True)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "填写发票代码", e.message)
            raise e

        # -*- 填写发票号码
        try:
            from time import sleep

            sleep(0)
            rpa_c7ad3a.add_element("rpa_e2c4cd", id="fphm", css="#fphm",
                                   xpath=["//input[@id='fphm']", "//div[@id='content2']/table/tbody/tr[2]/td[2]/input",
                                          "//tr[2]/td[2]/input"], frame=[])
            rpa_c7ad3a.switch_to_frame_by_path([])
            rpa_c7ad3a.get_element("rpa_e2c4cd", timeout=30).input(rpa_4c4ea6.get("发票号码"), simulate=True)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "填写发票号码", e.message)
            raise e

        # -*- 填写开票日期
        try:
            from time import sleep

            sleep(0)
            rpa_c7ad3a.add_element("rpa_d3dd2f", id="kprq", css="#kprq", xpath=["//input[@id='kprq']",
                                                                                "//div[@id='content2']/table/tbody/tr[3]/td[2]/label/input",
                                                                                "//label/input"], frame=[])
            rpa_c7ad3a.switch_to_frame_by_path([])
            rpa_c7ad3a.get_element("rpa_d3dd2f", timeout=30).input(rpa_d412c4, simulate=True)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "填写开票日期", e.message)
            raise e

        # -*- 校验码变量
        try:
            yanz_str = rpa_4c4ea6.get("校验码")

        except Exception as e:
            log.error("[%s] %s", "校验码变量", e.message)
            raise e

        # -*- 字符串操作
        try:
            rpa_72858c = yanz_str[14:]

        except Exception as e:
            log.error("[%s] %s", "字符串操作", e.message)
            raise e

        # -*- 填写校验码后6位
        try:
            from time import sleep

            sleep(0)
            rpa_c7ad3a.add_element("rpa_34dc63", id="kjje", css="#kjje",
                                   xpath=["//input[@id='kjje']", "//div[@id='content2']/table/tbody/tr[4]/td[2]/input",
                                          "//tr[4]/td[2]/input"], frame=[])
            rpa_c7ad3a.switch_to_frame_by_path([])
            rpa_c7ad3a.get_element("rpa_34dc63", timeout=30).input(rpa_72858c, simulate=True)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "填写校验码后6位", e.message)
            raise e

        # -*- Excel行数
        try:
            row = 2

        except Exception as e:
            log.error("[%s] %s", "Excel行数", e.message)
            raise e

        # -*- 循环执行
        try:

            while "1" == "1":

                # -*- 获取成功网页元素
                try:
                    from time import sleep

                    sleep(0)
                    rpa_c7ad3a.add_element("rpa_426edb", id="fpcc_dzfp", css="#fpcc_dzfp",
                                           xpath=['//*[@id="fpcc_dzfp"]',
                                                  '/html/body/div/div/div[2]/div/div[1]/div[2]/div/h1'], frame=[0])
                    rpa_c7ad3a.switch_to_frame_by_path([0])
                    rpa_5a6268 = rpa_c7ad3a.get_element(element_name="rpa_426edb", index=0, timeout=5)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取成功网页元素", e.message)
                    raise e

                # -*- 条件判断
                try:

                    if rpa_5a6268 != cre_none:

                        # -*- 获取标题内容
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_c7ad3a.add_element("rpa_c42e4a", id="fpcc_dzfp", css="#fpcc_dzfp",
                                                   xpath=['//*[@id="fpcc_dzfp"]',
                                                          '/html/body/div/div/div[2]/div/div[1]/div[2]/div/h1'],
                                                   frame=[0])
                            rpa_c7ad3a.switch_to_frame_by_path([0])
                            rpa_6f20db_string = rpa_c7ad3a.get_element("rpa_c42e4a", timeout=30).text()
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取标题内容", e.message)
                            raise e

                        # -*- 打印日志
                        try:
                            from rpa import log

                            log.info("[%s] %s", "打印日志", rpa_6f20db_string)

                        except Exception as e:
                            log.error("[%s] %s", "打印日志", e.message)
                            raise e

                        # -*- 获取Table1
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_c7ad3a.add_element("rpa_856f3f", id="", css="",
                                                   xpath=['//*[@id="tabPage-dzfp"]/table[1]',
                                                          "/html/body/div/div/div[2]/div/div[1]/div[2]/div/table[1]"],
                                                   frame=[0])
                            rpa_c7ad3a.switch_to_frame_by_path([0])
                            rpa_99b83b = rpa_c7ad3a.get_element("rpa_856f3f", timeout=30).text_of_table(row=0)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取Table1", e.message)
                            raise e

                        # -*- 截图文件名
                        try:
                            rpa_7a42c3_string = "'截图'" + rpa_573c3d_array_any

                        except Exception as e:
                            log.error("[%s] %s", "截图文件名", e.message)
                            raise e

                        # -*- 截图的绝对路径
                        try:
                            rpa_9e704e_string = a_path + rpa_7a42c3_string

                        except Exception as e:
                            log.error("[%s] %s", "截图的绝对路径", e.message)
                            raise e

                        # -*- 成功页面截图
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_c7ad3a.add_element("rpa_98d82f", id="print_area", css="",
                                                   xpath=['//*[@id="print_area"]',
                                                          '/html/body/div[1]/div/div[2]/div/div[1]'], frame=[0])
                            rpa_c7ad3a.switch_to_frame_by_path([0])
                            rpa_c7ad3a.get_element("rpa_98d82f", timeout=30).screen_shot(rpa_9e704e_string)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "成功页面截图", e.message)
                            raise e

                        # -*- a_list
                        try:
                            a_list = rpa_99b83b

                        except Exception as e:
                            log.error("[%s] %s", "a_list", e.message)
                            raise e

                        # -*- b_list
                        try:
                            b_list = []

                        except Exception as e:
                            log.error("[%s] %s", "b_list", e.message)
                            raise e

                        # -*- 得到信息
                        try:
                            try:
                                visual_block.Visual_Block_Info("自定义脚本", 24, 0, "正在执行")
                                for i in a_list:
                                    a = i.split(':')
                                    b_list.append(a[1])
                                print b_list
                            except Exception as e:
                                visual_block.Visual_Block_Info("自定义脚本", 24, 2, e)
                                log.error("[%s] %s", "自定义脚本", e.message)
                                raise e

                        except Exception as e:
                            log.error("[%s] %s", "得到信息", e.message)
                            raise e

                        # -*- 写入信息
                        try:
                            import rpa.excel

                            rpa_6a4539_excel.get_sheet("").write("A" + str(row) + ":" + "E" + str(row), b_list)

                        except Exception as e:
                            log.error("[%s] %s", "写入信息", e.message)
                            raise e

                        # -*- 获取Table2
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_c7ad3a.add_element("rpa_856f3f", id="", css="",
                                                   xpath=['//*[@id="tabPage-dzfp"]/table[2]',
                                                          "/html/body/div/div/div[2]/div/div[1]/div[2]/div/table[2]"],
                                                   frame=[0])
                            rpa_c7ad3a.switch_to_frame_by_path([0])
                            rpa_d0d673 = rpa_c7ad3a.get_element("rpa_856f3f", timeout=30).text_of_table()
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取Table2", e.message)
                            raise e

                        # -*- 接收Table2
                        try:
                            a = rpa_d0d673

                        except Exception as e:
                            log.error("[%s] %s", "接收Table2", e.message)
                            raise e

                        # -*- 存储获取的信息
                        try:
                            a_info = []

                        except Exception as e:
                            log.error("[%s] %s", "存储获取的信息", e.message)
                            raise e

                        # -*- 得到金额
                        try:
                            b = a[4][0].replace('\t', '\n').split('\n')
                            for z in b:
                                if '小写' in z:
                                    a_info.append(z.split('￥')[1])

                        except Exception as e:
                            log.error("[%s] %s", "得到金额", e.message)
                            raise e

                        # -*- 对Table2进行处理
                        try:
                            for i, v in enumerate(a):
                                b = len(v)
                                if b == 5:
                                    a[i] = v[1:3]
                            for x in a[:4]:
                                a_info.append(x[1])
                            for y in a[5:]:
                                a_info.append(y[1])

                        except Exception as e:
                            log.error("[%s] %s", "对Table2进行处理", e.message)
                            raise e

                        # -*- 写入Table2信息
                        try:
                            import rpa.excel

                            rpa_6a4539_excel.get_sheet("").write("F" + str(row) + ":" + "M" + str(row), a_info)

                        except Exception as e:
                            log.error("[%s] %s", "写入Table2信息", e.message)
                            raise e

                        # -*- row + 1
                        try:
                            rpa_9ad017_number = row + 1

                        except Exception as e:
                            log.error("[%s] %s", "row + 1", e.message)
                            raise e

                        # -*- 赋值row
                        try:
                            row = rpa_9ad017_number

                        except Exception as e:
                            log.error("[%s] %s", "赋值row", e.message)
                            raise e

                        # -*- 索引加1
                        try:
                            rpa_8f3677_number = count_num + 1

                        except Exception as e:
                            log.error("[%s] %s", "索引加1", e.message)
                            raise e

                        # -*- 赋值索引
                        try:
                            count_num = rpa_8f3677_number

                        except Exception as e:
                            log.error("[%s] %s", "赋值索引", e.message)
                            raise e

                        # -*- 关闭网页
                        try:
                            rpa_c7ad3a.close()

                        except Exception as e:
                            log.error("[%s] %s", "关闭网页", e.message)
                            raise e

                        # -*- 退出循环
                        try:
                            break

                        except Exception as e:
                            log.error("[%s] %s", "退出循环", e.message)
                            raise e
                    else:

                        # -*- 获取失败网页元素
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_c7ad3a.add_element("rpa_f52617", id="", css="dialog", xpath=["//dialog"], frame=[])
                            rpa_c7ad3a.switch_to_frame_by_path([])
                            rpa_651248 = rpa_c7ad3a.get_element(element_name="rpa_f52617", index=0, timeout=5)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取失败网页元素", e.message)
                            raise e

                        # -*- 打印日志12
                        try:
                            from rpa import log

                            log.info("[%s] %s", "打印日志12", rpa_651248)

                        except Exception as e:
                            log.error("[%s] %s", "打印日志12", e.message)
                            raise e

                        # -*- 条件判断1
                        try:

                            if rpa_651248 != cre_none:

                                # -*- 获取网页元素
                                try:
                                    from time import sleep

                                    sleep(0)
                                    rpa_c7ad3a.add_element("rpa_5f6b4e", id="", css="",
                                                           xpath=['//*[@id="cyjg"]',
                                                                  '/html/body/div/div/div/div[1]/table/tbody/tr/td/span[1]/strong'],
                                                           frame=[0])
                                    rpa_c7ad3a.switch_to_frame_by_path([0])
                                    rpa_ff4f7c_webelement = rpa_c7ad3a.get_element(element_name="rpa_5f6b4e", index=0,
                                                                                   timeout=30)
                                    sleep(0)

                                except Exception as e:
                                    log.error("[%s] %s", "获取网页元素", e.message)
                                    raise e

                                # -*- 打印日志13
                                try:
                                    from rpa import log

                                    log.info("[%s] %s", "打印日志13", rpa_ff4f7c_webelement)

                                except Exception as e:
                                    log.error("[%s] %s", "打印日志13", e.message)
                                    raise e
                                    # -*- 获取网页元素内容
                                try:
                                    from time import sleep

                                    sleep(0)
                                    rpa_c7ad3a.switch_to_frame_by_path(rpa_ff4f7c_webelement.frame)
                                    rpa_318eed_string = rpa_ff4f7c_webelement.text()
                                    print type(rpa_318eed_string)
                                    print rpa_318eed_string
                                    sleep(0)

                                except Exception as e:
                                    log.error("[%s] %s", "获取网页元素内容", e.message)
                                    raise e
                                # -*- 退出程序
                                try:
                                    exit(0)

                                except Exception as e:
                                    log.error("[%s] %s", "退出程序", e.message)
                                    raise e
                            else:

                                # -*- 退出循环1
                                try:
                                    continue

                                except Exception as e:
                                    log.error("[%s] %s", "退出循环1", e.message)
                                    raise e
                        except Exception as e:
                            log.error("[%s] %s", "条件判断1", e.message)
                            raise e
                except Exception as e:
                    log.error("[%s] %s", "条件判断", e.message)
                    raise e
        except Exception as e:
            log.error("[%s] %s", "循环执行", e.message)
            raise e
except Exception as e:
    visual_block.Visual_Block_Info("遍历文件列表", 14, 2, e)

    log.error("[%s] %s", "遍历文件列表", e.message)
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", e.message)
