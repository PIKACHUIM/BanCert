@echo off
color 3f
title Ƥ����֤�����ι���
mode con lines=20 cols=50
echo.
echo.
echo.
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~        Ƥ�����б����ɹ���      �~
echo        �~                                �~
echo        �~        ***������������***      �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo.
echo.
cd ..
cd banlist
dir /b /n /on >..\getlist\info.ini
cd ..
cd getlist
(for /f "delims=" %%a in (info.ini) do echo https://pikachuim.coding.net/p/pika-cod-pro-codings/d/BanCerts/git/raw/master/banlist/%%a)>$
move /y $ info.ini
