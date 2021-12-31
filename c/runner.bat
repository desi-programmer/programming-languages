@echo off
@REM clear screen 
cls

IF "%~1" == "" ( 
    echo "Please input a file"
    exit 0
)
@REM compile it 
gcc %1 -o output
@REM run it 
output.exe
