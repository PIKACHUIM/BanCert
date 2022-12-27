# -*- coding: utf-8 -*-
import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = []

# TARGET
target = Executable(
    script="Client.py",
    base="Win32GUI",
    icon="Asserts/favicon.ico"
)

# SETUP CX FREEZE
setup(
    name="PC Software Code Signing Certificate Block Tool",
    copyright="https://github.com/PIKACHUIM/BanCert/raw/master/LICENSE",
    version="2.0.0",
    description="PC软件代码签名证书限制工具",
    author="Pikachu I.M. https://github.com/PIKACHUIM/BanCert",
    options={'build_exe': {'include_files': files}},
    executables=[target],
)
