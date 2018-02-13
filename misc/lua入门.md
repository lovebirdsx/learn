# lua入门

## 准备工作

通过下面几个东西的安装,就可以搭建好lua的运行和编辑环境

- 安装[lua for windows](http://files.luaforge.net/releases/luaforwindows/luaforwindows/5.1.4-35)
- 安装[vs code](https://code.visualstudio.com/download)
- 在vs code安装插件Code Runner和LuaIde

## 建议

下面的操作是为了方便做版本管理,之后在公司也可以看

- 安装[git for windows](https://git-scm.com/download/win)
- 将.ssh目录(注意是目录)直接拷贝到你的用户目录,一般是 C:\Users\用户名,这一步之后,你就可以针对我给你建的lua版本库进行提交
- 右键某个目录(譬如:E\git_project),选择Git Bash Here,从而打开git命令行
- 克隆目录:在命令行中输入 ```git clone git@github.com:lovebirdsx/yutao_test.git```
- 注: 下面的用户名和邮件你可以按照自己的喜好来配置
- 配置git用户名: ```git config --global user.name "Yu Tao"```
- 配置git邮件: ```git config --global user.email tanyutao@ejoy.com```

## 测试方法

- 在yutao_test目录右键Git Bash Here
- 输入 code .
- 随便新建lua文件测试吧
- 通过ctrl+alt+n来运行

## 提交步骤

- 在yutao_test目录右键Git Bash Here
- 在git bash中依次输入:

``` git
git add .
git commit -m '你的提交信息'
git push
```