rd /s /q Release\2.0.0
mkdir Release\2.0.0
xcopy /s /e /y build\exe.win-amd64-3.9\ Release\2.0.0\
rd /s /q build