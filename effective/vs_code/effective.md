# VS Code Effective

- 设置文件路径: C:\Users\lovebird\AppData\Roaming\Code\User\settings.json

## 快捷键

- 选中需要修改的内容后,ctrl+shift+l可以马上修改匹配的项
- ctrl+shift+0 折叠所有
- ctrl+shift+9 展开所有
- ctrl+x (没有选中内容) 剪切行
- ctrl+c (没有选中内容) 拷贝行

## 配置同步方法

- 安装syncing后，通过Syncing: Open Syncing Settings，填写token和gist id
- 然后通过Syncing: Upload Settings来同步
- 公司的网络有问题（可能是由于经过了代理服务器），可以通过连接手机的热点来同步
- 如果连接不到gist，可以通过修改host文件来实现
- 配置如下：

``` Json
{
    "token": "cbd42448ea08ff817a61a14de950d8befbaa5c88",
    "id": "f380966b253d63aaa7f80d5404b0b791"
}
```

## md->pdf

- 安装pandoc（在github上找最新版，官网的版本好像比较老）
- 安装whhtmltopdf
- 在coder runner的`code-runner.executorMapByFileExtension`的配置节中加入：

``` Json
".md": "cd $dir && pandoc -s $fileName -o $fileNameWithoutExt.html && wkhtmltopdf --encoding utf-8 --user-style-sheet C:\\Users\\lovebird\\git_project\\css\\markdown.css $fileNameWithoutExt.html $fileNameWithoutExt.pdf && del $fileNameWithoutExt.html"
```

其中 `C:\\Users\\lovebird\\git_project\\css\\markdown.css`是pdf的css配置

## todo+: 将时间日期格式改成更简单的方式

- 修改方法:
    - 在todo.js的`finish()`接口中进行如下修改:
        - `moment['preciseDiff'](startedDate, finishedDate)` -> `moment['preciseDiff'](startedDate, finishedDate, true)`
        - `${diff}` -> `${diff.hours + ":" + diff.minutes}`
    - [参考preciseDiff相关的说明](https://github.com/codebox/moment-precise-range)