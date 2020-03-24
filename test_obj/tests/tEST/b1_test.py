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
visual_block.Visual_Block_Total_Block(18)

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

# -*- yzm
try:
    visual_block.Visual_Block_Info("yzm", 1, 0, "正在执行")

    # coding=utf-8
    import os, sys
    import hashlib
    import time
    import json
    import requests
    import base64

    FATEA_PRED_URL = "http://pred.fateadm.com"


    def LOG(log):
        # 不需要测试时，注释掉日志就可以了
        print(log)
        log = None


    class TmpObj():
        def __init__(self):
            self.value = None


    class Rsp():
        def __init__(self):
            self.ret_code = -1
            self.cust_val = 0.0
            self.err_msg = "succ"
            self.pred_rsp = TmpObj()

        def ParseJsonRsp(self, rsp_data):
            if rsp_data is None:
                self.err_msg = "http request failed, get rsp Nil data"
                return
            jrsp = json.loads(rsp_data)
            self.ret_code = int(jrsp["RetCode"])
            self.err_msg = jrsp["ErrMsg"]
            self.request_id = jrsp["RequestId"]
            if self.ret_code == 0:
                rslt_data = jrsp["RspData"]
                if rslt_data is not None and rslt_data != "":
                    jrsp_ext = json.loads(rslt_data)
                    if "cust_val" in jrsp_ext:
                        data = jrsp_ext["cust_val"]
                        self.cust_val = float(data)
                    if "result" in jrsp_ext:
                        data = jrsp_ext["result"]
                        self.pred_rsp.value = data


    def CalcSign(pd_id, passwd, timestamp):
        md5 = hashlib.md5()
        md5.update((timestamp + passwd).encode())
        csign = md5.hexdigest()
        md5 = hashlib.md5()
        md5.update((pd_id + timestamp + csign).encode())
        csign = md5.hexdigest()
        return csign


    def CalcCardSign(cardid, cardkey, timestamp, passwd):
        md5 = hashlib.md5()
        md5.update(passwd + timestamp + cardid + cardkey)
        return md5.hexdigest()


    def HttpRequest(url, body_data, img_data=""):
        rsp = Rsp()
        post_data = body_data
        files = {
            'img_data': ('img_data', img_data)
        }
        header = {
            'User-Agent': 'Mozilla/5.0',
        }
        rsp_data = requests.post(url, post_data, files=files, headers=header)
        rsp.ParseJsonRsp(rsp_data.text)
        return rsp


    class FateadmApi():
        # API接口调用类
        # 参数（appID，appKey，pdID，pdKey）
        def __init__(self, app_id, app_key, pd_id, pd_key):
            self.app_id = app_id
            if app_id is None:
                self.app_id = ""
            self.app_key = app_key
            self.pd_id = pd_id
            self.pd_key = pd_key
            self.host = FATEA_PRED_URL

        def SetHost(self, url):
            self.host = url

        #
        # 查询余额
        # 参数：无
        # 返回值：
        #   rsp.ret_code：正常返回0
        #   rsp.cust_val：用户余额
        #   rsp.err_msg：异常时返回异常详情
        #
        def QueryBalc(self):
            tm = str(int(time.time()))
            sign = CalcSign(self.pd_id, self.pd_key, tm)
            param = {
                "user_id": self.pd_id,
                "timestamp": tm,
                "sign": sign
            }
            url = self.host + "/api/custval"
            rsp = HttpRequest(url, param)
            if rsp.ret_code == 0:
                LOG("query succ ret: {} cust_val: {} rsp: {} pred: {}".format(rsp.ret_code, rsp.cust_val, rsp.err_msg,
                                                                              rsp.pred_rsp.value))
            else:
                LOG("query failed ret: {} err: {}".format(rsp.ret_code, rsp.err_msg.encode('utf-8')))
            return rsp

        #
        # 查询网络延迟
        # 参数：pred_type:识别类型
        # 返回值：
        #   rsp.ret_code：正常返回0
        #   rsp.err_msg： 异常时返回异常详情
        #
        def QueryTTS(self, pred_type):
            tm = str(int(time.time()))
            sign = CalcSign(self.pd_id, self.pd_key, tm)
            param = {
                "user_id": self.pd_id,
                "timestamp": tm,
                "sign": sign,
                "predict_type": pred_type,
            }
            if self.app_id != "":
                #
                asign = CalcSign(self.app_id, self.app_key, tm)
                param["appid"] = self.app_id
                param["asign"] = asign
            url = self.host + "/api/qcrtt"
            rsp = HttpRequest(url, param)
            if rsp.ret_code == 0:
                LOG("query rtt succ ret: {} request_id: {} err: {}".format(rsp.ret_code, rsp.request_id, rsp.err_msg))
            else:
                LOG("predict failed ret: {} err: {}".format(rsp.ret_code, rsp.err_msg.encode('utf-8')))
            return rsp

        #
        # 识别验证码
        # 参数：pred_type:识别类型  img_data:图片的数据
        # 返回值：
        #   rsp.ret_code：正常返回0
        #   rsp.request_id：唯一订单号
        #   rsp.pred_rsp.value：识别结果
        #   rsp.err_msg：异常时返回异常详情
        #
        def Predict(self, pred_type, img_data, head_info=""):
            tm = str(int(time.time()))
            sign = CalcSign(self.pd_id, self.pd_key, tm)
            param = {
                "user_id": self.pd_id,
                "timestamp": tm,
                "sign": sign,
                "predict_type": pred_type,
                "up_type": "mt"
            }
            if head_info is not None or head_info != "":
                param["head_info"] = head_info
            if self.app_id != "":
                #
                asign = CalcSign(self.app_id, self.app_key, tm)
                param["appid"] = self.app_id
                param["asign"] = asign
            url = self.host + "/api/capreg"
            files = img_data
            rsp = HttpRequest(url, param, files)
            if rsp.ret_code == 0:
                LOG("predict succ ret: {} request_id: {} pred: {} err: {}".format(rsp.ret_code, rsp.request_id,
                                                                                  rsp.pred_rsp.value, rsp.err_msg))
            else:
                LOG("predict failed ret: {} err: {}".format(rsp.ret_code, rsp.err_msg))
                if rsp.ret_code == 4003:
                    # lack of money
                    LOG("cust_val <= 0 lack of money, please charge immediately")
            return rsp

        #
        # 从文件进行验证码识别
        # 参数：pred_type;识别类型  file_name:文件名
        # 返回值：
        #   rsp.ret_code：正常返回0
        #   rsp.request_id：唯一订单号
        #   rsp.pred_rsp.value：识别结果
        #   rsp.err_msg：异常时返回异常详情
        #
        def PredictFromFile(self, pred_type, file_name, head_info=""):
            with open(file_name, "rb") as f:
                data = f.read()
            return self.Predict(pred_type, data, head_info=head_info)

        #
        # 识别失败，进行退款请求
        # 参数：request_id：需要退款的订单号
        # 返回值：
        #   rsp.ret_code：正常返回0
        #   rsp.err_msg：异常时返回异常详情
        #
        # 注意:
        #    Predict识别接口，仅在ret_code == 0时才会进行扣款，才需要进行退款请求，否则无需进行退款操作
        # 注意2:
        #   退款仅在正常识别出结果后，无法通过网站验证的情况，请勿非法或者滥用，否则可能进行封号处理
        #
        def Justice(self, request_id):
            if request_id == "":
                #
                return
            tm = str(int(time.time()))
            sign = CalcSign(self.pd_id, self.pd_key, tm)
            param = {
                "user_id": self.pd_id,
                "timestamp": tm,
                "sign": sign,
                "request_id": request_id
            }
            url = self.host + "/api/capjust"
            rsp = HttpRequest(url, param)
            if rsp.ret_code == 0:
                LOG("justice succ ret: {} request_id: {} pred: {} err: {}".format(rsp.ret_code, rsp.request_id,
                                                                                  rsp.pred_rsp.value, rsp.err_msg))
            else:
                LOG("justice failed ret: {} err: {}".format(rsp.ret_code, rsp.err_msg.encode('utf-8')))
            return rsp

        #
        # 充值接口
        # 参数：cardid：充值卡号  cardkey：充值卡签名串
        # 返回值：
        #   rsp.ret_code：正常返回0
        #   rsp.err_msg：异常时返回异常详情
        #
        def Charge(self, cardid, cardkey):
            tm = str(int(time.time()))
            sign = CalcSign(self.pd_id, self.pd_key, tm)
            csign = CalcCardSign(cardid, cardkey, tm, self.pd_key)
            param = {
                "user_id": self.pd_id,
                "timestamp": tm,
                "sign": sign,
                'cardid': cardid,
                'csign': csign
            }
            url = self.host + "/api/charge"
            rsp = HttpRequest(url, param)
            if rsp.ret_code == 0:
                LOG("charge succ ret: {} request_id: {} pred: {} err: {}".format(rsp.ret_code, rsp.request_id,
                                                                                 rsp.pred_rsp.value, rsp.err_msg))
            else:
                LOG("charge failed ret: {} err: {}".format(rsp.ret_code, rsp.err_msg.encode('utf-8')))
            return rsp

        ##
        # 充值，只返回是否成功
        # 参数：cardid：充值卡号  cardkey：充值卡签名串
        # 返回值： 充值成功时返回0
        ##
        def ExtendCharge(self, cardid, cardkey):
            return self.Charge(cardid, cardkey).ret_code

        ##
        # 调用退款，只返回是否成功
        # 参数： request_id：需要退款的订单号
        # 返回值： 退款成功时返回0
        #
        # 注意:
        #    Predict识别接口，仅在ret_code == 0时才会进行扣款，才需要进行退款请求，否则无需进行退款操作
        # 注意2:
        #   退款仅在正常识别出结果后，无法通过网站验证的情况，请勿非法或者滥用，否则可能进行封号处理
        ##
        def JusticeExtend(self, request_id):
            return self.Justice(request_id).ret_code

        ##
        # 查询余额，只返回余额
        # 参数：无
        # 返回值：rsp.cust_val：余额
        ##
        def QueryBalcExtend(self):
            rsp = self.QueryBalc()
            return rsp.cust_val

        ##
        # 从文件识别验证码，只返回识别结果
        # 参数：pred_type;识别类型  file_name:文件名
        # 返回值： rsp.pred_rsp.value：识别的结果
        ##
        def PredictFromFileExtend(self, pred_type, file_name, head_info=""):
            rsp = self.PredictFromFile(pred_type, file_name, head_info)
            return rsp.pred_rsp.value

        ##
        # 识别接口，只返回识别结果
        # 参数：pred_type:识别类型  img_data:图片的数据
        # 返回值： rsp.pred_rsp.value：识别的结果
        ##
        def PredictExtend(self, pred_type, img_data, head_info=""):
            rsp = self.Predict(pred_type, img_data, head_info)
            return rsp.pred_rsp.value

