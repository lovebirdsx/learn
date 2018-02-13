# Nginx

## 安装步骤

- `sudo apt-get install nginx`
- `vi /etc/nginx/sites-available/default`
    - location /rayline/ {
        alias /root/http_root/rayline/;
    }
- `vi /etc/nginx/nginx.conf`
    - 首行改成 `user root;`
- `service nginx restart`
