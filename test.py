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
visual_block.Visual_Block_Total_Block(50)

# -*- 参数面板
try:

    PANEL_VARS = {
        "tb_qs": [],
        "ts_one": [],
        "ts_two": [],
        "p_true": [],
        "p_false": [],
        "mx_true": [],
        "mx_false": [],
        "count": 0,
        "cny_sum": 0.0,
        "sg_true": [],
        "tb_dh": [],
        "sj_bf": [],
    }

except Exception as e:
    log.error("[%s] %s", "参数面板", str(e))

# -*- 传入的JSON
try:

    update_panel(sys.argv, PANEL_VARS)

except Exception as e:
    log.error("[%s] %s", "传入的JSON", str(e))

# -*- 变量注释说明
try:
    visual_block.Visual_Block_Info("变量注释说明", 1, 0, "正在执行")

    sys.coinit_flags = 0
    # "tb_qs" : []     # 投保去重
    # "ts_one" : []    # 汇总表透视表1
    # "ts_two" : []    # 收付费明细表透视表2
    # "p_true" : []    # 匹配表得到数据一致列表
    # a_dic = {}       # 中间对汇总表去重以及金额相加所使用的字典
    # p_one = []       # 匹配表中透视表1的ABC三列的二维列表
    # b_dic = {}       # 中间对收付费明细表去重以及金额相加所使用的字典
    # p_two = []       # 匹配表中透视表2的F列的列表
    # "mx_true" : []   # 与收付费明细表的数据一致列表
    # "mx_false" : []  # 与收付费明细表数据不一致列表
    # "count" : 0      # 导入笔数
    # "cny_sum" : 0.0  # 导入金额
    # "sg_true" : []   # 手工数据匹配数据一致列表
    # "tb_dh" : []     # 得到助贷手工拆分表投保单号
    # "sj_bf" : []     # 得到助贷手工拆分表期数+保费


except Exception as e:
    exception_capture(__errorCapturePath, "变量注释说明", __taskId)
    visual_block.Visual_Block_Info("变量注释说明", 1, 2, str(e))

    log.error("[%s] %s", "变量注释说明", str(e))
    raise e

