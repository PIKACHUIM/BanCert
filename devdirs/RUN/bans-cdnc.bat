@echo off
color 3f
title 皮卡丘流氓软件屏蔽工具
mode con lines=30 cols=50
set targe=''
setlocal enabledelayedexpansion


echo.
echo.
echo.
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo        ▇                                ▇
echo        ▇        皮卡丘流氓软件屏蔽      ▇
echo        ▇                                ▇
echo        ▇        ***正在申请权限***      ▇
echo        ▇                                ▇
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo.
echo.
echo          ***如果提示授权，请点击【是】***         
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"



color 8f
cls
echo.
echo.
echo.
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo        ▇                                ▇
echo        ▇       ***正在获取列表***       ▇
echo        ▇                                ▇
echo        ▇           请耐心等待           ▇
echo        ▇                                ▇
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo.
echo.
%~dp0wget.exe https://cdnc-dat.99pika.com/Bancert/info-cdnc.ini
mkdir cert
cd cert



for /f   %%i in (..\info-cdnc.ini)  do (
color cf
cls
echo.
echo.
echo.
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo        ▇                                ▇
echo        ▇       ***正在下载证书***       ▇
echo        ▇                                ▇
echo        ▇           请耐心等待           ▇
echo        ▇                                ▇
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo.
echo.
set target=%%i
%~dp0wget.exe !target!
) 
for /R %%s in (.,*.cer) do (
cls
echo.
echo.
echo.
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo        ▇                                ▇
echo        ▇       ***正在执行操作***       ▇
echo        ▇                                ▇
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo.
echo.
certutil -addstore -user -f “Disallowed” %%s
)
cls
color 2f
echo.
echo.
echo.
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo        ▇                                ▇
echo        ▇     ***成功屏蔽流氓软件***     ▇
echo        ▇                                ▇
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
cd ..
del /q /f /q cer*
del /q /f /q info-cdnc*
rd /s/q cert
timeout /t 10

