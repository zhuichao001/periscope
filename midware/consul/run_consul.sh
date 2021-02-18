#! /bin/bash
/usr/local/bin/consul agent -dev -ui -client=0.0.0.0 -data-dir=/var/run/consul/ -log-file=/var/log/consul.log -pid-file=/var/run/consul.pid 
