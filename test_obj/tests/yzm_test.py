
# name = u"\u8d26\u53f7\u672a\u8ba4\u8bc1"
# print(name.decode('unicode_escape'))
# a = name.encode('unicode_escape')
# print(a.decode('unicode_escape'))
a = '2019年03月09日'
#
a_list = ['开票日期：2019年03月09日','我的：你的']
b = []
for i in a_list:
    if i.split('：')[0] == '开票日期':
        import re
        a = ''.join(re.findall(r'\d+', i.split('：')[1]))
        print(a)
        b.append(a)
        continue
    b.append("'" + i.split('：')[1])
print(b)
# import re
# ''.join(re.findall(r'\d+',a))
# print(b)
# print(name.encode().decode('unicode_escape'))


# import re
# s = '2019年3月20日'
# s_list = re.findall(r'\d+', s)
# if len(s_list[1]) == 1:
#     s_list[1] = '0' + s_list[1]
# if len(s_list[2]) == 1:
#     s_list[2] = '0' + s_list[2]
# date_fin = [s_list[0] + s_list[1] + s_list[2]]
# print date_fin

# a = [1,2,3,4]
# b = [2,1,3,4]
# if a == b:
#     print 111
import json

# a = ['051001600111', '85345640', '2019\xe5\xb9\xb403\xe6\x9c\x8820\xe6\x97\xa5', '13686533700202252336', '218.22', '\xe6\x88\x90\xe9\x83\xbd\xe5\x86\x9c\xe6\x9d\x91\xe5\x95\x86\xe4\xb8\x9a\xe9\x93\xb6\xe8\xa1\x8c\xe8\x82\xa1\xe4\xbb\xbd\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb8', None, '\xe5\x9b\xbd\xe7\xbd\x91\xe5\x9b\x9b\xe5\xb7\x9d\xe7\x9c\x81\xe7\x94\xb5\xe5\x8a\x9b\xe5\x85\xac\xe5\x8f\xb8\xe5\xa4\xa7\xe8\x89\xb2\xe5\x8e\xbf\xe4\xbe\x9b\xe7\x94\xb5\xe5\x88\x86\xe5\x85\xac\xe5\x8f\xb8', None]
# for i in a:
#     i = i.encode('string_escape')
#     print(i)
# print('%.2f' % float(a[4]))
# a = json.dumps('哈哈',ensure_ascii=True)
# b = json.loads(a)
# print(a)
# print(b)

# file_list = [1,1,2,2,1,1]
# a = file_list[:]
# for i, v in enumerate(file_list[:]):
#     # print(i)
#     if v == 1:
#         file_list.remove(v)
#         print(file_list)

# a = [1,2,3]
# b = [4,5,6]
#
# for i,v in zip(a,b):
#     print(i)
#     print(v)
# -*- coding:utf-8 -*-

