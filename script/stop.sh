python3 -m common.consul
ps -ef | grep python3 | awk '{print $2}' | xargs kill -9
