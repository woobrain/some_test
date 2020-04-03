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
visual_block.Visual_Block_Total_Block(5)

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


# -*- 打开 Excel 文档
try:
    visual_block.Visual_Block_Info("打开 Excel 文档", 1, 0, "正在执行")

    import rpa.excel
    rpa_ac8955_excel = rpa.excel.open(r"C:\\Users\\Administrator\\Desktop\\POC 用例.xls", visible=True, readonly=False, pass_word="", wps=False)

except Exception as e:
    exception_capture(__errorCapturePath, "打开 Excel 文档", __taskId)
    visual_block.Visual_Block_Info("打开 Excel 文档", 1, 2, str(e))

    log.error("[%s] %s", "打开 Excel 文档", str(e))
    raise e

# -*- 读取内容
try:
    visual_block.Visual_Block_Info("读取内容", 2, 0, "正在执行")

    import rpa.excel
    rpa_70594c_array_any = rpa_ac8955_excel.get_sheet("").read()

except Exception as e:
    exception_capture(__errorCapturePath, "读取内容", __taskId)
    visual_block.Visual_Block_Info("读取内容", 2, 2, str(e))

    log.error("[%s] %s", "读取内容", str(e))
    raise e

# -*- 读取企业名称列
try:
    visual_block.Visual_Block_Info("读取企业名称列", 3, 0, "正在执行")

    import rpa.excel
    rpa_0d7b56_array_any = rpa_ac8955_excel.get_sheet("").read("B", skip=0, max=1000)

except Exception as e:
    exception_capture(__errorCapturePath, "读取企业名称列", __taskId)
    visual_block.Visual_Block_Info("读取企业名称列", 3, 2, str(e))

    log.error("[%s] %s", "读取企业名称列", str(e))
    raise e

# -*- 读取抵押物信息列
try:
    visual_block.Visual_Block_Info("读取抵押物信息列", 4, 0, "正在执行")

    import rpa.excel
    rpa_594850 = rpa_ac8955_excel.get_sheet("").read("F", skip=0, max=1000)

except Exception as e:
    exception_capture(__errorCapturePath, "读取抵押物信息列", __taskId)
    visual_block.Visual_Block_Info("读取抵押物信息列", 4, 2, str(e))

    log.error("[%s] %s", "读取抵押物信息列", str(e))
    raise e

# -*- 处理txt
try:
    visual_block.Visual_Block_Info("处理txt", 5, 0, "正在执行")

    rpa_0d7b56_array_any = rpa_0d7b56_array_any[:len(rpa_0d7b56_array_any)-1:]
    b = rpa_0d7b56_array_any[::]
    for i, k in enumerate(b):
        v = rpa_0d7b56_array_any.count(k)
        if v > 1:
            b[i] = str(i + 1) + k
    rpa_594850 = rpa_594850[:len(rpa_594850)-1:]
    for k,i in enumerate(b):
        desktop_path = "C:\\Users\\Administrator\\Desktop\\poc用例\\"  # 新创建的txt文件的存放路径
        full_path = desktop_path + i + '.txt'  # 也可以创建一个.doc的word文档
        with open(full_path, 'wb') as f:
            f.write(rpa_594850[k].encode('utf-8'))

except Exception as e:
    exception_capture(__errorCapturePath, "处理txt", __taskId)
    visual_block.Visual_Block_Info("处理txt", 5, 2, str(e))

    log.error("[%s] %s", "处理txt", str(e))
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", str(e))
