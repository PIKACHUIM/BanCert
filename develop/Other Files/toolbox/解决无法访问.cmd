@echo off
color 3f
title Ƥ����Github��������
mode con lines=20 cols=50
echo.
echo.
echo.
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~      Ƥ����Github��������      �~
echo        �~                                �~
echo        �~        ***��������Ȩ��***      �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo.
echo.
echo          ***�����ʾ��Ȩ���������ǡ�***         
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
echo 199.232.68.133 raw.githubusercontent.com >>C:\Windows\System32\drivers\etc\hosts
pause