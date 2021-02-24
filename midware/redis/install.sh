#rebuild redis-server and install

yum install systemd-devel

#build redis
cp redis.service redis2.service /usr/lib/systemd/system/
systemctl daemon-reload
systemctl start redis
systemctl start redis2
systemctl enable redis
systemctl enable redis2
