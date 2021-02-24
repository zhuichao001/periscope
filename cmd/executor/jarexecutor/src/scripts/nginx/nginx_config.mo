upstream {{PROXY_NAME}} {
    server 127.0.0.1:{{PORT}}  weight=10 max_fails=2 fail_timeout=30s;
}

server {
    listen                   80;
    server_name              {{DOMAIN}};
    access_log               {{NGINX_LOG_PATH}}/{{DOMAIN}}/{{DOMAIN}}_access.log main;
    error_log                {{NGINX_LOG_PATH}}/{{DOMAIN}}/{{DOMAIN}}_error.log warn;
    error_page 411 = @my_error;
    location / {
        lua_need_request_body   on;
        proxy_next_upstream     http_500 http_502 http_503 http_504 error timeout invalid_header;
        proxy_set_header        Host  $host;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass              http://{{PROXY_NAME}};
        expires                 1d;
    }
}
