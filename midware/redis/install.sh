
#build redis
yum install systemd-devel

#rebuild redis-server and install

#prepare systemd.service
#path: /etc/systemd/system/redis.service

systemctl deamon-reload
systemctl enable redis
systemctl restart redis
systemctl status redis
