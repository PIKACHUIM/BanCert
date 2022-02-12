# 设置窗体大小 ----------------------------------------------
$win=$Host.UI.RawUI.WindowSize
$win.Height=30
$win.Width=60
$Host.UI.RawUI.Set_windowsize($win)
# 提示信息 --------------------------------------------------
Write-Host ""
Write-Host ""
Write-Host "                ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"
Write-Host "                ⬛                          ⬛"
Write-Host "                ⬛   正在申请管理员权限     ⬛"
Write-Host "                ⬛       请点击[是]         ⬛"
Write-Host "                ⬛                          ⬛"
Write-Host "                ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"
Write-Host ""
Write-Host ""
# 自动提权 ---------------------------------------------------
If (-NOT ([Security.Principal.WindowsPrincipal]`
[Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(`
[Security.Principal.WindowsBuiltInRole]::Administrator))
{
  Start-Process powershell.exe "-NonInteractive `
  -WindowStyle Hidden -NoProfile -File",`
  ('"{0}"' -f $MyInvocation.MyCommand.Path) -Verb RunAs
  exit
}
# 允许脚本运行 ------------------------------------------------
set-ExecutionPolicy RemoteSigned
# 执行命令 ----------------------------------------------------
$certList = Get-ChildItem -Recurse $PSScriptRoot -Filter *.cer `
| Where { ! $_.PSIsContainer } | Select Name,FullName,Length
foreach ($cert in $certList) 
    {
        $certPrint = New-Object `
System.Security.Cryptography.X509Certificates.X509Certificate2
        $certPrint.Import($cert.FullName)
	certutil -user -delstore "Disallowed" $certPrint.Thumbprint
}
pause