# -*- 打开保费匹配文档
try:
    visual_block.Visual_Block_Info("打开保费匹配文档", 2, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel = rpa.excel.open(r"C:\\Users\\datagrand\\Desktop\\poc\\保费匹配表.xlsx", visible=True, readonly=False,
                                      pass_word="", wps=False)

except Exception as e:
    exception_capture(__errorCapturePath, "打开保费匹配文档", __taskId)
    visual_block.Visual_Block_Info("打开保费匹配文档", 2, 2, str(e))

    log.error("[%s] %s", "打开保费匹配文档", str(e))
    raise e

# -*- 复制汇总表
try:
    visual_block.Visual_Block_Info("复制汇总表", 3, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("汇总表").copy()

except Exception as e:
    exception_capture(__errorCapturePath, "复制汇总表", __taskId)
    visual_block.Visual_Block_Info("复制汇总表", 3, 2, str(e))

    log.error("[%s] %s", "复制汇总表", str(e))
    raise e

# -*- 粘贴到手工数据匹配
try:
    visual_block.Visual_Block_Info("粘贴到手工数据匹配", 4, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("手工数据匹配").paste("D", "1", type="全部")

except Exception as e:
    exception_capture(__errorCapturePath, "粘贴到手工数据匹配", __taskId)
    visual_block.Visual_Block_Info("粘贴到手工数据匹配", 4, 2, str(e))

    log.error("[%s] %s", "粘贴到手工数据匹配", str(e))
    raise e

# -*- 删除公司列
try:
    visual_block.Visual_Block_Info("删除公司列", 5, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("手工数据匹配").delete("U", deleteDirection="up")

except Exception as e:
    exception_capture(__errorCapturePath, "删除公司列", __taskId)
    visual_block.Visual_Block_Info("删除公司列", 5, 2, str(e))

    log.error("[%s] %s", "删除公司列", str(e))
    raise e

# -*- 读汇总表保费投保+期数
try:
    visual_block.Visual_Block_Info("读汇总表保费投保+期数", 6, 0, "正在执行")

    import rpa.excel

    rpa_3cca73_array_any = rpa_318e1e_excel.get_sheet("汇总表").read("Q", skip=0, max=1000)

except Exception as e:
    exception_capture(__errorCapturePath, "读汇总表保费投保+期数", __taskId)
    visual_block.Visual_Block_Info("读汇总表保费投保+期数", 6, 2, str(e))

    log.error("[%s] %s", "读汇总表保费投保+期数", str(e))
    raise e

# -*- 删除投保期数第1行表头
try:
    visual_block.Visual_Block_Info("删除投保期数第1行表头", 7, 0, "正在执行")

    del rpa_3cca73_array_any[0]

except Exception as e:
    exception_capture(__errorCapturePath, "删除投保期数第1行表头", __taskId)
    visual_block.Visual_Block_Info("删除投保期数第1行表头", 7, 2, str(e))

    log.error("[%s] %s", "删除投保期数第1行表头", str(e))
    raise e

# -*- 读取汇总表实缴保费
try:
    visual_block.Visual_Block_Info("读取汇总表实缴保费", 8, 0, "正在执行")

    import rpa.excel

    rpa_966481_array_any = rpa_318e1e_excel.get_sheet("汇总表").read("J", skip=0, max=1000)

except Exception as e:
    exception_capture(__errorCapturePath, "读取汇总表实缴保费", __taskId)
    visual_block.Visual_Block_Info("读取汇总表实缴保费", 8, 2, str(e))

    log.error("[%s] %s", "读取汇总表实缴保费", str(e))
    raise e

# -*- 删除实缴保费第1行表头
try:
    visual_block.Visual_Block_Info("删除实缴保费第1行表头", 9, 0, "正在执行")

    del rpa_966481_array_any[0]

except Exception as e:
    exception_capture(__errorCapturePath, "删除实缴保费第1行表头", __taskId)
    visual_block.Visual_Block_Info("删除实缴保费第1行表头", 9, 2, str(e))

    log.error("[%s] %s", "删除实缴保费第1行表头", str(e))
    raise e

# -*- 得到汇总表透视表1
try:
    visual_block.Visual_Block_Info("得到汇总表透视表1", 10, 0, "正在执行")

    a_dic = {}  # 中间对汇总表去重以及金额相加所使用的字典
    p_one = []  # 匹配表中透视表1的ABC三列的二维列表
    for i, v in enumerate(rpa_3cca73_array_any):
        if v is None:
            break
        else:
            if v in a_dic.keys():
                # a_dic存储的是汇总表的投保单+期数，实缴保费
                # a_dic = {'投保单+期数':'实缴保费'}
                a_dic[v] = round((a_dic[v] + float(rpa_966481_array_any[i])), 2)
            else:
                if rpa_966481_array_any[i] is None:
                    break
                a_dic[v] = float(rpa_966481_array_any[i])
    for i in a_dic.keys():
        # ts_one 存储汇总表的透视表1
        # ts_one = [['投保单+期数','实缴保费']]
        PANEL_VARS['ts_one'].append([i, a_dic[i]])
        # p_one 存储匹配表A,B,C三列内容
        # p_one = [['投保单+期数','实缴保费','C列公式列']]
        p_one.append([i, a_dic[i], str(i) + str(a_dic[i])])

except Exception as e:
    exception_capture(__errorCapturePath, "得到汇总表透视表1", __taskId)
    visual_block.Visual_Block_Info("得到汇总表透视表1", 10, 2, str(e))

    log.error("[%s] %s", "得到汇总表透视表1", str(e))
    raise e

# -*- 打开bbr缴费文档
try:
    visual_block.Visual_Block_Info("打开bbr缴费文档", 11, 0, "正在执行")

    import rpa.excel

    rpa_e9af33_excel = rpa.excel.open(r"C:\\Users\\datagrand\\Desktop\\poc\\bbr缴费通知单提数.xlsx", visible=True,
                                      readonly=False, pass_word="", wps=False)

except Exception as e:
    exception_capture(__errorCapturePath, "打开bbr缴费文档", __taskId)
    visual_block.Visual_Block_Info("打开bbr缴费文档", 11, 2, str(e))

    log.error("[%s] %s", "打开bbr缴费文档", str(e))
    raise e

# -*- 复制bbr全部内容
try:
    visual_block.Visual_Block_Info("复制bbr全部内容", 12, 0, "正在执行")

    import rpa.excel

    rpa_9a4196_array_any = rpa_e9af33_excel.get_sheet("").read()

except Exception as e:
    exception_capture(__errorCapturePath, "复制bbr全部内容", __taskId)
    visual_block.Visual_Block_Info("复制bbr全部内容", 12, 2, str(e))

    log.error("[%s] %s", "复制bbr全部内容", str(e))
    raise e

# -*- 删除bbr第1行表头
try:
    visual_block.Visual_Block_Info("删除bbr第1行表头", 13, 0, "正在执行")

    del rpa_9a4196_array_any[0]

except Exception as e:
    exception_capture(__errorCapturePath, "删除bbr第1行表头", __taskId)
    visual_block.Visual_Block_Info("删除bbr第1行表头", 13, 2, str(e))

    log.error("[%s] %s", "删除bbr第1行表头", str(e))
    raise e

# -*- 删除bbr第2行表头
try:
    visual_block.Visual_Block_Info("删除bbr第2行表头", 14, 0, "正在执行")

    del rpa_9a4196_array_any[0]

except Exception as e:
    exception_capture(__errorCapturePath, "删除bbr第2行表头", __taskId)
    visual_block.Visual_Block_Info("删除bbr第2行表头", 14, 2, str(e))

    log.error("[%s] %s", "删除bbr第2行表头", str(e))
    raise e

# -*- 写入收付费明细
try:
    visual_block.Visual_Block_Info("写入收付费明细", 15, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("收付费明细表").write("A" + str("3"), rpa_9a4196_array_any)

except Exception as e:
    exception_capture(__errorCapturePath, "写入收付费明细", __taskId)
    visual_block.Visual_Block_Info("写入收付费明细", 15, 2, str(e))

    log.error("[%s] %s", "写入收付费明细", str(e))
    raise e

# -*- 格式收付费明细表G列
try:
    visual_block.Visual_Block_Info("格式收付费明细表G列", 16, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("收付费明细表").set_style("G", style="number_format", value="数值")

except Exception as e:
    exception_capture(__errorCapturePath, "格式收付费明细表G列", __taskId)
    visual_block.Visual_Block_Info("格式收付费明细表G列", 16, 2, str(e))

    log.error("[%s] %s", "格式收付费明细表G列", str(e))
    raise e

# -*- 写入与收付费匹配
try:
    visual_block.Visual_Block_Info("写入与收付费匹配", 17, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("与收付费明细表匹配").write("D" + str("2"), rpa_9a4196_array_any)

except Exception as e:
    exception_capture(__errorCapturePath, "写入与收付费匹配", __taskId)
    visual_block.Visual_Block_Info("写入与收付费匹配", 17, 2, str(e))

    log.error("[%s] %s", "写入与收付费匹配", str(e))
    raise e

# -*- 格式与收付费明细表J列
try:
    visual_block.Visual_Block_Info("格式与收付费明细表J列", 18, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("与收付费明细表匹配").set_style("J", style="number_format", value="数值")

except Exception as e:
    exception_capture(__errorCapturePath, "格式与收付费明细表J列", __taskId)
    visual_block.Visual_Block_Info("格式与收付费明细表J列", 18, 2, str(e))

    log.error("[%s] %s", "格式与收付费明细表J列", str(e))
    raise e

# -*- 收付费明细表投保单序列号
try:
    visual_block.Visual_Block_Info("收付费明细表投保单序列号", 19, 0, "正在执行")

    import rpa.excel

    rpa_eef098_array_any = rpa_e9af33_excel.get_sheet("").read("K", skip=0, max=1000)

except Exception as e:
    exception_capture(__errorCapturePath, "收付费明细表投保单序列号", __taskId)
    visual_block.Visual_Block_Info("收付费明细表投保单序列号", 19, 2, str(e))

    log.error("[%s] %s", "收付费明细表投保单序列号", str(e))
    raise e

# -*- 删除投保单第1行表头
try:
    visual_block.Visual_Block_Info("删除投保单第1行表头", 20, 0, "正在执行")

    del rpa_eef098_array_any[0]

except Exception as e:
    exception_capture(__errorCapturePath, "删除投保单第1行表头", __taskId)
    visual_block.Visual_Block_Info("删除投保单第1行表头", 20, 2, str(e))

    log.error("[%s] %s", "删除投保单第1行表头", str(e))
    raise e

# -*- 删除投保单第2行表头
try:
    visual_block.Visual_Block_Info("删除投保单第2行表头", 21, 0, "正在执行")

    del rpa_eef098_array_any[0]

except Exception as e:
    exception_capture(__errorCapturePath, "删除投保单第2行表头", __taskId)
    visual_block.Visual_Block_Info("删除投保单第2行表头", 21, 2, str(e))

    log.error("[%s] %s", "删除投保单第2行表头", str(e))
    raise e

# -*- 收付费明细表金额列
try:
    visual_block.Visual_Block_Info("收付费明细表金额列", 22, 0, "正在执行")

    import rpa.excel

    rpa_004be8_array_any = rpa_e9af33_excel.get_sheet("").read("I", skip=0, max=1000)

except Exception as e:
    exception_capture(__errorCapturePath, "收付费明细表金额列", __taskId)
    visual_block.Visual_Block_Info("收付费明细表金额列", 22, 2, str(e))

    log.error("[%s] %s", "收付费明细表金额列", str(e))
    raise e

# -*- 删除金额第1行表头
try:
    visual_block.Visual_Block_Info("删除金额第1行表头", 23, 0, "正在执行")

    del rpa_004be8_array_any[0]

except Exception as e:
    exception_capture(__errorCapturePath, "删除金额第1行表头", __taskId)
    visual_block.Visual_Block_Info("删除金额第1行表头", 23, 2, str(e))

    log.error("[%s] %s", "删除金额第1行表头", str(e))
    raise e

# -*- 删除金额第2行表头
try:
    visual_block.Visual_Block_Info("删除金额第2行表头", 24, 0, "正在执行")

    del rpa_004be8_array_any[0]

except Exception as e:
    exception_capture(__errorCapturePath, "删除金额第2行表头", __taskId)
    visual_block.Visual_Block_Info("删除金额第2行表头", 24, 2, str(e))

    log.error("[%s] %s", "删除金额第2行表头", str(e))
    raise e

# -*- 得到收付费透视表2
try:
    visual_block.Visual_Block_Info("得到收付费透视表2", 25, 0, "正在执行")

    b_dic = {}  # 中间对收付费明细表去重以及金额相加所使用的字典
    p_two = []  # 匹配表中透视表2的F列的列表
    for i, v in enumerate(rpa_eef098_array_any):
        if v is None:
            break
        else:
            if v in b_dic.keys():
                # b_dic = {'投保单号序列号':'金额'}
                b_dic[v] = round((b_dic[v] + float(rpa_004be8_array_any[i])), 2)
            else:
                if rpa_004be8_array_any[i] is None:
                    break
                b_dic[v] = float(rpa_004be8_array_any[i])
    for i in b_dic.keys():
        # ts_two是收付费明细表的透视表
        # ts_two = [['投保单号序列号','金额']]
        PANEL_VARS['ts_two'].append([i, b_dic[i]])
        # p_two 匹配表中透视表2的F列的列表
        p_two.append(str(i) + str(b_dic[i]))

except Exception as e:
    exception_capture(__errorCapturePath, "得到收付费透视表2", __taskId)
    visual_block.Visual_Block_Info("得到收付费透视表2", 25, 2, str(e))

    log.error("[%s] %s", "得到收付费透视表2", str(e))
    raise e

# -*- 关闭bbr文档
try:
    visual_block.Visual_Block_Info("关闭bbr文档", 26, 0, "正在执行")

    import rpa.excel

    rpa_e9af33_excel.close(save=True)

except Exception as e:
    exception_capture(__errorCapturePath, "关闭bbr文档", __taskId)
    visual_block.Visual_Block_Info("关闭bbr文档", 26, 2, str(e))

    log.error("[%s] %s", "关闭bbr文档", str(e))
    raise e

# -*- 写入匹配表透视表1
try:
    visual_block.Visual_Block_Info("写入匹配表透视表1", 27, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("匹配表").write("A" + str("2"), PANEL_VARS.get("ts_one"))

except Exception as e:
    exception_capture(__errorCapturePath, "写入匹配表透视表1", __taskId)
    visual_block.Visual_Block_Info("写入匹配表透视表1", 27, 2, str(e))

    log.error("[%s] %s", "写入匹配表透视表1", str(e))
    raise e

# -*- 写入匹配表透视表2
try:
    visual_block.Visual_Block_Info("写入匹配表透视表2", 28, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("匹配表").write("G" + str("2"), PANEL_VARS.get("ts_two"))

except Exception as e:
    exception_capture(__errorCapturePath, "写入匹配表透视表2", __taskId)
    visual_block.Visual_Block_Info("写入匹配表透视表2", 28, 2, str(e))

    log.error("[%s] %s", "写入匹配表透视表2", str(e))
    raise e

# -*- 得到匹配表中数据
try:
    visual_block.Visual_Block_Info("得到匹配表中数据", 29, 0, "正在执行")

    a_list = []  # 匹配表数据一致数组 [投保单号|序列号]
    b_list = []  # 匹配表数据不一致数组 [投保单号|序列号]
    # 对透视表1进行遍历拿到公式列C,并在透视表2的公式列F查找，如果找到代表数据一致
    for i in p_one:
        if i[2] in p_two:
            # p_true存储数据一致的匹配表AB列
            PANEL_VARS['p_true'].append([i[0], i[1]])
            # a_list只存储数据一致的投保单号|序列号
            a_list.append(i[0])
        else:
            b_list.append(i[0])

except Exception as e:
    exception_capture(__errorCapturePath, "得到匹配表中数据", __taskId)
    visual_block.Visual_Block_Info("得到匹配表中数据", 29, 2, str(e))

    log.error("[%s] %s", "得到匹配表中数据", str(e))
    raise e

# -*- 写入明细表匹配左
try:
    visual_block.Visual_Block_Info("写入明细表匹配左", 30, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("与收付费明细表匹配").write("A" + str("2"), PANEL_VARS.get("p_true"))

except Exception as e:
    exception_capture(__errorCapturePath, "写入明细表匹配左", __taskId)
    visual_block.Visual_Block_Info("写入明细表匹配左", 30, 2, str(e))

    log.error("[%s] %s", "写入明细表匹配左", str(e))
    raise e

# -*- 得到明细表匹配数据
try:
    visual_block.Visual_Block_Info("得到明细表匹配数据", 31, 0, "正在执行")

    # 对与收付费明细表匹配的D-N列即收付费明细表进行遍历，拿收付费投保单号|序列号在a_list列表中查找
    # 得到与收付费明细表匹配的数据一致的收付费明细列表mx_true
    for v in rpa_9a4196_array_any:
        if v[10] in a_list:
            # cny_sum 累加数据一致的金额
            PANEL_VARS['cny_sum'] += v[8]
            # count 累加数据一致的笔数
            PANEL_VARS['count'] += 1
            # mx_true 保存数据一致的收付费明细列表
            PANEL_VARS['mx_true'].append(v)
        else:
            # mx_false 保存数据不一致的收付费明细列表
            PANEL_VARS['mx_false'].append(v)
    # 打印导入笔数，导入金额
    print([PANEL_VARS['count'], round(PANEL_VARS['cny_sum'], 2)])

except Exception as e:
    exception_capture(__errorCapturePath, "得到明细表匹配数据", __taskId)
    visual_block.Visual_Block_Info("得到明细表匹配数据", 31, 2, str(e))

    log.error("[%s] %s", "得到明细表匹配数据", str(e))
    raise e

# -*- 写入省公司导入清单
try:
    visual_block.Visual_Block_Info("写入省公司导入清单", 32, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("省公司导入清单").write("A" + str("2"), PANEL_VARS.get("mx_true"))

except Exception as e:
    exception_capture(__errorCapturePath, "写入省公司导入清单", __taskId)
    visual_block.Visual_Block_Info("写入省公司导入清单", 32, 2, str(e))

    log.error("[%s] %s", "写入省公司导入清单", str(e))
    raise e

# -*- 写入手工数据匹配
try:
    visual_block.Visual_Block_Info("写入手工数据匹配", 33, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("手工数据匹配").write("A" + str("2"), PANEL_VARS.get("p_false"))

except Exception as e:
    exception_capture(__errorCapturePath, "写入手工数据匹配", __taskId)
    visual_block.Visual_Block_Info("写入手工数据匹配", 33, 2, str(e))

    log.error("[%s] %s", "写入手工数据匹配", str(e))
    raise e

# -*- 格式省公司导入G列
try:
    visual_block.Visual_Block_Info("格式省公司导入G列", 34, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.get_sheet("省公司导入清单").set_style("G", style="number_format", value="数值")

except Exception as e:
    exception_capture(__errorCapturePath, "格式省公司导入G列", __taskId)
    visual_block.Visual_Block_Info("格式省公司导入G列", 34, 2, str(e))

    log.error("[%s] %s", "格式省公司导入G列", str(e))
    raise e

# -*- 关闭保费匹配文档
try:
    visual_block.Visual_Block_Info("关闭保费匹配文档", 35, 0, "正在执行")

    import rpa.excel

    rpa_318e1e_excel.close(save=True)

except Exception as e:
    exception_capture(__errorCapturePath, "关闭保费匹配文档", __taskId)
    visual_block.Visual_Block_Info("关闭保费匹配文档", 35, 2, str(e))

    log.error("[%s] %s", "关闭保费匹配文档", str(e))
    raise e

# -*- 打开保费匹配模板
try:
    visual_block.Visual_Block_Info("打开保费匹配模板", 36, 0, "正在执行")

    import rpa.excel

    rpa_4fed84_excel = rpa.excel.open(r"C:\\Users\\datagrand\\Desktop\\poc\\保费匹配模板.xlsx", visible=True, readonly=False,
                                      pass_word="", wps=False)

except Exception as e:
    exception_capture(__errorCapturePath, "打开保费匹配模板", __taskId)
    visual_block.Visual_Block_Info("打开保费匹配模板", 36, 2, str(e))

    log.error("[%s] %s", "打开保费匹配模板", str(e))
    raise e

# -*- 打开新保费匹配表
try:
    visual_block.Visual_Block_Info("打开新保费匹配表", 37, 0, "正在执行")

    import rpa.excel

    rpa_ef1652_excel = rpa.excel.open(r"C:\\Users\\datagrand\\Desktop\\poc\\保费匹配表.xlsx", visible=True, readonly=False,
                                      pass_word="", wps=False)

except Exception as e:
    exception_capture(__errorCapturePath, "打开新保费匹配表", __taskId)
    visual_block.Visual_Block_Info("打开新保费匹配表", 37, 2, str(e))

    log.error("[%s] %s", "打开新保费匹配表", str(e))
    raise e

# -*- 粘贴保费匹配模板
try:
    visual_block.Visual_Block_Info("粘贴保费匹配模板", 38, 0, "正在执行")

    import rpa.excel

    rpa_4fed84_excel.get_sheet("保费匹配模板").write("A" + str("2"), PANEL_VARS.get("mx_true"))

except Exception as e:
    exception_capture(__errorCapturePath, "粘贴保费匹配模板", __taskId)
    visual_block.Visual_Block_Info("粘贴保费匹配模板", 38, 2, str(e))

    log.error("[%s] %s", "粘贴保费匹配模板", str(e))
    raise e

# -*- 格式保费匹配模板G列
try:
    visual_block.Visual_Block_Info("格式保费匹配模板G列", 39, 0, "正在执行")

    import rpa.excel

    rpa_4fed84_excel.get_sheet("保费匹配模板").set_style("G", style="number_format", value="数值")

except Exception as e:
    exception_capture(__errorCapturePath, "格式保费匹配模板G列", __taskId)
    visual_block.Visual_Block_Info("格式保费匹配模板G列", 39, 2, str(e))

    log.error("[%s] %s", "格式保费匹配模板G列", str(e))
    raise e

# -*- 关闭保费匹配模板
try:
    visual_block.Visual_Block_Info("关闭保费匹配模板", 40, 0, "正在执行")

    import rpa.excel

    rpa_4fed84_excel.close(save=True)

except Exception as e:
    exception_capture(__errorCapturePath, "关闭保费匹配模板", __taskId)
    visual_block.Visual_Block_Info("关闭保费匹配模板", 40, 2, str(e))

    log.error("[%s] %s", "关闭保费匹配模板", str(e))
    raise e

# -*- 读取汇总表内容
try:
    visual_block.Visual_Block_Info("读取汇总表内容", 41, 0, "正在执行")

    import rpa.excel

    rpa_7ff618_array_any = rpa_ef1652_excel.get_sheet("汇总表").read()

except Exception as e:
    exception_capture(__errorCapturePath, "读取汇总表内容", __taskId)
    visual_block.Visual_Block_Info("读取汇总表内容", 41, 2, str(e))

    log.error("[%s] %s", "读取汇总表内容", str(e))
    raise e

# -*- 删除汇总表第1行表头
try:
    visual_block.Visual_Block_Info("删除汇总表第1行表头", 42, 0, "正在执行")

    del rpa_7ff618_array_any[0]

except Exception as e:
    exception_capture(__errorCapturePath, "删除汇总表第1行表头", __taskId)
    visual_block.Visual_Block_Info("删除汇总表第1行表头", 42, 2, str(e))

    log.error("[%s] %s", "删除汇总表第1行表头", str(e))
    raise e

# -*- 得到手工数据匹配数据
try:
    visual_block.Visual_Block_Info("得到手工数据匹配数据", 43, 0, "正在执行")

    for i in rpa_7ff618_array_any:
        if i[-2] in b_list:
            i[14] += '\t'
            i[15] += '\t'
            PANEL_VARS['sg_true'].append(i[:16:])
            PANEL_VARS['tb_dh'].append([i[3]])
            PANEL_VARS['sj_bf'].append([i[8], i[9]])

except Exception as e:
    exception_capture(__errorCapturePath, "得到手工数据匹配数据", __taskId)
    visual_block.Visual_Block_Info("得到手工数据匹配数据", 43, 2, str(e))

    log.error("[%s] %s", "得到手工数据匹配数据", str(e))
    raise e

# -*- 写入省公司手工处理
try:
    visual_block.Visual_Block_Info("写入省公司手工处理", 44, 0, "正在执行")

    import rpa.excel

    rpa_ef1652_excel.get_sheet("省公司手工处理").write("A" + str("2"), PANEL_VARS.get("sg_true"))

except Exception as e:
    exception_capture(__errorCapturePath, "写入省公司手工处理", __taskId)
    visual_block.Visual_Block_Info("写入省公司手工处理", 44, 2, str(e))

    log.error("[%s] %s", "写入省公司手工处理", str(e))
    raise e

# -*- 关闭新保费文档
try:
    visual_block.Visual_Block_Info("关闭新保费文档", 45, 0, "正在执行")

    import rpa.excel

    rpa_ef1652_excel.close(save=True)

except Exception as e:
    exception_capture(__errorCapturePath, "关闭新保费文档", __taskId)
    visual_block.Visual_Block_Info("关闭新保费文档", 45, 2, str(e))

    log.error("[%s] %s", "关闭新保费文档", str(e))
    raise e

# -*- 打开助贷手工拆分表
try:
    visual_block.Visual_Block_Info("打开助贷手工拆分表", 46, 0, "正在执行")

    import rpa.excel

    rpa_5656c7_excel = rpa.excel.open(r"C:\\Users\\datagrand\\Desktop\\poc\\助贷手工拆分表.xlsx", visible=True, readonly=False,
                                      pass_word="", wps=False)

except Exception as e:
    exception_capture(__errorCapturePath, "打开助贷手工拆分表", __taskId)
    visual_block.Visual_Block_Info("打开助贷手工拆分表", 46, 2, str(e))

    log.error("[%s] %s", "打开助贷手工拆分表", str(e))
    raise e

# -*- 写入拆分表的保费表
try:
    visual_block.Visual_Block_Info("写入拆分表的保费表", 47, 0, "正在执行")

    import rpa.excel

    rpa_5656c7_excel.get_sheet("保费").write("B" + str("2"), PANEL_VARS.get("sg_true"))

except Exception as e:
    exception_capture(__errorCapturePath, "写入拆分表的保费表", __taskId)
    visual_block.Visual_Block_Info("写入拆分表的保费表", 47, 2, str(e))

    log.error("[%s] %s", "写入拆分表的保费表", str(e))
    raise e

# -*- 写入拆分表的投保单
try:
    visual_block.Visual_Block_Info("写入拆分表的投保单", 48, 0, "正在执行")

    import rpa.excel

    rpa_5656c7_excel.get_sheet("拆分表").write("E" + str("2"), PANEL_VARS.get("tb_dh"))

except Exception as e:
    exception_capture(__errorCapturePath, "写入拆分表的投保单", __taskId)
    visual_block.Visual_Block_Info("写入拆分表的投保单", 48, 2, str(e))

    log.error("[%s] %s", "写入拆分表的投保单", str(e))
    raise e

# -*- 写入拆分表的期数
try:
    visual_block.Visual_Block_Info("写入拆分表的期数", 49, 0, "正在执行")

    import rpa.excel

    rpa_5656c7_excel.get_sheet("拆分表").write("J" + str("2"), PANEL_VARS.get("sj_bf"))

except Exception as e:
    exception_capture(__errorCapturePath, "写入拆分表的期数", __taskId)
    visual_block.Visual_Block_Info("写入拆分表的期数", 49, 2, str(e))

    log.error("[%s] %s", "写入拆分表的期数", str(e))
    raise e

# -*- 关闭助贷手工拆分表
try:
    visual_block.Visual_Block_Info("关闭助贷手工拆分表", 50, 0, "正在执行")

    import rpa.excel

    rpa_5656c7_excel.close(save=True)

except Exception as e:
    exception_capture(__errorCapturePath, "关闭助贷手工拆分表", __taskId)
    visual_block.Visual_Block_Info("关闭助贷手工拆分表", 50, 2, str(e))

    log.error("[%s] %s", "关闭助贷手工拆分表", str(e))
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", str(e))
