# SVN

- svn定时更新某个目录的方法

```Batch
set DIRS="G:\svn_project\LR\design\tools\wjsl"
set DIRS=%DIRS%;"G:\svn_project\LR\design\tools\yxsl"

CD C:\Program Files\TortoiseSVN\bin\
for %%d in (%DIRS%) do (
    TortoiseProc.exe /command:update /path:%%d /closeonend:1
)
```

``` Batch
svn up path_to_svn_dir
```

- [TortoiseProc参数说明](https://tortoisesvn.net/docs/nightly/TortoiseSVN_zh_CN/tsvn-automation.html)