# Git Effective

## git假设服务器经验

[参考](https://git-scm.com/book/zh/v1/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-%E6%9E%B6%E8%AE%BE%E6%9C%8D%E5%8A%A1%E5%99%A8)

- 注意: 通过类似以下命令来添加公共密钥,手动拷贝有可能有问题

``` Shell
cat /tmp/id_rsa.john.pub >> ~/.ssh/authorized_keys
```

## git rebase 做了什么

[链接](http://gitbook.liuhui998.com/4_2.html)

## rebase冲突处理

> 注意:
> --ours表示HEAD,也就是远端的版本
> --theirs表示自己的版本

``` Shell
git checkout --theirs file_path
git add file_path
git rebase --continue
```

## 删除缓存的远程分支列表

`git remote prune origin`

## Git 别名

windows下的文件位置: `C:\Program Files\Git\etc\bash.bashrc`

``` Shell
alias gs='git status'
alias ga='git add'
alias gb='git branch '
alias gc='git commit -a -m'
alias gd='git diff'
alias go='git checkout '
alias gk='gitk --all'
alias gg='git gui'
alias gf='git fetch'
alias gl='git pull'
alias glr='git pull --rebase'
alias gh='git push'
alias gr='git rebase'
alias g='git'
alias glog='git log --pretty=format:"%ad %s%d [%an]" --date=format:%m%d-%H:%M'
alias glm='git log --pretty=format:"%ad %s%d [%an]" --date=format:%m%d-%H:%M --author=lovebirdsx'
```

## 查看某个用户的提交记录

- [文档](https://git-scm.com/docs/git-log)
- [strftime](http://www.cplusplus.com/reference/ctime/strftime/)
- [参考](https://ruby-china.org/topics/939)

示例:

- `git log --author=lovebird --pretty=format:"%h %ad | %s%d" --date=short`

## 查看某个文件的提交记录

`gitk file_path`

## git submodule使用方法

[参考](https://segmentfault.com/a/1190000003076028), 几个关键点:

- 主项目只是存储了子项目中的某个提交点
- 子项目内容不会自动跟随主项目的pull而pull,而需要手动pull

## git 查看哪些分支包含哪个提交

`git branch --contains <commit>`