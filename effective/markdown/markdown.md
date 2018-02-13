# Markdown

## markdown to pdf

- 安装 wkhtmltopdf
- 安装 pandoc
- 下载css文件，可以到网上找，也可以下载[这个](http://xiaoxiao.ejoy/css/markdown.css)
- vs code 中安装 Code Runner 插件
    - 在配置节："code-runner.executorMapByFileExtension"中加入：

``` Json
".md": "cd $dir && pandoc -s $fileName -o $fileNameWithoutExt.html && wkhtmltopdf --encoding utf-8 --user-style-sheet CSS_PATH $fileNameWithoutExt.html $fileNameWithoutExt.pdf && del $fileNameWithoutExt.html"
```

注意：将上面的CSS_PATH替换成你本地的css文件（上一部操作中下载的）路径

- 在vs code中编辑好markdown文件后，按ctrl+alt+n运行，将在对应目录下生成pdf文件
