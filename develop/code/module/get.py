# -------------------------------------
#       下载并解压选中的证书模块
# -------------------------------------
import os
import hashlib
import requests


def get(url, log=None):
    try:
        html = requests.get(url)
    except requests.exceptions.MissingSchema as e:
        log.log("无法下载，错误: " + str(e), "GET")
        return None
    if html.status_code != 200:
        if log is not None:
            log.log("下载失败，错误: " + str(html.status_code), "GET")
            html.close()
    else:
        # 获取路径 -------------------------------------------------------
        path_text = "%temp%\\ban-cert\\"
        path_text = os.popen("echo " + path_text).read()
        path_text = path_text.replace("\n", "")
        # 创建文件夹 -----------------------------------------------------
        logs_text = "文件夹已经存在!!!!!!!"
        if not os.path.exists(path_text):
            logs_text = os.popen("mkdir " + path_text).read()
        if not os.path.exists(path_text + "\\download"):
            logs_text = os.popen("mkdir " + path_text + "\\download").read()
        if not os.path.exists(path_text + "\\cache"):
            logs_text = os.popen("mkdir " + path_text + "\\cache").read()
        data_file = html.content
        data_hash = hashlib.sha256(data_file)
        # 信息输出 -------------------------------------------------------
        if log is not None:
            if len(logs_text) > 2:
                log.log(logs_text, "GET")
            log.log("下载成功:" + str(data_hash.hexdigest()[:12]), "GET")
        # 文件写入 -------------------------------------------------------
        data_path = os.path.join(path_text, "download")
        data_path = os.path.join(data_path, data_hash.hexdigest() + ".zip")
        with open(data_path, "wb+") as file:
            file.write(data_file)
        # 文件解压 -------------------------------------------------------
        exec_path = os.path.join(path_text, "cache")
        exec_path = os.path.join(exec_path, data_hash.hexdigest())
        logs_text = os.popen("bin\\7za.exe x -y "
                             + data_path
                             + " -r -o"
                             + exec_path).read()
        if log is not None and logs_text != "":
            logs_temp = logs_text.replace(" ", "").split("\n")[-3:]
            for i in logs_temp:
                log.log(i, "GET")
        return exec_path


if __name__ == '__main__':
    get("https://tool.52pika.cn/zip.zip")
