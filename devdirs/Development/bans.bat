::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCuDJGmW+0g1Kw9ofA2JPWiyE7wR1Mfr6uS3sEIOaMA+dqzeyKCdHOQW/EHtZ4UR33lVloUFDxQ4
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF65
::ZR41oxFsdFKZSTk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+IeA==
::cxY6rQJ7JhzQF1fEqQJgZkgaHUrSXA==
::ZQ05rAF9IBncCkqN+0xwdVsEAlfMbSXqZg==
::ZQ05rAF9IAHYFVzEqQIdKRdDTRaHfFi5FLAZ5uH16KqzrUIRNA==
::eg0/rx1wNQPfEVWB+kM9LVsJDCmDMHy7FLBc2+vp6u+Jq0MaFNYwd4O7
::fBEirQZwNQPfEVWB+kM9LVsJDCmDMHy7FLBc2+vp6u+Jq0MaFNYwd4O7
::cRolqwZ3JBvQF1fEqQK2/frSnPcK4aQ+3WOZOQdzGzcCdYiYsTVf
::dhA7uBVwLU+EWGmN/0MzIA4UeAGBNGW1Crob8ajY4KTL4mEJUII=
::YQ03rBFzNR3SWATExEs7KRhcWUS2OWiyCLoQ5+/ir8mI7AFdePY7GA==
::dhAmsQZ3MwfNWATExEs7KRhcWUS2OWiyCLoQ5+/ir8mI7AFdePY7GA==
::ZQ0/vhVqMQ3MEVWAtB9wGBJfTQeKKSuOA7YU5uf34O2e4m4SGq5/VJvfug==
::Zg8zqx1/OA3MEVWAtB9wGBJfTQeKKSuOA7YU5uf34O2e4m4SGq5/VJvfug==
::dhA7pRFwIByZRRkCIaO2+OjckcsG570/11qUHDV+OC8CR5p9
::Zh4grVQjdCuDJGmW+0g1Kw9ofA2JPWiyE7wR1Mfr6uS3sEIOaMA+dqzeyKCdHOQW/EHtZ4UR1HtUi4UJFB44
::YB416Ek+ZW8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
color 2f
title Ƥ����֤�����ι���
mode con lines=30 cols=50
set targe=''
setlocal enabledelayedexpansion


echo.
echo.
echo.
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~        Ƥ����֤�����ι���      �~
echo        �~                                �~
echo        �~        ***��������Ȩ��***      �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo.
echo.
echo          ***�����ʾ��Ȩ���������ǡ�***         
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"



color 6f
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
%~dp0wget.exe https://pikachuim.coding.net/p/pika-cod-pro-codings/d/BanCerts/git/raw/master/getlist/info.ini
mkdir cert
cd cert



for /f   %%i in (..\info.ini)  do (
color 5f
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
certutil -urlcache -split -f !target!
del /a /f /s /q  "*.crt"
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
echo.
echo.
echo.
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
echo        �~                                �~
echo        �~       ***�ɹ�����֤��***       �~
echo        �~                                �~
echo        �~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~�~
timeout /t 5

