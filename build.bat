@echo off
pushd %cd%
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\VC\Auxiliary\Build\vcvarsall.bat" x64
popd
echo %cd%
set compilerflags=/Od /EHsc
set linkerflags=/OUT:%1.exe
cl.exe %compilerflags% %1.cpp /link %linkerflags%