except Exception as e:
    visual_block.Visual_Block_Info("yzm", 1, 2, e)

    log.error("[%s] %s", "yzm", str(e))
    raise e

# -*- 新建 Excel 文档
try:
    visual_block.Visual_Block_Info("新建 Excel 文档", 2, 0, "正在执行")

    import rpa.excel

    rpa_6a4539_excel = rpa.excel.create(visible=True, wps=False)

except Exception as e:
    visual_block.Visual_Block_Info("新建 Excel 文档", 2, 2, e)

    log.error("[%s] %s", "新建 Excel 文档", str(e))
    raise e

# -*- 设置列宽
try:
    visual_block.Visual_Block_Info("设置列宽", 3, 0, "正在执行")

    import rpa.excel

    rpa_6a4539_excel.get_sheet("").set_col_width("A" + str("1") + ":" + "M" + str("1"), "17")

except Exception as e:
    visual_block.Visual_Block_Info("设置列宽", 3, 2, e)

    log.error("[%s] %s", "设置列宽", str(e))
    raise e

# -*- 居中
try:
    visual_block.Visual_Block_Info("居中", 4, 0, "正在执行")

    import rpa.excel

    rpa_6a4539_excel.get_sheet("").set_style("A" + str("1") + ":" + "M" + str("1"), style="align", value="居中")

except Exception as e:
    visual_block.Visual_Block_Info("居中", 4, 2, e)

    log.error("[%s] %s", "居中", str(e))
    raise e

# -*- head_list
try:
    visual_block.Visual_Block_Info("head_list", 5, 0, "正在执行")

    head_list = ['发票代码', '发票代码结果', '销售方名称', '销售方税号', '开票日期', '购买方单位', '购买方税号', '小写金额', '校验码']

except Exception as e:
    visual_block.Visual_Block_Info("head_list", 5, 2, e)

    log.error("[%s] %s", "head_list", str(e))
    raise e

# -*- 写入表头
try:
    visual_block.Visual_Block_Info("写入表头", 6, 0, "正在执行")

    import rpa.excel

    rpa_6a4539_excel.get_sheet("").write("A" + str("1") + ":" + "I" + str("1"), head_list)

except Exception as e:
    visual_block.Visual_Block_Info("写入表头", 6, 2, e)

    log.error("[%s] %s", "写入表头", str(e))
    raise e

# -*- 文件夹绝对路径
try:
    visual_block.Visual_Block_Info("文件夹绝对路径", 7, 0, "正在执行")

    a_path = "C:\\Users\\Administrator\\Desktop\\第三题 附件\\fapiao_pics\\"

except Exception as e:
    visual_block.Visual_Block_Info("文件夹绝对路径", 7, 2, e)

    log.error("[%s] %s", "文件夹绝对路径", str(e))
    raise e

# -*- 获取文件列表
try:
    visual_block.Visual_Block_Info("获取文件列表", 8, 0, "正在执行")

    import rpa.file_folder

    rpa_e54673_array_string = rpa.file_folder.list_dir(path=a_path, dirtype="file", withpath=False, isext=True)

except Exception as e:
    visual_block.Visual_Block_Info("获取文件列表", 8, 2, e)

    log.error("[%s] %s", "获取文件列表", str(e))
    raise e

# -*- 接收文件列表
try:
    visual_block.Visual_Block_Info("接收文件列表", 9, 0, "正在执行")

    file_list = rpa_e54673_array_string

except Exception as e:
    visual_block.Visual_Block_Info("接收文件列表", 9, 2, e)

    log.error("[%s] %s", "接收文件列表", str(e))
    raise e

# -*- 得到新的文件列表
try:
    visual_block.Visual_Block_Info("得到新的文件列表", 10, 0, "正在执行")

    for i, v in enumerate(file_list[:]):
        if v.endswith('.png') or v.endswith('.jpg') or v.endswith('.pdf'):
            pass
        else:
            file_list.remove(v)

except Exception as e:
    visual_block.Visual_Block_Info("得到新的文件列表", 10, 2, e)

    log.error("[%s] %s", "得到新的文件列表", str(e))
    raise e

# -*- 数组长度
try:
    visual_block.Visual_Block_Info("数组长度", 11, 0, "正在执行")

    rpa_35b5f0_array_any = len(file_list)

except Exception as e:
    visual_block.Visual_Block_Info("数组长度", 11, 2, e)

    log.error("[%s] %s", "数组长度", str(e))
    raise e

