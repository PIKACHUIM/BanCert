# -*- coding: utf-8 -*-
import json
import os.path

from flask import Flask, request
import hashlib

app = Flask(__name__)


@app.route('/post', methods=["POST"])
def saveCerts():
    # 获取文件名称 -------------------------------------------------
    file_list = request.files
    file_cert = file_list['file']
    json_data = file_list['data'].read()
    json_data = json.loads(json_data)
    original_name = file_cert.filename
    contents_data = file_cert.read()
    storages_name = hashlib.new('sha1', contents_data).hexdigest()
    storages_path = os.path.join("Uploads", json_data['name'])
    storages_file = os.path.join(storages_path, storages_name + ".cer")
    print("原始名称:", original_name.replace(" ", ""))
    print("SHA1-FID:", storages_file)
    if os.path.isfile("Uploads"):
        os.remove("Uploads")
    if not os.path.exists("Uploads"):
        os.mkdir("Uploads")
    if not os.path.exists(storages_path):
        os.mkdir(storages_path)
    with open(storages_file, "wb") as save_file:
        save_file.write(contents_data)
    return '{"msg":"ok"}'


if __name__ == '__main__':
    app.run()
