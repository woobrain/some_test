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
    log.error("[%s] %s", "参数面板", str(e))

# -*- 传入的JSON
try:

    update_panel(sys.argv, PANEL_VARS)

except Exception as e:
    log.error("[%s] %s", "传入的JSON", str(e))

# -*- 启动浏览器
try:
    visual_block.Visual_Block_Info("启动浏览器", 1, 0, "正在执行")

    option = ChromeOptions()
    prefs = {'safebrowsing.enabled': True}
    option.add_experimental_option('prefs', prefs)
    rpa_1a41b1_browser = Chrome(option)

except Exception as e:
    visual_block.Visual_Block_Info("启动浏览器", 1, 2, e)

    log.error("[%s] %s", "启动浏览器", str(e))
    raise e

# -*- 打开网页
try:
    visual_block.Visual_Block_Info("打开网页", 2, 0, "正在执行")

    rpa_fcda63_webpage = rpa_1a41b1_browser.create("https://www.gelonghui.com/tag/research")

except Exception as e:
    visual_block.Visual_Block_Info("打开网页", 2, 2, e)

    log.error("[%s] %s", "打开网页", str(e))
    raise e

# -*- 浏览器最大化
try:
    visual_block.Visual_Block_Info("浏览器最大化", 3, 0, "正在执行")

    rpa_1a41b1_browser.max_window()

except Exception as e:
    visual_block.Visual_Block_Info("浏览器最大化", 3, 2, e)

    log.error("[%s] %s", "浏览器最大化", str(e))
    raise e

# -*- 创建url_str
try:
    visual_block.Visual_Block_Info("创建url_str", 4, 0, "正在执行")

    url_str = ''

except Exception as e:
    visual_block.Visual_Block_Info("创建url_str", 4, 2, e)

    log.error("[%s] %s", "创建url_str", str(e))
    raise e

# -*- 创建pdf_str
try:
    visual_block.Visual_Block_Info("创建pdf_str", 5, 0, "正在执行")

    pdf_str = ''

except Exception as e:
    visual_block.Visual_Block_Info("创建pdf_str", 5, 2, e)

    log.error("[%s] %s", "创建pdf_str", str(e))
    raise e

# -*- 创建file_name
try:
    visual_block.Visual_Block_Info("创建file_name", 6, 0, "正在执行")

    file_name = ''

except Exception as e:
    visual_block.Visual_Block_Info("创建file_name", 6, 2, e)

    log.error("[%s] %s", "创建file_name", str(e))
    raise e

# -*- 创建time_str
try:
    visual_block.Visual_Block_Info("创建time_str", 7, 0, "正在执行")

    time_str = ''

except Exception as e:
    visual_block.Visual_Block_Info("创建time_str", 7, 2, e)

    log.error("[%s] %s", "创建time_str", str(e))
    raise e

# -*- 创建t_str
try:
    visual_block.Visual_Block_Info("创建t_str", 8, 0, "正在执行")

    t_str = ''

except Exception as e:
    visual_block.Visual_Block_Info("创建t_str", 8, 2, e)

    log.error("[%s] %s", "创建t_str", str(e))
    raise e

# -*- 创建p_date
try:
    visual_block.Visual_Block_Info("创建p_date", 9, 0, "正在执行")

    p_date = ''

except Exception as e:
    visual_block.Visual_Block_Info("创建p_date", 9, 2, e)

    log.error("[%s] %s", "创建p_date", str(e))
    raise e

# -*- 创建old_ele
try:
    visual_block.Visual_Block_Info("创建old_ele", 10, 0, "正在执行")

    old_ele = 6000

except Exception as e:
    visual_block.Visual_Block_Info("创建old_ele", 10, 2, e)

    log.error("[%s] %s", "创建old_ele", str(e))
    raise e

# -*- 创建new_list
try:
    visual_block.Visual_Block_Info("创建new_list", 11, 0, "正在执行")

    new_list = ''

except Exception as e:
    visual_block.Visual_Block_Info("创建new_list", 11, 2, e)

    log.error("[%s] %s", "创建new_list", str(e))
    raise e

# -*- 创建flag
try:
    visual_block.Visual_Block_Info("创建flag", 12, 0, "正在执行")

    flag = 0

except Exception as e:
    visual_block.Visual_Block_Info("创建flag", 12, 2, e)

    log.error("[%s] %s", "创建flag", str(e))
    raise e

# -*- 创建count
try:
    visual_block.Visual_Block_Info("创建count", 13, 0, "正在执行")

    count = 1

except Exception as e:
    visual_block.Visual_Block_Info("创建count", 13, 2, e)

    log.error("[%s] %s", "创建count", str(e))
    raise e

