@echo off
color 3f
title Ƥ������å������ι���
mode con lines=30 cols=50
set targe=''
setlocal enabledelayedexpansion


echo.
echo.
echo.
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~        Ƥ������å�������      �~
echo        �~                                �~
echo        �~        ***��������Ȩ��***      �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo.
echo.
echo          ***�����ʾ��Ȩ���������ǡ�***         
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"



color 8f
cls
echo.
echo.
echo.
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~       ***���ڻ�ȡ�б�***       �~
echo        �~                                �~
echo        �~           �����ĵȴ�           �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
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
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~       ***��������֤��***       �~
echo        �~                                �~
echo        �~           �����ĵȴ�           �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
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
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~       ***����ִ�в���***       �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo.
echo.
certutil -addstore -user -f ��Disallowed�� %%s
)
cls
color 2f
echo.
echo.
echo.
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~     ***�ɹ�������å���***     �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
cd ..
del /q /f /q cer*
del /q /f /q info-cdnc*
rd /s/q cert
timeout /t 10

