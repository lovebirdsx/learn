@echo off
set DIRS="G:\svn_project\LR\design\tools\wjsl"
set DIRS=%DIRS%;"G:\svn_project\LR\design\tools\yxsl"

CD C:\Program Files\TortoiseSVN\bin\
for %%d in (%DIRS%) do (
    REM TortoiseProc.exe /command:update /path:%%d /closeonend:1
    svn up %%d
)