# -*- 点击次数
try:
    visual_block.Visual_Block_Info("点击次数", 14, 0, "正在执行")

    while "1" == "1":

        # -*- 判断flag
        try:

            if flag == 1:

                # -*- 退出循环2
                try:
                    break

                except Exception as e:
                    log.error("[%s] %s", "退出循环2", str(e))
                    raise e
            else:
                pass

        except Exception as e:
            log.error("[%s] %s", "判断flag", str(e))
            raise e

        # -*- 异常处理22
        try:
            try:

                # -*- 获取加载更多元素21
                try:
                    from time import sleep

                    sleep(0)
                    rpa_fcda63_webpage.add_element("rpa_c54ce8", id="waterfall", css="#waterfall",
                                                   xpath=["//p[@id='waterfall']",
                                                          "//div[@id='__layout']/div/section/section/section/section/div/section[2]/p",
                                                          "//section[2]/p", "//p[contains(.,'加载更多')]"], frame=[])
                    rpa_fcda63_webpage.switch_to_frame_by_path([])
                    rpa_00bd99 = rpa_fcda63_webpage.get_element(element_name="rpa_c54ce8", index=0, timeout=30)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取加载更多元素21", str(e))
                    raise e

                # -*- 获取加载更多子元素31
                try:
                    from time import sleep

                    sleep(0)
                    rpa_00bd99.switch_to_frame()
                    rpa_e86ba3 = rpa_00bd99.children(index=0)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取加载更多子元素31", str(e))
                    raise e

                # -*- 点击加载更多1
                try:
                    from time import sleep

                    sleep(0)
                    rpa_fcda63_webpage.switch_to_frame_by_path(rpa_e86ba3.frame)
                    from rpa import ElementClickMethod

                    rpa_e86ba3.click(method=ElementClickMethod.ELEMENT_CLICK)
                    sleep(1)

                except Exception as e:
                    log.error("[%s] %s", "点击加载更多1", str(e))
                    raise e

                # -*- 数学运算
                try:
                    rpa_d84fd0 = count + 1

                except Exception as e:
                    log.error("[%s] %s", "数学运算", str(e))
                    raise e

                # -*- 赋值操作2
                try:
                    count = rpa_d84fd0

                except Exception as e:
                    log.error("[%s] %s", "赋值操作2", str(e))
                    raise e

                # -*- 条件判断3
                try:

                    if count <= 1100:

                        # -*- 退出循环3
                        try:
                            continue

                        except Exception as e:
                            log.error("[%s] %s", "退出循环3", str(e))
                            raise e
                    else:
                        pass

                except Exception as e:
                    log.error("[%s] %s", "条件判断3", str(e))
                    raise e
            except Exception as e:

                # -*- 退出循环4
                try:
                    break

                except Exception as e:
                    log.error("[%s] %s", "退出循环4", str(e))
                    raise e
            finally:
                pass

        except Exception as e:
            log.error("[%s] %s", "异常处理22", str(e))
            raise e

        # -*- 获取列表总元素1
        try:
            from time import sleep

            sleep(0)
            rpa_fcda63_webpage.add_element("rpa_e686c2", id="", css=".article-ul", xpath=[
                "//div[@id='__layout']/div/section/section/section/section/div/section/section/ul",
                "//div/section/section/ul"], frame=[])
            rpa_fcda63_webpage.switch_to_frame_by_path([])
            rpa_25ca06 = rpa_fcda63_webpage.get_element(element_name="rpa_e686c2", index=0, timeout=30)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取列表总元素1", str(e))
            raise e

        # -*- 获取总列表子元素11
        try:
            from time import sleep

            sleep(0)
            rpa_25ca06.switch_to_frame()
            rpa_47b178 = rpa_25ca06.children(index=None)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取总列表子元素11", str(e))
            raise e

        # -*- 创建变量1
        try:
            new_ele = rpa_47b178

        except Exception as e:
            log.error("[%s] %s", "创建变量1", str(e))
            raise e

        # -*- 创建z_list
        try:
            z_list = rpa_47b178

        except Exception as e:
            log.error("[%s] %s", "创建z_list", str(e))
            raise e

        # -*- 自定义脚本31
        try:
            a_len = len(z_list)
            # print(a_len)
            new_list = z_list[old_ele::]
            # print(new_list)
            old_ele = a_len
            # print(old_ele)
            z_list = z_list[-1]
            # print(z_list)

        except Exception as e:
            log.error("[%s] %s", "自定义脚本31", str(e))
            raise e

        # -*- 获取列表元素41
        try:
            from time import sleep

            sleep(0)
            z_list.switch_to_frame()
            rpa_e890db = z_list.children(index=1)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取列表元素41", str(e))
            raise e

        # -*- 获取日期标签1
        try:
            from time import sleep

            sleep(0)
            rpa_e890db.switch_to_frame()
            rpa_a0bb27 = rpa_e890db.children(index=1)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取日期标签1", str(e))
            raise e

        # -*- 获取日期子标签1
        try:
            from time import sleep

            sleep(0)
            rpa_a0bb27.switch_to_frame()
            rpa_9ece18 = rpa_a0bb27.children(index=None)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取日期子标签1", str(e))
            raise e

        # -*- 创建d_date1
        try:
            d_date = rpa_9ece18

        except Exception as e:
            log.error("[%s] %s", "创建d_date1", str(e))
            raise e

        # -*- 得到日期1
        try:
            d_date = d_date[-1]

        except Exception as e:
            log.error("[%s] %s", "得到日期1", str(e))
            raise e

        # -*- 获取日期内容1
        try:
            from time import sleep

            sleep(0)
            rpa_fcda63_webpage.switch_to_frame_by_path(d_date.frame)
            rpa_e0e1ca = d_date.text()
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取日期内容1", str(e))
            raise e

        # -*- 赋值time_str1
        try:
            t_str = rpa_e0e1ca

        except Exception as e:
            log.error("[%s] %s", "赋值time_str1", str(e))
            raise e

        # -*- 判断日期1
        try:
            import datetime

            a_str = datetime.datetime.strptime('2019年1月14日08时21分', '%Y年%m月%d日%H时%M分')
            # if len(t_str) >= 7:
            #     pass
            # else:
            #     continue
            # if len(t_str) > 11:
            aa = datetime.datetime.strptime(t_str, '%Y年%m月%d日%H时%M分')
            if aa < a_str:
                pass
            else:
                continue
            # else:
            #     continue
            new_list = new_list[::-1]
            new_list = new_list[2500::]

        except Exception as e:
            log.error("[%s] %s", "判断日期1", str(e))
            raise e

        # -*- 遍历列表1
        try:

            for rpa_cef005 in rpa_47b178:

                # -*- 异常处理11
                try:
                    try:

                        # -*- 获取列表元素421
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_cef005.switch_to_frame()
                            rpa_c052bb = rpa_cef005.children(index=1)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取列表元素421", str(e))
                            raise e

                        # -*- 获取日期标签21
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_c052bb.switch_to_frame()
                            rpa_6e3d92 = rpa_c052bb.children(index=1)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取日期标签21", str(e))
                            raise e

                        # -*- 获取日期子标签21
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_6e3d92.switch_to_frame()
                            rpa_c166b8 = rpa_6e3d92.children(index=None)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取日期子标签21", str(e))
                            raise e

                        # -*- 赋值操作1
                        try:
                            p_date = rpa_c166b8

                        except Exception as e:
                            log.error("[%s] %s", "赋值操作1", str(e))
                            raise e

                        # -*- 得到日期21
                        try:
                            p_date = p_date[-1]

                        except Exception as e:
                            log.error("[%s] %s", "得到日期21", str(e))
                            raise e

                        # -*- 获取日期内容21
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_fcda63_webpage.switch_to_frame_by_path(p_date.frame)
                            rpa_4cf6d9 = p_date.text()
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取日期内容21", str(e))
                            raise e

                        # -*- 赋值time_str21
                        try:
                            time_str = rpa_4cf6d9

                        except Exception as e:
                            log.error("[%s] %s", "赋值time_str21", str(e))
                            raise e

                        # -*- 判断日期21
                        try:
                            import datetime

                            a_str = datetime.datetime.strptime('2018年12月6日15时22分', '%Y年%m月%d日%H时%M分')
                            # if len(time_str) > 11:
                            # print(time_str)
                            dateTime_p = datetime.datetime.strptime(time_str, '%Y年%m月%d日%H时%M分')
                            print(dateTime_p)
                            if dateTime_p > a_str:
                                pass
                            elif dateTime_p.year < 2017:
                                flag = 1
                                break
                            else:
                                continue
                            # else:
                            #     continue
                            # import datetime
                            # # a_str = datetime.datetime.strptime('2019年12月10日17时42分','%Y年%m月%d日%H时%M分')
                            # if len(time_str) > 11:
                            #     dateTime_p = datetime.datetime.strptime(time_str,'%Y年%m月%d日%H时%M分')
                            #     if dateTime_p.year >= 2019:
                            #         pass
                            #     elif dateTime_p.year < 2019:
                            #         break
                            # else:
                            #     pass

                        except Exception as e:
                            log.error("[%s] %s", "判断日期21", str(e))
                            raise e

                        # -*- 获取标题子元素41
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_c052bb.switch_to_frame()
                            rpa_68937f = rpa_c052bb.children(index=0)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取标题子元素41", str(e))
                            raise e

                        # -*- 获取标题子子元素51
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_68937f.switch_to_frame()
                            rpa_2f1a6f = rpa_68937f.children(index=0)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取标题子子元素51", str(e))
                            raise e

                        # -*- 获取标题内容1
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_fcda63_webpage.switch_to_frame_by_path(rpa_2f1a6f.frame)
                            rpa_e5514d = rpa_2f1a6f.text()
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取标题内容1", str(e))
                            raise e

                        # -*- 赋值file_name1
                        try:
                            file_name = rpa_e5514d

                        except Exception as e:
                            log.error("[%s] %s", "赋值file_name1", str(e))
                            raise e

                        # -*- 得到file_name1
                        try:
                            b = {'?': '', '*': '', '|': '', '/': '', '\\': '', '"': '', "'": '', '<': '', '>': '',
                                 '[': '', ']': '', '{': '', '}': '', ':': '：', '(': '（', ')': '）', '&': '和', '!': '！',
                                 '^': ''}
                            for k, v in b.items():
                                if k in file_name:
                                    file_name = file_name.replace(k, v)

                        except Exception as e:
                            log.error("[%s] %s", "得到file_name1", str(e))
                            raise e

                        # -*- 拼接文件名1
                        try:
                            rpa_2bd1e0 = file_name + ".pdf"

                        except Exception as e:
                            log.error("[%s] %s", "拼接文件名1", str(e))
                            raise e

                        # -*- 打印日志21
                        try:
                            from rpa import log

                            log.info("[%s] %s", "打印日志21", rpa_e5514d)

                        except Exception as e:
                            log.error("[%s] %s", "打印日志21", str(e))
                            raise e

                        # -*- 获取标题网址1
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_fcda63_webpage.switch_to_frame_by_path(rpa_68937f.frame)
                            rpa_8d6105 = rpa_68937f.get_attr("href")
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取标题网址1", str(e))
                            raise e

                        # -*- 赋值给url_str1
                        try:
                            url_str = rpa_8d6105

                        except Exception as e:
                            log.error("[%s] %s", "赋值给url_str1", str(e))
                            raise e

                        # -*- 获取下载地址1
                        try:
                            import requests
                            import re

                            a = requests.get(url_str)
                            b = re.search(r'https://img3.gelonghui.com/pdf/[\w|\-|.]+', a.content.decode('utf-8'))
                            if b is not None:
                                pdf_str = b.group()
                            else:
                                continue


                        except Exception as e:
                            log.error("[%s] %s", "获取下载地址1", str(e))
                            raise e

                        # -*- 异常处理21
                        try:
                            try:

                                # -*- 下载1
                                try:
                                    import requests
                                    import os

                                    rpa_08f26b = open(
                                        os.path.join("C:\\Users\\Administrator\\Desktop\\new", rpa_2bd1e0), "wb")
                                    rpa_08f26b.write(requests.get(pdf_str).content)
                                    rpa_08f26b.close()

                                except Exception as e:
                                    log.error("[%s] %s", "下载1", str(e))
                                    raise e

                                # -*- 写入csv1
                                try:
                                    import csv

                                    with open("C:\\Users\\Administrator\\Desktop\\gelonghui.csv", "a", newline='',
                                              encoding='utf-8') as csvfile:
                                        writer = csv.writer(csvfile)
                                        # 先写入columns_name
                                        writer.writerow([file_name, pdf_str])

                                except Exception as e:
                                    log.error("[%s] %s", "写入csv1", str(e))
                                    raise e
                            except Exception as e:
                                pass

                            finally:
                                pass

                        except Exception as e:
                            log.error("[%s] %s", "异常处理21", str(e))
                            raise e
                    except Exception as e:

                        # -*- 打印日志41
                        try:
                            from rpa import log

                            log.info("[%s] %s", "打印日志41", "1111111111111111111111111111111111")

                        except Exception as e:
                            log.error("[%s] %s", "打印日志41", str(e))
                            raise e
                    finally:
                        pass

                except Exception as e:
                    log.error("[%s] %s", "异常处理11", str(e))
                    raise e
        except Exception as e:
            log.error("[%s] %s", "遍历列表1", str(e))
            raise e
except Exception as e:
    visual_block.Visual_Block_Info("点击次数", 14, 2, e)

    log.error("[%s] %s", "点击次数", str(e))
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", str(e))
