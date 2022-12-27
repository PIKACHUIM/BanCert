# -------------------------------------
#       禁用并吊销选中的证书模块
# -------------------------------------
import os


# 禁用证书模块 ----------------------------------------------------------------------------------------
def ban_cert(in_path, in_name, log=None, processbar=None, size=1):
    name_list = os.listdir(in_path)
    lens = 0
    size = 1 if size <= 0 else size
    for name_item in name_list:
        # 进度条操作
        if processbar is not None:
            lens = lens + 1
            processbar['value'] = lens * 100 / size
        if name_item in in_name:
            subs_path = os.path.join(in_path, name_item)
            try:
                subs_name = os.listdir(subs_path)
            except NotADirectoryError:
                continue
            for subs_item in subs_name:
                if subs_item.find("cer") > 0:
                    cert_path = os.path.join(subs_path, subs_item)
                    result = os.popen("certutil -addstore -user -f \"Disallowed\" \"" + cert_path + "\"").read()
                    if log is not None:
                        log.log(result.replace("\n", " "))
