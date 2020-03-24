# -*- coding:utf-8 -*-

from rpa import Chrome, IE, log, ChromeOptions, update_panel
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
visual_block.Visual_Block_Total_Block(44)

# -*- 参数面板
try:

    PANEL_VARS = {
    }

except Exception as e:
    log.error("[%s] %s", "参数面板", str(e))

# -*- 传入的JSON
try:

    update_panel(sys.argv,PANEL_VARS)

except Exception as e:
    log.error("[%s] %s", "传入的JSON", str(e))


# -*- 打开/新建 Excel 文档
try:
    visual_block.Visual_Block_Info("打开/新建 Excel 文档", 1, 0, "正在执行")

    import rpa.excel
    rpa_f2fd63_excel = rpa.excel.open(r"C:\\Users\\Administrator\\Desktop\\四川picc\\new\\保费匹配表.xlsx", visible=True, readonly=False, pass_word="", wps=False)

except Exception as e:
    exception_capture(__errorCapturePath, "打开/新建 Excel 文档", __taskId)
    visual_block.Visual_Block_Info("打开/新建 Excel 文档", 1, 2, str(e))

    log.error("[%s] %s", "打开/新建 Excel 文档", str(e))
    raise e

# -*- 创建透视表
try:
    visual_block.Visual_Block_Info("创建透视表", 2, 0, "正在执行")

    import rpa.excel
    rpa_4bc301_string = rpa_f2fd63_excel.get_sheet("汇总表").create_pivottable("A:R", "", "A3", "",{"filter":[""], "row":[""], "column":["机构"], "data":{"":"求和"}})

except Exception as e:
    exception_capture(__errorCapturePath, "创建透视表", __taskId)
    visual_block.Visual_Block_Info("创建透视表", 2, 2, str(e))

    log.error("[%s] %s", "创建透视表", str(e))
    raise e


exit(0)