# -------------------------------------
#          获取并上传证书信息
# -------------------------------------
import os


def cuts(in_data):
    temp = ""
    for item in in_data.split(","):
        if len(temp) > 45:
            temp = temp + ",..."
            break
        else:
            if item != "":
                if temp != "":
                    temp = temp + ","
                temp = temp + item
    if temp == "":
        temp = "None"
    return temp


# 读取信息 ----------------------------------------------------
def dump(file_path, log=None):
    result = os.popen("certutil -dump " + file_path).read()
    result.replace("\n", "")
    data = dict()
    # 证书名称 ------------------------------------------------
    data['name'] = result.find("使用者")
    data['name'] = result[data['name'] + 11:]
    data['name'] = data['name'].split("\n")[0].replace("=", "")
    data['org'] = result.find("使用者")
    data['org'] = result[data['org']:]
    data['org'] = data['org'].split("\n")[2].split("=")[1]
    # 颁发者 --------------------------------------------------
    data['supper'] = result.find("颁发者")
    data['supper'] = result[data['supper'] + 11:]
    data['supper'] = data['supper'].split("\n")[0]
    data['supper'] = data['supper'].replace("=", "")
    # 证书编号 ------------------------------------------------
    data['id'] = result.find("序列号")
    data['id'] = result[data['id'] + 5:].split("\n")[0]
    # 证书时效 ------------------------------------------------
    data['start'] = result.find("NotBefore")
    data['start'] = result[data['start'] + 11:].split("\n")[0]
    data['ends'] = result.find("NotAfter")
    data['ends'] = result[data['ends'] + 10:].split("\n")[0]
    # 证书算法 ------------------------------------------------
    data['encryption'] = result.find("签名算法:")
    data['encryption'] = result[data['encryption'] + 44:]
    data['encryption'] = data['encryption'].split("\n")[0]
    data['encryption'] = data['encryption'].replace(" ", "")
    data['public'] = result.find("公钥算法:")
    data['public'] = result[data['public'] + 44:]
    data['public'] = data['public'].split("\n")[0]
    data['public'] = data['public'].replace(" ", "")
    # 版本和用法 ----------------------------------------------
    data['v'] = result.find("版本")
    data['v'] = result[data['v']:].split(":")[1].split("\n")[0]
    data['usage'] = result.find("密钥用法")
    data['usage'] = result[data['usage']:].split("\n")[1]
    data['usage'] = data['usage'].replace(" ", "")
    data['usage'] = cuts(data['usage'])
    data['extend'] = result.find("增强型密钥用法")
    data['extend'] = result[data['extend']:].split("\n")[1]
    data['extend'] = data['extend'].replace(" ", "")
    data['extend'] = cuts(data['extend'])
    # 证书哈希sha1 ---------------------------------------------
    data['hash'] = result.find("证书哈希(sha1)")
    data['hash'] = result[data['hash']:].split(":")[1]
    data['hash'] = data['hash'].split("\n")[0]
    return data


if __name__ == '__main__':
    dump("C:\\Users\\Pika\\Desktop\\banlist\\test2.cer")
