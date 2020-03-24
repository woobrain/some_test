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
visual_block.Visual_Block_Total_Block(9)

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

# -*- 打开流水账单文档
try:
    visual_block.Visual_Block_Info("打开流水账单文档", 1, 0, "正在执行")

    import rpa.excel

    rpa_141104_excel = rpa.excel.open(r"C:\\Users\\Administrator\\Desktop\\题目五\\银行流水.xls", visible=True, readonly=False,
                                      pass_word="", wps=True)

except Exception as e:
    visual_block.Visual_Block_Info("打开流水账单文档", 1, 2, e)

    log.error("[%s] %s", "打开流水账单文档", e.message)
    raise e

# -*- 打开CSV文档
try:
    visual_block.Visual_Block_Info("打开CSV文档", 2, 0, "正在执行")

    import rpa.excel

    rpa_3fe138_excel = rpa.excel.open(r"C:\\Users\\Administrator\\Desktop\\题目五\\jd20191203.csv", visible=True,
                                      readonly=False, pass_word="", wps=True)

except Exception as e:
    visual_block.Visual_Block_Info("打开CSV文档", 2, 2, e)

    log.error("[%s] %s", "打开CSV文档", e.message)
    raise e

# -*- 新建金额不一致文档
try:
    visual_block.Visual_Block_Info("新建金额不一致文档", 3, 0, "正在执行")

    import rpa.excel

    rpa_95ec18_excel = rpa.excel.create(visible=True, wps=True)

except Exception as e:
    visual_block.Visual_Block_Info("新建金额不一致文档", 3, 2, e)

    log.error("[%s] %s", "新建金额不一致文档", e.message)
    raise e

# -*- 读取流水账单内容
try:
    visual_block.Visual_Block_Info("读取流水账单内容", 4, 0, "正在执行")

    import rpa.excel

    rpa_9bd41b_array_any = rpa_141104_excel.get_sheet("").read()

except Exception as e:
    visual_block.Visual_Block_Info("读取流水账单内容", 4, 2, e)

    log.error("[%s] %s", "读取流水账单内容", e.message)
    raise e

# -*- 所有账单列表
try:
    visual_block.Visual_Block_Info("所有账单列表", 5, 0, "正在执行")

    use_list = rpa_9bd41b_array_any
    print use_list

except Exception as e:
    visual_block.Visual_Block_Info("所有账单列表", 5, 2, e)

    log.error("[%s] %s", "所有账单列表", e.message)
    raise e

# -*- 读取CSV中内容
try:
    visual_block.Visual_Block_Info("读取CSV中内容", 6, 0, "正在执行")

    import rpa.excel

    rpa_f189a2 = rpa_3fe138_excel.get_sheet("").read("A", skip=0, max=10)

except Exception as e:
    visual_block.Visual_Block_Info("读取CSV中内容", 6, 2, e)

    log.error("[%s] %s", "读取CSV中内容", e.message)
    raise e

# -*- 所有信息列表
try:
    visual_block.Visual_Block_Info("所有信息列表", 7, 0, "正在执行")

    ca_list = rpa_f189a2

except Exception as e:
    visual_block.Visual_Block_Info("所有信息列表", 7, 2, e)

    log.error("[%s] %s", "所有信息列表", e.message)
    raise e

# -*- 创建索引
try:
    visual_block.Visual_Block_Info("创建索引", 8, 0, "正在执行")

    use_index = 0

except Exception as e:
    visual_block.Visual_Block_Info("创建索引", 8, 2, e)

    log.error("[%s] %s", "创建索引", e.message)
    raise e

# -*- 创建Excel行数
try:
    visual_block.Visual_Block_Info("创建Excel行数", 9, 0, "正在执行")

    row = 2

except Exception as e:
    visual_block.Visual_Block_Info("创建Excel行数", 9, 2, e)

    log.error("[%s] %s", "创建Excel行数", e.message)
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", e.message)
