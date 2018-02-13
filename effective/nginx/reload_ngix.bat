@echo off
REM 查看nginx是否已经在运行
REM tasklist /fi "imagename eq nginx.exe"

REM nginx -s stop	fast shutdown
REM nginx -s quit	graceful shutdown
REM nginx -s reload	changing configuration, starting new worker processes with a new configuration, graceful shutdown of old worker processes
REM nginx -s reopen	re-opening log files

nginx -v
nginx -s reload
