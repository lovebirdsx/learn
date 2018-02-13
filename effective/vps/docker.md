# Docker

## 安装

- 提示以下信息导致安装不成功

> No default Boot2Docker ISO found locally, downloading the latest release...

Download the *boot2docker.iso* file manually by going to <https://api.github.com/repos/boot2docker/boot2docker/releases/latest> then clicking on the *html_url* and finally choosing to download the file.

Once you get the file go and place it manually in */Users/{user}/.docker/machine/cache/*

Finally re-run this command `docker-machine create --driver virtualbox default`

## 镜像

- virtualbox的默认用户名和密码: docker tcuser
- 添加阿里云镜像加速器地址: 打开~/.docker下对应的machine目录,将阿里云的个人独有极速器地址添加到config.json中的"RegistryMirror"字段中
- 镜像操作
  - 移除: `docker image rm [name]`
  - 列举: `docker images`
  - 查找: `docker search [name]`
  - 提交: `docker commit [选项] <容器ID或容器名> [<仓库名>[:<标签>]]`
    ``` Shell
    docker commit \
        --author "Tao Wang <twang2218@gmail.com>" \
        --message "修改了默认网页" \
        webserver \
        nginx:v2
    ```
  - 查看修改: `docker diff [name]`
  - 删除tag为none的景象: `docker images|grep none|awk '{print $3}'|xargs docker rmi`

## 容器

- 容器操作
  - 运行容器:
    - `docker run --name [container name] -d -p 80:80 [name]`
    - `docker run -t -i lovebirdsx/rayline /bin/bash`
  - 恢复容器: `docker start [container name]`
  - 进入容器: `docker exec -it [container name] bash`
  - 终止容器: `docker stop [container name]`
  - 删除所有已经停止的容器 `docker rm $(docker ps -a -q)`
  - 停止所有正在运行的容器  `docker kill $(docker ps -q)`

## 其它

- 重启服务 `service docker restart`

## 构建

- 在Dockerfile所在的目录执行: `docker build -t [image name] .`
> 注意后面的*.*