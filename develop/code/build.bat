RAM ������pyinstaller��ִ���ļ�λ��
set pyinstaller="E:\Venv\BanCerts\Scripts\pyinstaller.exe"
set file_path="%temp%\ban-cert\build\%date:~0,4%%date:~5,2%%date:~8,2%0%time:~1,1%%time:~3,2%%time:~6,2%"
@echo off
color 3f
title PyInstaller��������
mode con lines=20 cols=50
echo.
echo.
echo.
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~       ***��������Ȩ��***       �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo.
echo.
echo          ***�����ʾ��Ȩ���������ǡ�***         
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
cls
echo.
echo.
echo.
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~       ***���ڹ�������***       �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo.
mkdir %file_path%
cd %file_path%
%pyinstaller% --clean -D "%~dp0\main.py" -F --workpath="%file_path%" --distpath="%file_path%\dist" --specpath="%file_path%"
rd /s /q __pycache__
explorer "%file_path%\dist"
timeout /t 600