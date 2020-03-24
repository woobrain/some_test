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
visual_block.Visual_Block_Total_Block(28)

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

# -*- 解压文件
try:
    visual_block.Visual_Block_Info("解压文件", 1, 0, "正在执行")

    import rpa.file_folder

    rpa_d6419b_array_string = rpa.file_folder.unzip_file(
        zip_src=r"C:\\Users\\Administrator\\Desktop\\DOC\\20191203.zip", dst_dir=r"C:\\Users\\Administrator\\Desktop\\DOC", cover=True)

except Exception as e:
    visual_block.Visual_Block_Info("解压文件", 1, 2, e)

    log.error("[%s] %s", "解压文件", e.message)
    raise e

# -*- 退出程序
try:
    visual_block.Visual_Block_Info("退出程序", 2, 0, "正在执行")

    exit(0)

except Exception as e:
    visual_block.Visual_Block_Info("退出程序", 2, 2, e)

    log.error("[%s] %s", "退出程序", e.message)
    raise e

# -*- 新建 Excel 文档
try:
    visual_block.Visual_Block_Info("新建 Excel 文档", 3, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel = rpa.excel.create(visible=True, wps=True)

except Exception as e:
    visual_block.Visual_Block_Info("新建 Excel 文档", 3, 2, e)

    log.error("[%s] %s", "新建 Excel 文档", e.message)
    raise e

# -*- 打开 Excel 文档1
try:
    visual_block.Visual_Block_Info("打开 Excel 文档1", 4, 0, "正在执行")

    import rpa.excel

    rpa_39f0f1_excel = rpa.excel.open(r"C:\\Users\\Administrator\\Desktop\\DOC\\20191203\\流水一.xlsx", visible=True,
                                      readonly=False, pass_word="", wps=False)

except Exception as e:
    visual_block.Visual_Block_Info("打开 Excel 文档1", 4, 2, e)

    log.error("[%s] %s", "打开 Excel 文档1", e.message)
    raise e

# -*- 操作单元格
try:
    visual_block.Visual_Block_Info("操作单元格", 5, 0, "正在执行")

    import rpa.excel

    rpa_39f0f1_excel.get_sheet("").copy()

except Exception as e:
    visual_block.Visual_Block_Info("操作单元格", 5, 2, e)

    log.error("[%s] %s", "操作单元格", e.message)
    raise e

# -*- 操作单元格1
try:
    visual_block.Visual_Block_Info("操作单元格1", 6, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel.get_sheet("").paste("A", "1", type="全部")

except Exception as e:
    visual_block.Visual_Block_Info("操作单元格1", 6, 2, e)

    log.error("[%s] %s", "操作单元格1", e.message)
    raise e

# -*- 操作 Sheet 页1
try:
    visual_block.Visual_Block_Info("操作 Sheet 页1", 7, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel.rename_sheet("Sheet1", "流水1")

except Exception as e:
    visual_block.Visual_Block_Info("操作 Sheet 页1", 7, 2, e)

    log.error("[%s] %s", "操作 Sheet 页1", e.message)
    raise e

# -*- 保存/关闭 Excel 文档
try:
    visual_block.Visual_Block_Info("保存/关闭 Excel 文档", 8, 0, "正在执行")

    import rpa.excel

    rpa_39f0f1_excel.close(save=True)

except Exception as e:
    visual_block.Visual_Block_Info("保存/关闭 Excel 文档", 8, 2, e)

    log.error("[%s] %s", "保存/关闭 Excel 文档", e.message)
    raise e

# -*- 打开 Excel 文档2
try:
    visual_block.Visual_Block_Info("打开 Excel 文档2", 9, 0, "正在执行")

    import rpa.excel

    rpa_4ba91a = rpa.excel.open(r"C:\\Users\\Administrator\\Desktop\\DOC\\20191203\\流水二.xlsx", visible=True,
                                readonly=False, pass_word="", wps=False)

except Exception as e:
    visual_block.Visual_Block_Info("打开 Excel 文档2", 9, 2, e)

    log.error("[%s] %s", "打开 Excel 文档2", e.message)
    raise e

# -*- 操作单元格2
try:
    visual_block.Visual_Block_Info("操作单元格2", 10, 0, "正在执行")

    import rpa.excel

    rpa_4ba91a.get_sheet("").copy()

except Exception as e:
    visual_block.Visual_Block_Info("操作单元格2", 10, 2, e)

    log.error("[%s] %s", "操作单元格2", e.message)
    raise e

# -*- 操作 Sheet 页2
try:
    visual_block.Visual_Block_Info("操作 Sheet 页2", 11, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel.add_sheet(sheet_name="流水2", location="流水1", relative="after")

except Exception as e:
    visual_block.Visual_Block_Info("操作 Sheet 页2", 11, 2, e)

    log.error("[%s] %s", "操作 Sheet 页2", e.message)
    raise e

# -*- 操作单元格21
try:
    visual_block.Visual_Block_Info("操作单元格21", 12, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel.get_sheet("流水2").paste("A", "1", type="全部")

except Exception as e:
    visual_block.Visual_Block_Info("操作单元格21", 12, 2, e)

    log.error("[%s] %s", "操作单元格21", e.message)
    raise e

# -*- 保存/关闭 Excel 文档1
try:
    visual_block.Visual_Block_Info("保存/关闭 Excel 文档1", 13, 0, "正在执行")

    import rpa.excel

    rpa_4ba91a.close(save=True)

except Exception as e:
    visual_block.Visual_Block_Info("保存/关闭 Excel 文档1", 13, 2, e)

    log.error("[%s] %s", "保存/关闭 Excel 文档1", e.message)
    raise e

# -*- 打开 Excel 文档3
try:
    visual_block.Visual_Block_Info("打开 Excel 文档3", 14, 0, "正在执行")

    import rpa.excel

    rpa_763550 = rpa.excel.open(r"C:\\Users\\Administrator\\Desktop\\DOC\\20191203\\流水三.xlsx", visible=True,
                                readonly=False, pass_word="", wps=False)

except Exception as e:
    visual_block.Visual_Block_Info("打开 Excel 文档3", 14, 2, e)

    log.error("[%s] %s", "打开 Excel 文档3", e.message)
    raise e

# -*- 操作单元格3
try:
    visual_block.Visual_Block_Info("操作单元格3", 15, 0, "正在执行")

    import rpa.excel

    rpa_763550.get_sheet("").copy()

except Exception as e:
    visual_block.Visual_Block_Info("操作单元格3", 15, 2, e)

    log.error("[%s] %s", "操作单元格3", e.message)
    raise e

# -*- 操作 Sheet 页3
try:
    visual_block.Visual_Block_Info("操作 Sheet 页3", 16, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel.add_sheet(sheet_name="流水3", location="流水2", relative="after")

except Exception as e:
    visual_block.Visual_Block_Info("操作 Sheet 页3", 16, 2, e)

    log.error("[%s] %s", "操作 Sheet 页3", e.message)
    raise e

# -*- 保存/关闭 Excel 文档2
try:
    visual_block.Visual_Block_Info("保存/关闭 Excel 文档2", 17, 0, "正在执行")

    import rpa.excel

    rpa_763550.close(save=True)

except Exception as e:
    visual_block.Visual_Block_Info("保存/关闭 Excel 文档2", 17, 2, e)

    log.error("[%s] %s", "保存/关闭 Excel 文档2", e.message)
    raise e

# -*- 操作 Sheet 页4
try:
    visual_block.Visual_Block_Info("操作 Sheet 页4", 18, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel.add_sheet(sheet_name="图片", location="流水3", relative="after")

except Exception as e:
    visual_block.Visual_Block_Info("操作 Sheet 页4", 18, 2, e)

    log.error("[%s] %s", "操作 Sheet 页4", e.message)
    raise e

# -*- 操作单元格31
try:
    visual_block.Visual_Block_Info("操作单元格31", 19, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel.get_sheet("流水3").paste("A", "1", type="全部")

except Exception as e:
    visual_block.Visual_Block_Info("操作单元格31", 19, 2, e)

    log.error("[%s] %s", "操作单元格31", e.message)
    raise e

# -*- 获取文件/文件夹列表
try:
    visual_block.Visual_Block_Info("获取文件/文件夹列表", 20, 0, "正在执行")

    import rpa.file_folder

    rpa_47f96f_array_string = rpa.file_folder.list_dir(path=r"C:\\Users\\Administrator\\Desktop\\DOC\\20191203",
                                                       dirtype="file", withpath=False, isext=True)

except Exception as e:
    visual_block.Visual_Block_Info("获取文件/文件夹列表", 20, 2, e)

    log.error("[%s] %s", "获取文件/文件夹列表", e.message)
    raise e

# -*- 创建a
try:
    visual_block.Visual_Block_Info("创建a", 21, 0, "正在执行")

    a = 0

except Exception as e:
    visual_block.Visual_Block_Info("创建a", 21, 2, e)

    log.error("[%s] %s", "创建a", e.message)
    raise e

# -*- 创建b
try:
    visual_block.Visual_Block_Info("创建b", 22, 0, "正在执行")

    b = 0

except Exception as e:
    visual_block.Visual_Block_Info("创建b", 22, 2, e)

    log.error("[%s] %s", "创建b", e.message)
    raise e

# -*- 循环执行
try:
    visual_block.Visual_Block_Info("循环执行", 23, 0, "正在执行")

    for rpa_4284b5_any in rpa_47f96f_array_string:

        # -*- 创建变量
        try:
            i = rpa_4284b5_any

        except Exception as e:
            log.error("[%s] %s", "创建变量", e.message)
            raise e

        # -*- 条件判断
        try:

            if i.endswith(".jpeg"):

                # -*- 数学运算
                try:
                    rpa_db0f53_number = a + 1

                except Exception as e:
                    log.error("[%s] %s", "数学运算", e.message)
                    raise e

                # -*- 赋值操作
                try:
                    a = rpa_db0f53_number

                except Exception as e:
                    log.error("[%s] %s", "赋值操作", e.message)
                    raise e
            else:
                pass

        except Exception as e:
            log.error("[%s] %s", "条件判断", e.message)
            raise e

        # -*- 条件判断1
        try:

            if i.endswith(".png"):

                # -*- 数学运算1
                try:
                    rpa_e56f61_number = b + 1

                except Exception as e:
                    log.error("[%s] %s", "数学运算1", e.message)
                    raise e

                # -*- 赋值操作1
                try:
                    b = rpa_e56f61_number

                except Exception as e:
                    log.error("[%s] %s", "赋值操作1", e.message)
                    raise e
            else:
                pass

        except Exception as e:
            log.error("[%s] %s", "条件判断1", e.message)
            raise e
except Exception as e:
    visual_block.Visual_Block_Info("循环执行", 23, 2, e)

    log.error("[%s] %s", "循环执行", e.message)
    raise e

# -*- 写入/设置 Excel 内容
try:
    visual_block.Visual_Block_Info("写入/设置 Excel 内容", 24, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel.get_sheet("图片").write("A" + str("1"), 'jpeg数量')

except Exception as e:
    visual_block.Visual_Block_Info("写入/设置 Excel 内容", 24, 2, e)

    log.error("[%s] %s", "写入/设置 Excel 内容", e.message)
    raise e

# -*- 写入/设置 Excel 内容1
try:
    visual_block.Visual_Block_Info("写入/设置 Excel 内容1", 25, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel.get_sheet("图片").write("B" + str("1"), 'png数量')

except Exception as e:
    visual_block.Visual_Block_Info("写入/设置 Excel 内容1", 25, 2, e)

    log.error("[%s] %s", "写入/设置 Excel 内容1", e.message)
    raise e

# -*- 写入/设置 Excel 内容12
try:
    visual_block.Visual_Block_Info("写入/设置 Excel 内容12", 26, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel.get_sheet("图片").write("A" + str("2"), a)

except Exception as e:
    visual_block.Visual_Block_Info("写入/设置 Excel 内容12", 26, 2, e)

    log.error("[%s] %s", "写入/设置 Excel 内容12", e.message)
    raise e

# -*- 写入/设置 Excel 内容11
try:
    visual_block.Visual_Block_Info("写入/设置 Excel 内容11", 27, 0, "正在执行")

    import rpa.excel

    rpa_eae6da_excel.get_sheet("图片").write("B" + str("2"), b)

except Exception as e:
    visual_block.Visual_Block_Info("写入/设置 Excel 内容11", 27, 2, e)

    log.error("[%s] %s", "写入/设置 Excel 内容11", e.message)
    raise e

# -*- 保存/关闭 Excel 文档3
try:
    visual_block.Visual_Block_Info("保存/关闭 Excel 文档3", 28, 0, "正在执行")

    import rpa.excel
    import os

    rpa_eae6da_excel.save(file=os.path.join("C:\\Users\\Administrator\\Desktop\\DOC", "合并.xlsx"), pass_word="")

except Exception as e:
    visual_block.Visual_Block_Info("保存/关闭 Excel 文档3", 28, 2, e)

    log.error("[%s] %s", "保存/关闭 Excel 文档3", e.message)
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", e.message)

    # print(zip_file.encode('utf-8').decode('utf-8'))
    # try:
    #     zip_file = zip_file.encode('cp437').decode('gbk')
    # except:
    #     zip_file = zip_file.encode('utf-8').decode('utf-8')
    # print(zip_file)