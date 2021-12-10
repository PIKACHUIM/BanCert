@echo off
color 3f
title 皮卡丘7ZIP压缩证书生成工具
mode con lines=20 cols=50
echo.
echo.
echo.
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo        ▇                                ▇
echo        ▇   皮卡丘7ZIP压缩证书生成工具   ▇
echo        ▇                                ▇
echo        ▇        ***正在申请权限***      ▇
echo        ▇                                ▇
echo        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
echo.
echo.
echo          ***如果提示授权，请点击【是】***         
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
echo "%~dp0"
pause
del /f /q getlist/7zip.7z
cmd /c 7za.exe a getlist/7zip.7z banlist/*
del /f /q temp/7za.exe
del /f /q temp/生成证书压缩.bat
rd temp
timeout /t 5