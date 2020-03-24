# -*- coding:utf-8 -*-

from rpa import Chrome, IE, log, ChromeOptions, update_panel
from rpa.visual_block.visual_block import VisualBlock
import sys, os

__taskId=None
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
visual_block.Visual_Block_Total_Block(1)

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


# -*- 解压文件
try:
    visual_block.Visual_Block_Info("解压文件", 1, 0, "正在执行")

    import rpa.file_folder
    rpa_f19e96_array_string = rpa.file_folder.unzip_file(zip_src=r"C:\\Users\\Administrator\\Desktop\\poc用例.zip", dst_dir=None, cover=True)

except Exception as e:
    visual_block.Visual_Block_Info("解压文件", 1, 2, e)

    log.error("[%s] %s", "解压文件", str(e))
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", str(e))