# -*- 文件索引
try:
    visual_block.Visual_Block_Info("文件索引", 12, 0, "正在执行")

    count_num = 0

except Exception as e:
    visual_block.Visual_Block_Info("文件索引", 12, 2, e)

    log.error("[%s] %s", "文件索引", str(e))
    raise e

# -*- 创建None变量
try:
    visual_block.Visual_Block_Info("创建None变量", 13, 0, "正在执行")

    cre_none = None

except Exception as e:
    visual_block.Visual_Block_Info("创建None变量", 13, 2, e)

    log.error("[%s] %s", "创建None变量", str(e))
    raise e

# -*- Excel行数
try:
    visual_block.Visual_Block_Info("Excel行数", 14, 0, "正在执行")

    row = 2

except Exception as e:
    visual_block.Visual_Block_Info("Excel行数", 14, 2, e)

    log.error("[%s] %s", "Excel行数", str(e))
    raise e

# -*- 遍历文件列表
try:
    visual_block.Visual_Block_Info("遍历文件列表", 15, 0, "正在执行")

    for rpa_4b969d_any in range(0, rpa_35b5f0_array_any, 1):

        # -*- 启动浏览器
        try:
            option = ChromeOptions()
            prefs = {'safebrowsing.enabled': True}
            option.add_experimental_option('prefs', prefs)
            rpa_6a9438_browser = Chrome(option)

        except Exception as e:
            log.error("[%s] %s", "启动浏览器", str(e))
            raise e

        # -*- 浏览器窗口最大化
        try:
            rpa_6a9438_browser.max_window()

        except Exception as e:
            log.error("[%s] %s", "浏览器窗口最大化", str(e))
            raise e

        # -*- 打开网页
        try:
            rpa_c7ad3a = rpa_6a9438_browser.create("https://inv-veri.chinatax.gov.cn/index.html")

        except Exception as e:
            log.error("[%s] %s", "打开网页", str(e))
            raise e

        # -*- 得到文件
        try:
            rpa_573c3d_array_any = file_list[count_num]

        except Exception as e:
            log.error("[%s] %s", "得到文件", str(e))
            raise e

        # -*- 文件的绝对路径
        try:
            rpa_9a3dec_string = a_path + rpa_573c3d_array_any

        except Exception as e:
            log.error("[%s] %s", "文件的绝对路径", str(e))
            raise e

        # -*- 发票抽取
        try:
            from rpa.ocr.ocr import OCR

            rpa_4c4ea6 = OCR().recognize(rpa_9a3dec_string, 'invoice')

        except Exception as e:
            log.error("[%s] %s", "发票抽取", str(e))
            raise e

        # -*- e_list
        try:
            e_list = []

        except Exception as e:
            log.error("[%s] %s", "e_list", str(e))
            raise e

        # -*- 接受日期
        try:
            s = rpa_4c4ea6.get("开票日期")

        except Exception as e:
            log.error("[%s] %s", "接受日期", str(e))
            raise e

        # -*- 创建日期变量
        try:
            date_fin = []

        except Exception as e:
            log.error("[%s] %s", "创建日期变量", str(e))
            raise e

        # -*- 转换日期
        try:
            import re

            s_list = re.findall(r'\d+', s)
            if len(s_list) != 1:
                if len(s_list[1]) == 1:
                    s_list[1] = '0' + s_list[1]
                if len(s_list[2]) == 1:
                    s_list[2] = '0' + s_list[2]
                date_fin = [s_list[0] + s_list[1] + s_list[2]]
            else:
                date_fin = s_list

        except Exception as e:
            log.error("[%s] %s", "转换日期", str(e))
            raise e

        # -*- 最终日期
        try:
            date_end = date_fin

        except Exception as e:
            log.error("[%s] %s", "最终日期", str(e))
            raise e

        # -*- 切片日期
        try:
            rpa_d412c4 = date_end[0]

        except Exception as e:
            log.error("[%s] %s", "切片日期", str(e))
            raise e

        # -*- 获取本地结果数组
        try:
            e_list = ["'" + rpa_4c4ea6.get("发票代码"),
                      "'" + rpa_4c4ea6.get("发票号码"),
                      "'" + rpa_d412c4,
                      "'" + rpa_4c4ea6.get("校验码"),
                      "'" + '%.2f' % float(rpa_4c4ea6.get("发票金额")),
                      "'" + rpa_4c4ea6.get("受票方名称"),
                      "'" + rpa_4c4ea6.get("受票方税号"),
                      "'" + rpa_4c4ea6.get("销售方名称"),
                      "'" + rpa_4c4ea6.get("销售方税号")]
            e_list[5] = e_list[5].replace(r'（', '(').replace(r'）', ')')
            e_list[7] = e_list[7].replace(r'（', '(').replace(r'）', ')')

        except Exception as e:
            log.error("[%s] %s", "获取本地结果数组", str(e))
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
            log.error("[%s] %s", "填写发票代码", str(e))
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
            log.error("[%s] %s", "填写发票号码", str(e))
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
            log.error("[%s] %s", "填写开票日期", str(e))
            raise e

        # -*- 获取网页元素内容1
        try:
            from time import sleep

            sleep(0)
            rpa_c7ad3a.add_element("rpa_605b75", id="context", css="#context",
                                   xpath=["//span[@id='context']", "//div[@id='content2']/table/tbody/tr[4]/td/span[2]",
                                          "//td/span[2]", "//span[contains(.,'开具金额(不含税)：')]"], frame=[])
            rpa_c7ad3a.switch_to_frame_by_path([])
            rpa_1592de_string = rpa_c7ad3a.get_element("rpa_605b75", timeout=30).text()
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取网页元素内容1", str(e))
            raise e

        # -*- 判断是否校验码
        try:

            if rpa_1592de_string == "开具金额(不含税)：	":

                # -*- 填写不含税金额
                try:
                    from time import sleep

                    sleep(0)
                    rpa_c7ad3a.add_element("rpa_4a786d", id="kjje", css="#kjje", xpath=["//input[@id='kjje']",
                                                                                        "//div[@id='content2']/table/tbody/tr[4]/td[2]/input",
                                                                                        "//tr[4]/td[2]/input"],
                                           frame=[])
                    rpa_c7ad3a.switch_to_frame_by_path([])
                    rpa_c7ad3a.get_element("rpa_4a786d", timeout=30).input(rpa_4c4ea6.get("不含税金额"), simulate=True)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "填写不含税金额", str(e))
                    raise e
            else:

                # -*- 校验码变量
                try:
                    jym_str = rpa_4c4ea6.get("校验码")

                except Exception as e:
                    log.error("[%s] %s", "校验码变量", str(e))
                    raise e

                # -*- 字符串操作2
                try:
                    rpa_244cf6_string = jym_str[14:]

                except Exception as e:
                    log.error("[%s] %s", "字符串操作2", str(e))
                    raise e

                # -*- 填写校验码后6位
                try:
                    from time import sleep

                    sleep(0)
                    rpa_c7ad3a.add_element("rpa_34dc63", id="kjje", css="#kjje", xpath=["//input[@id='kjje']",
                                                                                        "//div[@id='content2']/table/tbody/tr[4]/td[2]/input",
                                                                                        "//tr[4]/td[2]/input"],
                                           frame=[])
                    rpa_c7ad3a.switch_to_frame_by_path([])
                    rpa_c7ad3a.get_element("rpa_34dc63", timeout=30).input(rpa_244cf6_string, simulate=True)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "填写校验码后6位", str(e))
                    raise e
        except Exception as e:
            log.error("[%s] %s", "判断是否校验码", str(e))
            raise e

        # -*- 点击验证码框
        try:
            from time import sleep

            sleep(0)
            rpa_c7ad3a.add_element("rpa_2345cc", id="yzm", css="#yzm",
                                   xpath=["//input[@id='yzm']", "//div[@id='content2']/table/tbody/tr[5]/td[2]/input",
                                          "//tr[5]/td[2]/input"], frame=[])
            rpa_c7ad3a.switch_to_frame_by_path([])
            from rpa import ElementClickMethod

            rpa_c7ad3a.get_element("rpa_2345cc", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "点击验证码框", str(e))
            raise e

        # -*- 获取Table内容
        try:
            from time import sleep

            sleep(0)
            rpa_c7ad3a.add_element("rpa_17e201", id="", css="tbody",
                                   xpath=["//div[@id='content2']/table/tbody", "//tbody"], frame=[])
            rpa_c7ad3a.switch_to_frame_by_path([])
            rpa_1400e4_string = rpa_c7ad3a.get_element("rpa_17e201", timeout=30).text()
            sleep(0)

        except Exception as e:
            log.error("[%s] %s", "获取Table内容", str(e))
            raise e

        # -*- 判断错误信息
        try:

            if "发票代码有误!" in rpa_1400e4_string or "发票号码有误!" in rpa_1400e4_string or "开票日期有误!" in rpa_1400e4_string or "校验码有误!" in rpa_1400e4_string:

                # -*- 截图文件名111
                try:
                    rpa_bf2aaf = "截图_" + rpa_573c3d_array_any

                except Exception as e:
                    log.error("[%s] %s", "截图文件名111", str(e))
                    raise e

                # -*- 截图的绝对路径111
                try:
                    rpa_406753 = "C:\\Users\\Administrator\\Desktop\\all_test\\orientation-master-69c44478cbf4319c878dd001239880dc717ac6fb\\rpa\\入门三道题\\第三题 附件\\false_res" + rpa_bf2aaf

                except Exception as e:
                    log.error("[%s] %s", "截图的绝对路径111", str(e))
                    raise e

                # -*- 失败页面截图11
                try:
                    from time import sleep

                    sleep(0)
                    rpa_c7ad3a.add_element("rpa_98d82f", id="", css="tbody",
                                           xpath=["//div[@id='content2']/table/tbody", "//tbody"], frame=[])
                    rpa_c7ad3a.switch_to_frame_by_path([])
                    rpa_c7ad3a.get_element("rpa_98d82f", timeout=30).screen_shot(rpa_406753)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "失败页面截图11", str(e))
                    raise e

                # -*- 拼接发票代码11
                try:
                    rpa_9db20b = "'" + rpa_4c4ea6.get("发票代码")

                except Exception as e:
                    log.error("[%s] %s", "拼接发票代码11", str(e))
                    raise e

                # -*- 写入发票代码11
                try:
                    import rpa.excel

                    rpa_6a4539_excel.get_sheet("").write("A" + str(row), rpa_9db20b)

                except Exception as e:
                    log.error("[%s] %s", "写入发票代码11", str(e))
                    raise e

                # -*- 写入False
                try:
                    import rpa.excel

                    rpa_6a4539_excel.get_sheet("").write("B" + str(row), '发票有误')

                except Exception as e:
                    log.error("[%s] %s", "写入False", str(e))
                    raise e

                # -*- Excel + 1计算1
                try:
                    rpa_6f3ae2 = row + 1

                except Exception as e:
                    log.error("[%s] %s", "Excel + 1计算1", str(e))
                    raise e

                # -*- 新Excel行数1
                try:
                    row = rpa_6f3ae2

                except Exception as e:
                    log.error("[%s] %s", "新Excel行数1", str(e))
                    raise e

                # -*- 索引计算1
                try:
                    rpa_8ffad7 = count_num + 1

                except Exception as e:
                    log.error("[%s] %s", "索引计算1", str(e))
                    raise e

                # -*- 新索引赋值1
                try:
                    count_num = rpa_8ffad7

                except Exception as e:
                    log.error("[%s] %s", "新索引赋值1", str(e))
                    raise e

                # -*- 关闭网页21
                try:
                    rpa_6a9438_browser.quit()

                except Exception as e:
                    log.error("[%s] %s", "关闭网页21", str(e))
                    raise e

                # -*- 退出循环21
                try:
                    continue

                except Exception as e:
                    log.error("[%s] %s", "退出循环21", str(e))
                    raise e
            else:
                pass

        except Exception as e:
            log.error("[%s] %s", "判断错误信息", str(e))
            raise e

        # -*- 循环执行
        try:

            while "1" == "1":

                # -*- 延时执行
                try:
                    from time import sleep

                    sleep(1)

                except Exception as e:
                    log.error("[%s] %s", "延时执行", str(e))
                    raise e

                # -*- 点击刷新验证码
                try:
                    from time import sleep

                    sleep(0)
                    rpa_c7ad3a.add_element("rpa_678630", id="yzm_img", css="#yzm_img",
                                           xpath=["//img[@id='yzm_img']", "//td[@id='imgarea']/div/a/img", "//a/img"],
                                           frame=[])
                    rpa_c7ad3a.switch_to_frame_by_path([])
                    from rpa import ElementClickMethod

                    rpa_c7ad3a.get_element("rpa_678630", timeout=5).click(method=ElementClickMethod.MOUSE_CLICK)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "点击刷新验证码", str(e))
                    raise e

                # -*- 获取颜色内容
                try:
                    from time import sleep

                    sleep(0)
                    rpa_c7ad3a.add_element("rpa_0ed401", id="yzminfo", css="#yzminfo", xpath=["//td[@id='yzminfo']",
                                                                                              "//div[@id='content2']/table/tbody/tr[5]/td[3]",
                                                                                              "//tr[5]/td[3]"],
                                           frame=[])
                    rpa_c7ad3a.switch_to_frame_by_path([])
                    rpa_676bca_string = rpa_c7ad3a.get_element("rpa_0ed401", timeout=30).text()
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取颜色内容", str(e))
                    raise e

                # -*- 获取图片base64
                try:
                    from time import sleep

                    sleep(0)
                    rpa_c7ad3a.add_element("rpa_eaa9ba", id="yzm_img", css="#yzm_img", xpath=['//*[@id="yzm_img"]',
                                                                                              '/html/body/div/div[2]/table/tbody/tr[6]/td[2]/div/a/img[1]'],
                                           frame=[])
                    rpa_c7ad3a.switch_to_frame_by_path([])
                    rpa_0b4465_string = rpa_c7ad3a.get_element("rpa_eaa9ba", timeout=30).get_attr("src")
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取图片base64", str(e))
                    raise e

                # -*- 创建验证码变量
                try:
                    res = ''

                except Exception as e:
                    log.error("[%s] %s", "创建验证码变量", str(e))
                    raise e

                # -*- 图片验证
                try:
                    pd_id = "119716"
                    pd_key = "2KQkaJfgXBNuS08Pr5nbKX+qk1VzRoio"
                    app_id = "302317"
                    app_key = ""
                    pred_type = "80400"
                    api = FateadmApi(app_id, app_key, pd_id, pd_key)
                    color_dict = {'红色': '01', '黄色': '02', '蓝色': '03'}
                    color = '00'
                    for k, v in color_dict.items():
                        if k in rpa_676bca_string:
                            color = v
                    try:
                        image_data = rpa_0b4465_string.split(',')[1]
                        color = json.dumps({'color': color})
                        image_data = base64.b64decode(image_data)
                        rsp = api.Predict(pred_type, image_data, color)
                        r_id = rsp.request_id
                        res = rsp.pred_rsp.value

                    except Exception as e:
                        log.error(e)

                except Exception as e:
                    log.error("[%s] %s", "图片验证", str(e))
                    raise e

                # -*- 填写验证码
                try:
                    from time import sleep

                    sleep(0)
                    rpa_c7ad3a.add_element("rpa_c2bfbc", id="yzm", css="#yzm", xpath=["//input[@id='yzm']",
                                                                                      "//div[@id='content2']/table/tbody/tr[5]/td[2]/input",
                                                                                      "//tr[5]/td[2]/input"], frame=[])
                    rpa_c7ad3a.switch_to_frame_by_path([])
                    rpa_c7ad3a.get_element("rpa_c2bfbc", timeout=30).input(res, simulate=True)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "填写验证码", str(e))
                    raise e

                # -*- 点击查询
                try:
                    from time import sleep

                    sleep(0)
                    rpa_c7ad3a.add_element("rpa_54e1b9", id="checkfp", css="#checkfp", xpath=["//button[@id='checkfp']",
                                                                                              "//div[@id='content2']/table/tbody/tr[7]/td/div/button[2]",
                                                                                              "//button[2]"], frame=[])
                    rpa_c7ad3a.switch_to_frame_by_path([])
                    from rpa import ElementClickMethod

                    rpa_c7ad3a.get_element("rpa_54e1b9", timeout=30).click(method=ElementClickMethod.MOUSE_CLICK)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "点击查询", str(e))
                    raise e

                # -*- 获取成功网页元素
                try:
                    from time import sleep

                    sleep(2)
                    rpa_c7ad3a.add_element("rpa_426edb", id="fpcc_dzfp", css="#fpcc_dzfp",
                                           xpath=['//*[@id="fpcc_dzfp"]',
                                                  '/html/body/div/div/div[2]/div/div[1]/div[2]/div/h1'], frame=[0])
                    rpa_c7ad3a.switch_to_frame_by_path([0])
                    rpa_5a6268 = rpa_c7ad3a.get_element(element_name="rpa_426edb", index=0, timeout=5)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取成功网页元素", str(e))
                    raise e

                # -*- 获取弹出框
                try:
                    from time import sleep

                    sleep(2)
                    rpa_c7ad3a.add_element("rpa_5e845d", id="popup_message", css="#popup_message",
                                           xpath=["//div[@id='popup_message']", "//div[@id='popup_content']/div",
                                                  "//div[4]/div/div"], frame=[])
                    rpa_c7ad3a.switch_to_frame_by_path([])
                    rpa_72b4c5_webelement = rpa_c7ad3a.get_element(element_name="rpa_5e845d", index=0, timeout=5)
                    sleep(0)

                except Exception as e:
                    log.error("[%s] %s", "获取弹出框", str(e))
                    raise e

                # -*- 弹出框是否出现
                try:

                    if rpa_72b4c5_webelement != cre_none:

                        # -*- 获取弹出框内容
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_c7ad3a.switch_to_frame_by_path(rpa_72b4c5_webelement.frame)
                            rpa_37694b_string = rpa_72b4c5_webelement.text()
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取弹出框内容", str(e))
                            raise e

                        # -*- 验证码错误
                        try:

                            if rpa_37694b_string == "验证码错误!":

                                # -*- 退款
                                try:
                                    api.Justice(r_id)

                                except Exception as e:
                                    log.error("[%s] %s", "退款", str(e))
                                    raise e

                                # -*- 点击确定
                                try:
                                    from time import sleep

                                    sleep(0)
                                    rpa_c7ad3a.add_element("rpa_a5e6b3", id="popup_ok", css="#popup_ok",
                                                           xpath=["//input[@id='popup_ok']",
                                                                  "//div[@id='popup_panel']/input", "//div[2]/input"],
                                                           frame=[])
                                    rpa_c7ad3a.switch_to_frame_by_path([])
                                    from rpa import ElementClickMethod

                                    rpa_c7ad3a.get_element("rpa_a5e6b3", timeout=30).click(
                                        method=ElementClickMethod.MOUSE_CLICK)
                                    sleep(0)

                                except Exception as e:
                                    log.error("[%s] %s", "点击确定", str(e))
                                    raise e

                                # -*- 下一次循环
                                try:
                                    continue

                                except Exception as e:
                                    log.error("[%s] %s", "下一次循环", str(e))
                                    raise e
                            else:

                                # -*- 验证码失效
                                try:

                                    if rpa_37694b_string == "验证码失效!":

                                        # -*- 点击确定1
                                        try:
                                            from time import sleep

                                            sleep(0)
                                            rpa_c7ad3a.add_element("rpa_a5e6b3", id="popup_ok", css="#popup_ok",
                                                                   xpath=["//input[@id='popup_ok']",
                                                                          "//div[@id='popup_panel']/input",
                                                                          "//div[2]/input"], frame=[])
                                            rpa_c7ad3a.switch_to_frame_by_path([])
                                            from rpa import ElementClickMethod

                                            rpa_c7ad3a.get_element("rpa_a5e6b3", timeout=30).click(
                                                method=ElementClickMethod.MOUSE_CLICK)
                                            sleep(0)

                                        except Exception as e:
                                            log.error("[%s] %s", "点击确定1", str(e))
                                            raise e

                                        # -*- 下一次循环1
                                        try:
                                            continue

                                        except Exception as e:
                                            log.error("[%s] %s", "下一次循环1", str(e))
                                            raise e
                                    else:

                                        # -*- 发票次数上限
                                        try:

                                            if rpa_37694b_string == "超过该张发票当日查验次数(请于次日再次查验)!":

                                                # -*- 截图文件名11
                                                try:
                                                    rpa_7c992e = "截图_" + rpa_573c3d_array_any

                                                except Exception as e:
                                                    log.error("[%s] %s", "截图文件名11", str(e))
                                                    raise e

                                                # -*- 截图的绝对路径11
                                                try:
                                                    rpa_627b65 = "C:\\Users\\Administrator\\Desktop\\all_test\\orientation-master-69c44478cbf4319c878dd001239880dc717ac6fb\\rpa\\入门三道题\\第三题 附件\\false_res\\" + rpa_7c992e

                                                except Exception as e:
                                                    log.error("[%s] %s", "截图的绝对路径11", str(e))
                                                    raise e

                                                # -*- 失败页面截图1
                                                try:
                                                    from time import sleep

                                                    sleep(0)
                                                    rpa_c7ad3a.add_element("rpa_98d82f", id="popup_container",
                                                                           css="#popup_container",
                                                                           xpath=["//div[@id='popup_container']",
                                                                                  "//body/div[4]"], frame=[])
                                                    rpa_c7ad3a.switch_to_frame_by_path([])
                                                    rpa_c7ad3a.get_element("rpa_98d82f", timeout=30).screen_shot(
                                                        rpa_627b65)
                                                    sleep(0)

                                                except Exception as e:
                                                    log.error("[%s] %s", "失败页面截图1", str(e))
                                                    raise e

                                                # -*- 拼接发票代码1
                                                try:
                                                    rpa_ce24a3 = "'" + rpa_4c4ea6.get("发票代码")

                                                except Exception as e:
                                                    log.error("[%s] %s", "拼接发票代码1", str(e))
                                                    raise e

                                                # -*- 写入发票代码1
                                                try:
                                                    import rpa.excel

                                                    rpa_6a4539_excel.get_sheet("").write("A" + str(row), rpa_ce24a3)

                                                except Exception as e:
                                                    log.error("[%s] %s", "写入发票代码1", str(e))
                                                    raise e

                                                # -*- 写入对比结果
                                                try:
                                                    import rpa.excel

                                                    rpa_6a4539_excel.get_sheet("").write("B" + str(row), '次数上限')

                                                except Exception as e:
                                                    log.error("[%s] %s", "写入对比结果", str(e))
                                                    raise e

                                                # -*- Excel + 1计算
                                                try:
                                                    rpa_5a990e_number = row + 1

                                                except Exception as e:
                                                    log.error("[%s] %s", "Excel + 1计算", str(e))
                                                    raise e

                                                # -*- 新Excel行数
                                                try:
                                                    row = rpa_5a990e_number

                                                except Exception as e:
                                                    log.error("[%s] %s", "新Excel行数", str(e))
                                                    raise e

                                                # -*- 索引计算
                                                try:
                                                    rpa_73a4e3_number = count_num + 1

                                                except Exception as e:
                                                    log.error("[%s] %s", "索引计算", str(e))
                                                    raise e

                                                # -*- 新索引赋值
                                                try:
                                                    count_num = rpa_73a4e3_number

                                                except Exception as e:
                                                    log.error("[%s] %s", "新索引赋值", str(e))
                                                    raise e

                                                # -*- 关闭网页2
                                                try:
                                                    rpa_6a9438_browser.quit()

                                                except Exception as e:
                                                    log.error("[%s] %s", "关闭网页2", str(e))
                                                    raise e

                                                # -*- 退出循环2
                                                try:
                                                    break

                                                except Exception as e:
                                                    log.error("[%s] %s", "退出循环2", str(e))
                                                    raise e
                                            else:
                                                pass

                                        except Exception as e:
                                            log.error("[%s] %s", "发票次数上限", str(e))
                                            raise e
                                except Exception as e:
                                    log.error("[%s] %s", "验证码失效", str(e))
                                    raise e
                        except Exception as e:
                            log.error("[%s] %s", "验证码错误", str(e))
                            raise e
                    else:
                        pass

                except Exception as e:
                    log.error("[%s] %s", "弹出框是否出现", str(e))
                    raise e

                # -*- 条件判断
                try:

                    if rpa_5a6268 != cre_none:

                        # -*- 获取标题
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_c7ad3a.add_element("rpa_b2dbce", id="", css="", xpath=['//*[@id="fpcc_jp"]',
                                                                                       '/html/body/div/div/div[2]/div/div[1]/div[2]/div/h1[1]'],
                                                   frame=[0])
                            rpa_c7ad3a.switch_to_frame_by_path([0])
                            rpa_94f34b_string = rpa_c7ad3a.get_element("rpa_b2dbce", timeout=30).text()
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取标题", str(e))
                            raise e

                        # -*- 条件判断3
                        try:

                            if "卷票" in rpa_94f34b_string:

                                # -*- 获取网页Table卷票
                                try:
                                    from time import sleep

                                    sleep(0)
                                    rpa_c7ad3a.add_element("rpa_4a07b6", id="", css="",
                                                           xpath=['//*[@id="tabPage-jsfp"]/div/table',
                                                                  '/html/body/div/div/div[2]/div/div[1]/div[2]/div/div/table'],
                                                           frame=[0])
                                    rpa_c7ad3a.switch_to_frame_by_path([0])
                                    rpa_08dc67_string = rpa_c7ad3a.get_element("rpa_4a07b6", timeout=30).text_of_table()
                                    sleep(0)

                                except Exception as e:
                                    log.error("[%s] %s", "获取网页Table卷票", str(e))
                                    raise e

                                # -*- jp_list
                                try:
                                    jp_list = []

                                except Exception as e:
                                    log.error("[%s] %s", "jp_list", str(e))
                                    raise e

                                # -*- bjp_list
                                try:
                                    bjp_list = []

                                except Exception as e:
                                    log.error("[%s] %s", "bjp_list", str(e))
                                    raise e

                                # -*- f_res_list 
                                try:
                                    f_res_list = rpa_4c4ea6.get("发票代码")

                                except Exception as e:
                                    log.error("[%s] %s", "f_res_list ", str(e))
                                    raise e

                                # -*- 得到卷票对比结果
                                try:
                                    import re

                                    bjp_list = [
                                        "'" + rpa_4c4ea6.get("发票代码"),
                                        "'" + rpa_4c4ea6.get("发票号码"),
                                        "'" + rpa_4c4ea6.get("销售方名称").replace(r'（', '(').replace(r'）', ')'),
                                        "'" + rpa_4c4ea6.get("销售方税号"),
                                        "'" + rpa_d412c4,
                                        "'" + rpa_4c4ea6.get("受票方名称").replace(r'（', '(').replace(r'）', ')'),
                                        "'" + rpa_4c4ea6.get("受票方税号"),
                                        "'" + '%.2f' % float(rpa_4c4ea6.get("发票金额")),
                                        "'" + rpa_4c4ea6.get("校验码"),
                                    ]
                                    print(bjp_list)
                                    for i, v in enumerate(rpa_08dc67_string):
                                        if i == 5:
                                            v1 = v[0].split('：')[1]
                                            v = ''.join(re.findall(r'\d+', v1))
                                        elif i == 2 or i == 8 or i == 9 or i == 10 or i == 11 or i == 13:
                                            continue
                                        elif i == 12:
                                            v = v[0].split('：￥')[1]
                                        else:
                                            v = v[0].split('：')[1]
                                        jp_list.append(v)
                                    print(jp_list)
                                    jp_res = list(zip(bjp_list, jp_list))
                                    for i, v in enumerate(jp_res):
                                        if v[0] != v[1]:
                                            f_res_list.append('对比错误')
                                        else:
                                            f_res_list.append('对比成功')
                                    print(f_res_list)

                                except Exception as e:
                                    log.error("[%s] %s", "得到卷票对比结果", str(e))
                                    raise e

                                # -*- 写入/设置 Excel 内容13
                                try:
                                    import rpa.excel

                                    rpa_6a4539_excel.get_sheet("").write("A" + str(row) + ":" + "I" + str(row),
                                                                         f_res_list)

                                except Exception as e:
                                    log.error("[%s] %s", "写入/设置 Excel 内容13", str(e))
                                    raise e

                                # -*- 数学运算
                                try:
                                    rpa_4f0a4b_number = row + 1

                                except Exception as e:
                                    log.error("[%s] %s", "数学运算", str(e))
                                    raise e

                                # -*- 赋值操作
                                try:
                                    row = rpa_4f0a4b_number

                                except Exception as e:
                                    log.error("[%s] %s", "赋值操作", str(e))
                                    raise e

                                # -*- 索引加上11
                                try:
                                    rpa_5c9b5e = count_num + 1

                                except Exception as e:
                                    log.error("[%s] %s", "索引加上11", str(e))
                                    raise e

                                # -*- 得到新索引1
                                try:
                                    count_num = rpa_5c9b5e

                                except Exception as e:
                                    log.error("[%s] %s", "得到新索引1", str(e))
                                    raise e

                                # -*- 关闭网页11
                                try:
                                    rpa_6a9438_browser.quit()

                                except Exception as e:
                                    log.error("[%s] %s", "关闭网页11", str(e))
                                    raise e

                                # -*- 退出循环11
                                try:
                                    break

                                except Exception as e:
                                    log.error("[%s] %s", "退出循环11", str(e))
                                    raise e
                            else:
                                pass

                        except Exception as e:
                            log.error("[%s] %s", "条件判断3", str(e))
                            raise e

                        # -*- 获取Table1
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_c7ad3a.add_element("rpa_856f3f", id="", css="",
                                                   xpath=['//*[@id="tabPage-dzfp"]/table[1]',
                                                          '/html/body/div/div/div[2]/div/div[1]/div[2]/div/table[1]'],
                                                   frame=[0])
                            rpa_c7ad3a.switch_to_frame_by_path([0])
                            rpa_99b83b = rpa_c7ad3a.get_element("rpa_856f3f", timeout=30).text_of_table(row=0)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取Table1", str(e))
                            raise e

                        # -*- a_list
                        try:
                            a_list = rpa_99b83b

                        except Exception as e:
                            log.error("[%s] %s", "a_list", str(e))
                            raise e

                        # -*- b_list
                        try:
                            b_list = []

                        except Exception as e:
                            log.error("[%s] %s", "b_list", str(e))
                            raise e

                        # -*- 得到信息
                        try:
                            for v in a_list[:]:
                                if v == '\xa0':
                                    a_list.remove(v)
                            for i in a_list[:4]:
                                if i.split('：')[0] == '开票日期':
                                    import re

                                    x = ''.join(re.findall(r'\d+', i.split('：')[1]))
                                    b_list.append("'" + x)
                                    continue
                                b_list.append("'" + i.split('：')[1])


                        except Exception as e:
                            log.error("[%s] %s", "得到信息", str(e))
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
                            log.error("[%s] %s", "获取Table2", str(e))
                            raise e

                        # -*- 接收Table2
                        try:
                            a = rpa_d0d673

                        except Exception as e:
                            log.error("[%s] %s", "接收Table2", str(e))
                            raise e

                        # -*- 存储获取的信息
                        try:
                            a_info = []

                        except Exception as e:
                            log.error("[%s] %s", "存储获取的信息", str(e))
                            raise e

                        # -*- 得到金额
                        try:
                            b = a[4][0].replace('\t', '\n').split('\n')
                            for z in b:
                                if '小写' in z:
                                    b_list.append("'" + '%.2f' % float(z.split('￥')[1]))

                        except Exception as e:
                            log.error("[%s] %s", "得到金额", str(e))
                            raise e

                        # -*- 对Table2进行处理
                        try:
                            for i, v in enumerate(a):
                                b = len(v)
                                if b == 5:
                                    a[i] = v[1:3]
                            # '购买方名称','购买方纳税人识别号','购买方地址、电话','购买方开户行及账号','销售方名称','销售方纳税人识别号','销售方地址、电话','销售方开户行及账号']
                            for x in a[:2]:
                                x[1] = x[1].replace(r'（', '(').replace(r'）', ')')
                                b_list.append("'" + x[1])
                            for y in a[5:7]:
                                y[1] = y[1].replace(r'（', '(').replace(r'）', ')')
                                b_list.append("'" + y[1])


                        except Exception as e:
                            log.error("[%s] %s", "对Table2进行处理", str(e))
                            raise e

                        # -*- 字符串操作1
                        try:
                            rpa_f976aa_string = "'" + rpa_4c4ea6.get("发票代码")

                        except Exception as e:
                            log.error("[%s] %s", "字符串操作1", str(e))
                            raise e

                        # -*- 写入/设置 Excel 内容12
                        try:
                            import rpa.excel

                            rpa_6a4539_excel.get_sheet("").write("A" + str(row), rpa_f976aa_string)

                        except Exception as e:
                            log.error("[%s] %s", "写入/设置 Excel 内容12", str(e))
                            raise e

                        # -*- 条件判断2
                        try:

                            if e_list == b_list:

                                # -*- 创建正确结果文件夹
                                try:
                                    import rpa.file_folder
                                    import os

                                    rpa.file_folder.new_document(
                                        doc_path=os.path.join(r"C:\\Users\\Administrator\\Desktop\\第三题 附件", "true_res"),
                                        creat=True, cover=True)

                                except Exception as e:
                                    log.error("[%s] %s", "创建正确结果文件夹", str(e))
                                    raise e

                                # -*- 截图文件名112
                                try:
                                    rpa_f7a396 = "截图_" + rpa_573c3d_array_any

                                except Exception as e:
                                    log.error("[%s] %s", "截图文件名112", str(e))
                                    raise e

                                # -*- 截图的绝对路径112
                                try:
                                    rpa_c32773 = "C:\\Users\\Administrator\\Desktop\\all_test\\orientation-master-69c44478cbf4319c878dd001239880dc717ac6fb\\rpa\\入门三道题\\第三题 附件\\true_res\\" + rpa_f7a396

                                except Exception as e:
                                    log.error("[%s] %s", "截图的绝对路径112", str(e))
                                    raise e

                                # -*- 成功结果截图1
                                try:
                                    from time import sleep

                                    sleep(0)
                                    rpa_c7ad3a.add_element("rpa_98d82f", id="print_area", css="",
                                                           xpath=['//*[@id="print_area"]',
                                                                  '/html/body/div[1]/div/div[2]/div/div[1]'], frame=[0])
                                    rpa_c7ad3a.switch_to_frame_by_path([0])
                                    rpa_c7ad3a.get_element("rpa_98d82f", timeout=30).screen_shot(rpa_c32773)
                                    sleep(0)

                                except Exception as e:
                                    log.error("[%s] %s", "成功结果截图1", str(e))
                                    raise e

                                # -*- 创建变量
                                try:
                                    res_t = "结果正确"

                                except Exception as e:
                                    log.error("[%s] %s", "创建变量", str(e))
                                    raise e

                                # -*- 写入/设置 Excel 内容1
                                try:
                                    import rpa.excel

                                    rpa_6a4539_excel.get_sheet("").write("B" + str(row), res_t)

                                except Exception as e:
                                    log.error("[%s] %s", "写入/设置 Excel 内容1", str(e))
                                    raise e
                            else:

                                # -*- 创建错误结果文件夹
                                try:
                                    import rpa.file_folder
                                    import os

                                    rpa.file_folder.new_file(
                                        file_path=os.path.join(r"C:\\Users\\Administrator\\Desktop\\第三题 附件",
                                                               "false_res"), creat=True, cover=True)

                                except Exception as e:
                                    log.error("[%s] %s", "创建错误结果文件夹", str(e))
                                    raise e

                                # -*- 截图文件名1121
                                try:
                                    rpa_2b50cb = "截图_" + rpa_573c3d_array_any

                                except Exception as e:
                                    log.error("[%s] %s", "截图文件名1121", str(e))
                                    raise e

                                # -*- 截图的绝对路径1121
                                try:
                                    rpa_6d140b = "C:\\Users\\Administrator\\Desktop\\all_test\\orientation-master-69c44478cbf4319c878dd001239880dc717ac6fb\\rpa\\入门三道题\\第三题 附件\\false_res\\" + rpa_2b50cb

                                except Exception as e:
                                    log.error("[%s] %s", "截图的绝对路径1121", str(e))
                                    raise e

                                # -*- 失败结果截图11
                                try:
                                    from time import sleep

                                    sleep(0)
                                    rpa_c7ad3a.add_element("rpa_98d82f", id="print_area", css="",
                                                           xpath=['//*[@id="print_area"]',
                                                                  '/html/body/div[1]/div/div[2]/div/div[1]'], frame=[0])
                                    rpa_c7ad3a.switch_to_frame_by_path([0])
                                    rpa_c7ad3a.get_element("rpa_98d82f", timeout=30).screen_shot(rpa_6d140b)
                                    sleep(0)

                                except Exception as e:
                                    log.error("[%s] %s", "失败结果截图11", str(e))
                                    raise e

                                # -*- 创建变量1
                                try:
                                    res_f = "结果错误"

                                except Exception as e:
                                    log.error("[%s] %s", "创建变量1", str(e))
                                    raise e

                                # -*- 写入/设置 Excel 内容11
                                try:
                                    import rpa.excel

                                    rpa_6a4539_excel.get_sheet("").write("B" + str(row), res_f)

                                except Exception as e:
                                    log.error("[%s] %s", "写入/设置 Excel 内容11", str(e))
                                    raise e
                        except Exception as e:
                            log.error("[%s] %s", "条件判断2", str(e))
                            raise e

                        # -*- row + 1
                        try:
                            rpa_9ad017_number = row + 1

                        except Exception as e:
                            log.error("[%s] %s", "row + 1", str(e))
                            raise e

                        # -*- 赋值row
                        try:
                            row = rpa_9ad017_number

                        except Exception as e:
                            log.error("[%s] %s", "赋值row", str(e))
                            raise e

                        # -*- 索引加1
                        try:
                            rpa_8f3677_number = count_num + 1

                        except Exception as e:
                            log.error("[%s] %s", "索引加1", str(e))
                            raise e

                        # -*- 赋值索引
                        try:
                            count_num = rpa_8f3677_number

                        except Exception as e:
                            log.error("[%s] %s", "赋值索引", str(e))
                            raise e

                        # -*- 关闭网页
                        try:
                            rpa_6a9438_browser.quit()

                        except Exception as e:
                            log.error("[%s] %s", "关闭网页", str(e))
                            raise e

                        # -*- 退出循环
                        try:
                            break

                        except Exception as e:
                            log.error("[%s] %s", "退出循环", str(e))
                            raise e
                    else:

                        # -*- 获取网页元素
                        try:
                            from time import sleep

                            sleep(0)
                            rpa_c7ad3a.add_element("rpa_5f6b4e", id="", css="", xpath=['//*[@id="cyjg"]',
                                                                                       '/html/body/div/div/div/div[1]/table/tbody/tr/td/span[1]/strong'],
                                                   frame=[0])
                            rpa_c7ad3a.switch_to_frame_by_path([0])
                            rpa_ff4f7c_webelement = rpa_c7ad3a.get_element(element_name="rpa_5f6b4e", index=0,
                                                                           timeout=5)
                            sleep(0)

                        except Exception as e:
                            log.error("[%s] %s", "获取网页元素", str(e))
                            raise e

                        # -*- 条件判断1
                        try:

                            if rpa_ff4f7c_webelement != cre_none:

                                # -*- 获取网页元素内容
                                try:
                                    from time import sleep

                                    sleep(0)
                                    rpa_c7ad3a.switch_to_frame_by_path(rpa_ff4f7c_webelement.frame)
                                    rpa_318eed_string = rpa_ff4f7c_webelement.text()
                                    sleep(0)

                                except Exception as e:
                                    log.error("[%s] %s", "获取网页元素内容", str(e))
                                    raise e

                                # -*- 得到结果
                                try:
                                    res_str = rpa_318eed_string

                                except Exception as e:
                                    log.error("[%s] %s", "得到结果", str(e))
                                    raise e

                                # -*- 截图文件名1
                                try:
                                    rpa_a509b6 = "截图_" + rpa_573c3d_array_any

                                except Exception as e:
                                    log.error("[%s] %s", "截图文件名1", str(e))
                                    raise e

                                # -*- 截图的绝对路径1
                                try:
                                    rpa_87d4cf = "C:\\Users\\Administrator\\Desktop\\all_test\\orientation-master-69c44478cbf4319c878dd001239880dc717ac6fb\\rpa\\入门三道题\\第三题 附件\\false_res\\" + rpa_a509b6

                                except Exception as e:
                                    log.error("[%s] %s", "截图的绝对路径1", str(e))
                                    raise e

                                # -*- 失败页面截图
                                try:
                                    from time import sleep

                                    sleep(0)
                                    rpa_c7ad3a.add_element("rpa_98d82f", id="cms_r", css="",
                                                           xpath=['//*[@id="cms_r"]', '/html/body/div/div'], frame=[0])
                                    rpa_c7ad3a.switch_to_frame_by_path([0])
                                    rpa_c7ad3a.get_element("rpa_98d82f", timeout=30).screen_shot(rpa_87d4cf)
                                    sleep(0)

                                except Exception as e:
                                    log.error("[%s] %s", "失败页面截图", str(e))
                                    raise e

                                # -*- 拼接发票代码
                                try:
                                    rpa_0ca5ed_string = "'" + rpa_4c4ea6.get("发票代码")

                                except Exception as e:
                                    log.error("[%s] %s", "拼接发票代码", str(e))
                                    raise e

                                # -*- 写入发票代码
                                try:
                                    import rpa.excel

                                    rpa_6a4539_excel.get_sheet("").write("A" + str(row), rpa_0ca5ed_string)

                                except Exception as e:
                                    log.error("[%s] %s", "写入发票代码", str(e))
                                    raise e

                                # -*- 写入结果
                                try:
                                    import rpa.excel

                                    rpa_6a4539_excel.get_sheet("").write("B" + str(row), res_str)

                                except Exception as e:
                                    log.error("[%s] %s", "写入结果", str(e))
                                    raise e

                                # -*- Excel + 1运算
                                try:
                                    rpa_7086eb_number = row + 1

                                except Exception as e:
                                    log.error("[%s] %s", "Excel + 1运算", str(e))
                                    raise e

                                # -*- 赋值新row
                                try:
                                    row = rpa_7086eb_number

                                except Exception as e:
                                    log.error("[%s] %s", "赋值新row", str(e))
                                    raise e

                                # -*- 索引加上1
                                try:
                                    rpa_c0ba34_number = count_num + 1

                                except Exception as e:
                                    log.error("[%s] %s", "索引加上1", str(e))
                                    raise e

                                # -*- 得到新索引
                                try:
                                    count_num = rpa_c0ba34_number

                                except Exception as e:
                                    log.error("[%s] %s", "得到新索引", str(e))
                                    raise e

                                # -*- 关闭网页1
                                try:
                                    rpa_6a9438_browser.quit()

                                except Exception as e:
                                    log.error("[%s] %s", "关闭网页1", str(e))
                                    raise e

                                # -*- 退出循环1
                                try:
                                    break

                                except Exception as e:
                                    log.error("[%s] %s", "退出循环1", str(e))
                                    raise e
                            else:
                                pass

                        except Exception as e:
                            log.error("[%s] %s", "条件判断1", str(e))
                            raise e
                except Exception as e:
                    log.error("[%s] %s", "条件判断", str(e))
                    raise e
        except Exception as e:
            log.error("[%s] %s", "循环执行", str(e))
            raise e
