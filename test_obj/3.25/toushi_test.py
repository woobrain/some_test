# -*- coding:utf-8 -*-

from rpa import Chrome, IE, log, ChromeOptions, update_panel
from rpa.excel import sheet_datagrand
from rpa.parameter_panel.exception_capture import exception_capture
from rpa.visual_block.visual_block import VisualBlock
import sys, os

__taskId = None
__errorCapturePath = None
try:
    import getopt

    opts, _ = getopt.getopt(sys.argv[2:], '-h-t:-p:', ['help', 'taskId='])
    for k, v in opts:
        if k in ('-t', '--taskId'):
            __taskId = v
        elif k == '-p' and v and v.strip() != '0':
            __errorCapturePath = v.strip()
except Exception as e:
    pass
try:
    import pywinauto
except:
    pass
visual_block = VisualBlock(taskId=__taskId)
visual_block.Visual_Block_Total_Block(3)

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

# -*- 打开 Excel 文档
try:
    visual_block.Visual_Block_Info("打开 Excel 文档", 1, 0, "正在执行")

    import rpa.excel

    rpa_1fa051_excel = rpa.excel.open(r"C:\\Users\\Administrator\\Desktop\\保费匹配表.xlsx", visible=True, readonly=False,
                                      pass_word="", wps=False)

except Exception as e:
    exception_capture(__errorCapturePath, "打开 Excel 文档", __taskId)
    visual_block.Visual_Block_Info("打开 Excel 文档", 1, 2, str(e))

    log.error("[%s] %s", "打开 Excel 文档", str(e))
    raise e

# -*- 新建 Sheet 页
try:
    visual_block.Visual_Block_Info("新建 Sheet 页", 2, 0, "正在执行")

    import rpa.excel

    rpa_1fa051_excel.add_sheet(sheet_name="sh3", location="汇总表", relative="after")

except Exception as e:
    exception_capture(__errorCapturePath, "新建 Sheet 页", __taskId)
    visual_block.Visual_Block_Info("新建 Sheet 页", 2, 2, str(e))

    log.error("[%s] %s", "新建 Sheet 页", str(e))
    raise e

# -*- 创建透视表
try:
    visual_block.Visual_Block_Info("创建透视表", 3, 0, "正在执行")

    import rpa.excel
    print(help(sheet_datagrand.Sheet.create_pivottable))
    rpa_edeb62_string = rpa_1fa051_excel.get_sheet("汇总表").create_pivottable("A1:Q30", "123", "A:R", "sh3",{"filter": [""], "row": [""],"column": [""], "data": {"实缴保费": "计数"}})

except Exception as e:
    exception_capture(__errorCapturePath, "创建透视表", __taskId)
    visual_block.Visual_Block_Info("创建透视表", 3, 2, str(e))

    log.error("[%s] %s", "创建透视表", str(e))
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", str(e))
