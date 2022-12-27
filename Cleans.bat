rd /s /q Release\2.0.0
mkdir Release\2.0.0
xcopy /s /e /y build\exe.win-amd64-3.9\ Release\2.0.0\
xcopy /s /e /y Binrary\ Release\2.0.0\Binrary\
xcopy /s /e /y Asserts\ Release\2.0.0\Asserts\
rd /s /q build