# ssh相关使用经验

## 调试方法

- 服务端

``` Shell
/home$/usr/sbin/sshd -d -p 2222
```

- 客户端

``` Shell
ssh git@119.23.58.223 -v -p 2222
```