except Exception as e:
    visual_block.Visual_Block_Info("遍历文件列表", 15, 2, e)

    log.error("[%s] %s", "遍历文件列表", str(e))
    raise e

# -*- 保存Excel 文档
try:
    visual_block.Visual_Block_Info("保存Excel 文档", 16, 0, "正在执行")

    import rpa.excel
    import os

    rpa_6a4539_excel.save(file=os.path.join(
        "C:\\Users\\Administrator\\Desktop\\all_test\\orientation-master-69c44478cbf4319c878dd001239880dc717ac6fb\\rpa\\入门三道题\\第三题 附件\\",
        "发票验证.xlsx"), pass_word="")

except Exception as e:
    visual_block.Visual_Block_Info("保存Excel 文档", 16, 2, e)

    log.error("[%s] %s", "保存Excel 文档", str(e))
    raise e

# -*- 关闭Excel 文档
try:
    visual_block.Visual_Block_Info("关闭Excel 文档", 17, 0, "正在执行")

    import rpa.excel

    rpa_6a4539_excel.close(save=True)

except Exception as e:
    visual_block.Visual_Block_Info("关闭Excel 文档", 17, 2, e)

    log.error("[%s] %s", "关闭Excel 文档", str(e))
    raise e

# -*- 退出程序
try:
    visual_block.Visual_Block_Info("退出程序", 18, 0, "正在执行")

    exit(0)

except Exception as e:
    visual_block.Visual_Block_Info("退出程序", 18, 2, e)

    log.error("[%s] %s", "退出程序", str(e))
    raise e

# -*- 流程结束
try:

    visual_block.Visual_Block_LastLine()

except Exception as e:
    log.error("[%s] %s", "流程结束", str(e))
