# -------------------------------------
#       禁用并吊销选中的证书模块
# -------------------------------------
import os


# 禁用证书模块 ----------------------------------------------------------------------------------------
def ban_cert(in_path, in_name, log=None):
    name_list = os.listdir(in_path)
    for name_item in name_list:
        if name_item in in_name:
            subs_path = os.path.join(in_path, name_item)
            try:
                subs_name = os.listdir(subs_path)
            except NotADirectoryError:
                continue
            for subs_item in subs_name:
                if subs_item.find("cer") > 0:
                    cert_path = os.path.join(subs_path, subs_item)
                    result = os.popen("certutil -addstore -user -f \"Disallowed\" " + cert_path).read()
                    if log is not None:
                        log.log(result.replace("\n", " "))



