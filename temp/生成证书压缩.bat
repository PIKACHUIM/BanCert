@echo off
color 3f
title Ƥ����7ZIPѹ��֤�����ɹ���
mode con lines=20 cols=50
echo.
echo.
echo.
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~   Ƥ����7ZIPѹ��֤�����ɹ���   �~
echo        �~                                �~
echo        �~        ***��������Ȩ��***      �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo.
echo.
echo          ***�����ʾ��Ȩ���������ǡ�***         
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
echo "%~dp0"
pause
del /f /q getlist/7zip.7z
cmd /c 7za.exe a getlist/7zip.7z banlist/*
del /f /q temp/7za.exe
del /f /q temp/����֤��ѹ��.bat
rd temp
timeout /t 5