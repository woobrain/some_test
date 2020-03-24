# -*- coding:utf-8 -*-
# a = '订单WZG05861734ZNB,网银在线(北京)科技有限公司'
# import re
# b = re.search(r'\d+',a)
# print type(b.group(0))


# a = None
# b = None
# if 'None' == None:
#     print 1111
# -*- coding:utf-8 -*-

# coding=utf-8
import base64
import os, sys
import hashlib
import time
import json
import requests

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


def TestFunc():
    pd_id = "119716"
    pd_key = "2KQkaJfgXBNuS08Pr5nbKX+qk1VzRoio"
    app_id = "302317"
    app_key = ""
    pred_type = "80400"
    api = FateadmApi(app_id, app_key, pd_id, pd_key)
    image_data = "data:image/png;base64,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"
    image_data = image_data.split(',')[1]
    color = json.dumps({'color': '02'})
    image_data = base64.b64decode(image_data)
    rsp = api.Predict(pred_type, image_data, color)
    r_id= rsp.request_id
    res= rsp.pred_rsp.value


if __name__ == "__main__":
    TestFunc()
