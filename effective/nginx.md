# nginx

- [windows help](http://nginx.org/en/docs/windows.html)
- [windows 配置nginx服务器](http://blog.csdn.net/revolver/article/details/50465636)
- [fastcgi简单指引](http://nginx.org/en/docs/beginners_guide.html#fastcgi)
- [Python WSGI初探](http://liaoph.com/python-wsgi/)

## fastcfg 配置

``` Conf
server {
    #nginx服务端口
    listen  8000;
    server_name test.com; 
    location /{
        #python server的端口
        fastcgi_pass  127.0.0.1:8008;
        fastcgi_param SCRIPT_FILENAME "";
        fastcgi_param PATH_INFO $fastcgi_script_name;
        include fastcgi.conf;
    }
}
```

## Ubuntu

- 配置文件： etc/nginx/nginx.conf
- www主目录：var/www/html
