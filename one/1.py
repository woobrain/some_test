flag = True
for value in settlement_sheet_list:
    # 判断收款人与代理人存在一致
    agreement_a = "一致"
    agreement_b = "不一致"
    v1 = value[7].strip().replace("）", ")").replace("（", "(")
    v2 = value[3].strip().replace("）", ")").replace("（", "(")
    if skr_name != v1:
        error_log(document_number, "处理表格内容", "收款人与代理人存在不一致")
        log.info("收款人与代理人存在不一致")
        agreement_a = "不一致"
        flag = False
    # # 判断投保人与代理人存在一致
    elif v1 == v2:
        error_log(document_number, "处理表格内容", "投保人与代理人存在一致")
        log.info("投保人与代理人存在一致")
        agreement_b = "一致"
        flag = False

    bb_list.append(
        [PANEL_VARS.get('batch_number'), document_number, skr_name, v1, v2, "", agreement_a, agreement_b, ""])
    if not flag:
        break

if not flag:
    continue