# from rpa import Chrome, IE, log, ChromeOptions, update_panel
# from rpa.visual_block.visual_block import VisualBlock
# import sys, os
#
# __taskId=None
# try:
#     import getopt
#     opts, _ = getopt.getopt(sys.argv[2:], '-h-t:', ['help', 'taskId='])
#     for k, v in opts:
#         if k in ('-t', '--taskId'):
#             __taskId = v
# except Exception as e:
#     pass
# try:
#     import pywinauto
# except:
#     pass
#
# visual_block = VisualBlock(taskId=__taskId)
# visual_block.Visual_Block_Total_Block(14)
#
# # -*- 参数面板
# try:
#
#     PANEL_VARS = {
#     }
#
# except Exception as e:
#     log.error("[%s] %s", "参数面板", str(e))
#
# # -*- 传入的JSON
# try:
#
#     update_panel(sys.argv,PANEL_VARS)
#
# except Exception as e:
#     log.error("[%s] %s", "传入的JSON", str(e))
#
#
# # -*- yzm
# try:
#     visual_block.Visual_Block_Info("yzm", 1, 0, "正在执行")
#
#     # coding=utf-8
#     import os,sys
#     import hashlib
#     import time
#     import json
#     import requests
#     import base64
#     FATEA_PRED_URL  = "http://pred.fateadm.com"
#     def LOG(log):
#         # 不需要测试时，注释掉日志就可以了
#         print(log)
#         log = None
#     class TmpObj():
#         def __init__(self):
#             self.value  = None
#     class Rsp():
#         def __init__(self):
#             self.ret_code   = -1
#             self.cust_val   = 0.0
#             self.err_msg    = "succ"
#             self.pred_rsp   = TmpObj()
#         def ParseJsonRsp(self, rsp_data):
#             if rsp_data is None:
#                 self.err_msg     = "http request failed, get rsp Nil data"
#                 return
#             jrsp                = json.loads( rsp_data)
#             self.ret_code       = int(jrsp["RetCode"])
#             self.err_msg        = jrsp["ErrMsg"]
#             self.request_id     = jrsp["RequestId"]
#             if self.ret_code == 0:
#                 rslt_data   = jrsp["RspData"]
#                 if rslt_data is not None and rslt_data != "":
#                     jrsp_ext    = json.loads( rslt_data)
#                     if "cust_val" in jrsp_ext:
#                         data        = jrsp_ext["cust_val"]
#                         self.cust_val   = float(data)
#                     if "result" in jrsp_ext:
#                         data        = jrsp_ext["result"]
#                         self.pred_rsp.value     = data
#     def CalcSign(pd_id, passwd, timestamp):
#         md5     = hashlib.md5()
#         md5.update((timestamp + passwd).encode())
#         csign   = md5.hexdigest()
#         md5     = hashlib.md5()
#         md5.update((pd_id + timestamp + csign).encode())
#         csign   = md5.hexdigest()
#         return csign
#     def CalcCardSign(cardid, cardkey, timestamp, passwd):
#         md5     = hashlib.md5()
#         md5.update(passwd + timestamp + cardid + cardkey)
#         return md5.hexdigest()
#     def HttpRequest(url, body_data, img_data=""):
#         rsp         = Rsp()
#         post_data   = body_data
#         files       = {
#             'img_data':('img_data',img_data)
#         }
#         header      = {
#                 'User-Agent': 'Mozilla/5.0',
#                 }
#         rsp_data    = requests.post(url, post_data,files=files ,headers=header)
#         rsp.ParseJsonRsp( rsp_data.text)
#         return rsp
#     class FateadmApi():
#         # API接口调用类
#         # 参数（appID，appKey，pdID，pdKey）
#         def __init__(self, app_id, app_key, pd_id, pd_key):
#             self.app_id     = app_id
#             if app_id is None:
#                 self.app_id = ""
#             self.app_key    = app_key
#             self.pd_id      = pd_id
#             self.pd_key     = pd_key
#             self.host       = FATEA_PRED_URL
#         def SetHost(self, url):
#             self.host       = url
#         #
#         # 查询余额
#         # 参数：无
#         # 返回值：
#         #   rsp.ret_code：正常返回0
#         #   rsp.cust_val：用户余额
#         #   rsp.err_msg：异常时返回异常详情
#         #
#         def QueryBalc(self):
#             tm      = str( int(time.time()))
#             sign    = CalcSign( self.pd_id, self.pd_key, tm)
#             param   = {
#                     "user_id": self.pd_id,
#                     "timestamp":tm,
#                     "sign":sign
#                     }
#             url     = self.host + "/api/custval"
#             rsp     = HttpRequest(url, param)
#             if rsp.ret_code == 0:
#                 LOG("query succ ret: {} cust_val: {} rsp: {} pred: {}".format( rsp.ret_code, rsp.cust_val, rsp.err_msg, rsp.pred_rsp.value))
#             else:
#                 LOG("query failed ret: {} err: {}".format( rsp.ret_code, rsp.err_msg.encode('utf-8')))
#             return rsp
#         #
#         # 查询网络延迟
#         # 参数：pred_type:识别类型
#         # 返回值：
#         #   rsp.ret_code：正常返回0
#         #   rsp.err_msg： 异常时返回异常详情
#         #
#         def QueryTTS(self, pred_type):
#             tm          = str( int(time.time()))
#             sign        = CalcSign( self.pd_id, self.pd_key, tm)
#             param       = {
#                     "user_id": self.pd_id,
#                     "timestamp":tm,
#                     "sign":sign,
#                     "predict_type":pred_type,
#                     }
#             if self.app_id != "":
#                 #
#                 asign       = CalcSign(self.app_id, self.app_key, tm)
#                 param["appid"]     = self.app_id
#                 param["asign"]      = asign
#             url     = self.host + "/api/qcrtt"
#             rsp     = HttpRequest(url, param)
#             if rsp.ret_code == 0:
#                 LOG("query rtt succ ret: {} request_id: {} err: {}".format( rsp.ret_code, rsp.request_id, rsp.err_msg))
#             else:
#                 LOG("predict failed ret: {} err: {}".format( rsp.ret_code, rsp.err_msg.encode('utf-8')))
#             return rsp
#         #
#         # 识别验证码
#         # 参数：pred_type:识别类型  img_data:图片的数据
#         # 返回值：
#         #   rsp.ret_code：正常返回0
#         #   rsp.request_id：唯一订单号
#         #   rsp.pred_rsp.value：识别结果
#         #   rsp.err_msg：异常时返回异常详情
#         #
#         def Predict(self, pred_type, img_data, head_info = ""):
#             tm          = str( int(time.time()))
#             sign        = CalcSign( self.pd_id, self.pd_key, tm)
#             param       = {
#                     "user_id": self.pd_id,
#                     "timestamp": tm,
#                     "sign": sign,
#                     "predict_type": pred_type,
#                     "up_type": "mt"
#                     }
#             if head_info is not None or head_info != "":
#                 param["head_info"] = head_info
#             if self.app_id != "":
#                 #
#                 asign       = CalcSign(self.app_id, self.app_key, tm)
#                 param["appid"]     = self.app_id
#                 param["asign"]      = asign
#             url     = self.host + "/api/capreg"
#             files = img_data
#             rsp     = HttpRequest(url, param, files)
#             if rsp.ret_code == 0:
#                 LOG("predict succ ret: {} request_id: {} pred: {} err: {}".format( rsp.ret_code, rsp.request_id, rsp.pred_rsp.value, rsp.err_msg))
#             else:
#                 LOG("predict failed ret: {} err: {}".format( rsp.ret_code, rsp.err_msg))
#                 if rsp.ret_code == 4003:
#                     #lack of money
#                     LOG("cust_val <= 0 lack of money, please charge immediately")
#             return rsp
#         #
#         # 从文件进行验证码识别
#         # 参数：pred_type;识别类型  file_name:文件名
#         # 返回值：
#         #   rsp.ret_code：正常返回0
#         #   rsp.request_id：唯一订单号
#         #   rsp.pred_rsp.value：识别结果
#         #   rsp.err_msg：异常时返回异常详情
#         #
#         def PredictFromFile( self, pred_type, file_name, head_info = ""):
#             with open(file_name, "rb") as f:
#                 data = f.read()
#             return self.Predict(pred_type,data,head_info=head_info)
#         #
#         # 识别失败，进行退款请求
#         # 参数：request_id：需要退款的订单号
#         # 返回值：
#         #   rsp.ret_code：正常返回0
#         #   rsp.err_msg：异常时返回异常详情
#         #
#         # 注意:
#         #    Predict识别接口，仅在ret_code == 0时才会进行扣款，才需要进行退款请求，否则无需进行退款操作
#         # 注意2:
#         #   退款仅在正常识别出结果后，无法通过网站验证的情况，请勿非法或者滥用，否则可能进行封号处理
#         #
#         def Justice(self, request_id):
#             if request_id == "":
#                 #
#                 return
#             tm          = str( int(time.time()))
#             sign        = CalcSign( self.pd_id, self.pd_key, tm)
#             param       = {
#                     "user_id": self.pd_id,
#                     "timestamp":tm,
#                     "sign":sign,
#                     "request_id":request_id
#                     }
#             url     = self.host + "/api/capjust"
#             rsp     = HttpRequest(url, param)
#             if rsp.ret_code == 0:
#                 LOG("justice succ ret: {} request_id: {} pred: {} err: {}".format( rsp.ret_code, rsp.request_id, rsp.pred_rsp.value, rsp.err_msg))
#             else:
#                 LOG("justice failed ret: {} err: {}".format( rsp.ret_code, rsp.err_msg.encode('utf-8')))
#             return rsp
#         #
#         # 充值接口
#         # 参数：cardid：充值卡号  cardkey：充值卡签名串
#         # 返回值：
#         #   rsp.ret_code：正常返回0
#         #   rsp.err_msg：异常时返回异常详情
#         #
#         def Charge(self, cardid, cardkey):
#             tm          = str( int(time.time()))
#             sign        = CalcSign( self.pd_id, self.pd_key, tm)
#             csign       = CalcCardSign(cardid, cardkey, tm, self.pd_key)
#             param       = {
#                     "user_id": self.pd_id,
#                     "timestamp":tm,
#                     "sign":sign,
#                     'cardid':cardid,
#                     'csign':csign
#                     }
#             url     = self.host + "/api/charge"
#             rsp     = HttpRequest(url, param)
#             if rsp.ret_code == 0:
#                 LOG("charge succ ret: {} request_id: {} pred: {} err: {}".format( rsp.ret_code, rsp.request_id, rsp.pred_rsp.value, rsp.err_msg))
#             else:
#                 LOG("charge failed ret: {} err: {}".format( rsp.ret_code, rsp.err_msg.encode('utf-8')))
#             return rsp
#         ##
#         # 充值，只返回是否成功
#         # 参数：cardid：充值卡号  cardkey：充值卡签名串
#         # 返回值： 充值成功时返回0
#         ##
#         def ExtendCharge(self, cardid, cardkey):
#             return self.Charge(cardid,cardkey).ret_code
#         ##
#         # 调用退款，只返回是否成功
#         # 参数： request_id：需要退款的订单号
#         # 返回值： 退款成功时返回0
#         #
#         # 注意:
#         #    Predict识别接口，仅在ret_code == 0时才会进行扣款，才需要进行退款请求，否则无需进行退款操作
#         # 注意2:
#         #   退款仅在正常识别出结果后，无法通过网站验证的情况，请勿非法或者滥用，否则可能进行封号处理
#         ##
#         def JusticeExtend(self, request_id):
#             return self.Justice(request_id).ret_code
#         ##
#         # 查询余额，只返回余额
#         # 参数：无
#         # 返回值：rsp.cust_val：余额
#         ##
#         def QueryBalcExtend(self):
#             rsp = self.QueryBalc()
#             return rsp.cust_val
#         ##
#         # 从文件识别验证码，只返回识别结果
#         # 参数：pred_type;识别类型  file_name:文件名
#         # 返回值： rsp.pred_rsp.value：识别的结果
#         ##
#         def PredictFromFileExtend( self, pred_type, file_name, head_info = ""):
#             rsp = self.PredictFromFile(pred_type,file_name,head_info)
#             return rsp.pred_rsp.value
#         ##
#         # 识别接口，只返回识别结果
#         # 参数：pred_type:识别类型  img_data:图片的数据
#         # 返回值： rsp.pred_rsp.value：识别的结果
#         ##
#         def PredictExtend(self,pred_type, img_data, head_info = ""):
#             rsp = self.Predict(pred_type,img_data,head_info)
#             return rsp.pred_rsp.value
#
# except Exception as e:
#     visual_block.Visual_Block_Info("yzm", 1, 2, e)
#
#     log.error("[%s] %s", "yzm", str(e))
#     raise e
#
# # -*- 新建 Excel 文档
# try:
#     visual_block.Visual_Block_Info("新建 Excel 文档", 2, 0, "正在执行")
#
#     import rpa.excel
#     rpa_6a4539_excel = rpa.excel.create(True, True)
#
# except Exception as e:
#     visual_block.Visual_Block_Info("新建 Excel 文档", 2, 2, e)
#
#     log.error("[%s] %s", "新建 Excel 文档", str(e))
#     raise e
# a = ["'011001900111", "'47240378", "'2019年05月21日", "'58180484432941029728", "'158.90", "'达而观信息科技(上海)有限公司", "'91310000341984589Y", "'中国移动通信集团北京有限公司", "'91110000722611700L"]
# b = ["'011001900111", "'47240378", "'2019年05月21日", "'58180484432941029728", "'158.90", "'达而观信息科技(上海)有限公司", "'91310000341984589Y", "'中国移动通信集团北京有限公司", "'91110000722611700L"]
#
# # import re
# # 才 = b[5].replace(r'（','(').replace(r'）',')')
# # print(b)
# # print(才)
# if a==b:
#     print(1111)
#     # import rpa.excel
#     # rpa_6a4539_excel.get_sheet("").write("B" + str(2), '结果错误')

# a = [1,1,1,1]
# b = [2,2,2,2]

# c = [1,1,1,1]
# d = [2,2,2,2]
# e = zip(a,c)
# f = zip(b,d)
# print(list(zip(e,f)))
# for i in zip(e,f):
    # if i[0] == i[1]:
    #     if v[0] == v[1]:
    #         pass
    #     else:
    #         pass
    # print(i)

# import re
# a = '订单WZGZNB,网银在线(北京)科技有限公司'
# pay_nums = str(re.search(r'\d+',a).group())
# print(pay_nums)
# b = '0'+str(int(5861734.0))
# print(b)
# d = '%.2f' % float(699.97)
# print(d)
# if pay_nums != '0'+str(5861734.0):
#     continue
# else:
#     if '%.2f' % float(c_list[4]) == '%.2f' % float(b_list[1]):
#         pass
