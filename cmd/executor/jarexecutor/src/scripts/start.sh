#!/bin/bash
# START DEMO
#set -o errexit
set -o nounset
#The vars can be used
#--------------------------
# $def_app_id
# $def_app_name
# $def_app_domain
# $def_app_deploy_path
# $def_path_app_log
# $def_path_app_data
# $def_group_id
# $def_instance_id
# $def_instance_name
# $def_instance_path
# $def_host_ip
#--------------------------
#
export domain="testframework.jim.jd.local"
function check_instance
{
    pgrep -lf "${build.finalName}.jar" >/dev/null   # 注意此处instance_pattern不要只写应用名,会把系统启动脚本也杀掉的
}
function start_instance
{
    local -i retry=0
    if check_instance; then
        echo "ERROR: instance process has already been started" >&2
        exit 1
    fi

    BASEDIR=`dirname $0`/..
    BASEDIR=$(readlink -f `(cd "$BASEDIR"; pwd)`)

    cd ${BASEDIR}

    echo 'current path:' ${BASEDIR}

    sh ./bin/nginx/add_nginx.sh -d ${domain} -p 8080

    mkdir -p /dev/shm/nginx_temp/client_body
    sudo /export/servers/nginx/sbin/nginx
    sudo /export/servers/nginx/sbin/nginx -s reload

    IP=`ifconfig eth0 | grep "inet addr:" | awk -F":" '{print $2}' | awk '{print $1}'`
    JVM_M="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=52001 -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Djava.rmi.server.hostname=${IP}"

    mkdir -p /export/Logs/${domain}

    curl -s "http://pfinder-master.jd.com/access/script" -o /tmp/pfinder.sh ; source /tmp/pfinder.sh || :

    echo "JAVA_OPTS: ${JAVA_OPTS}"

    setsid java ${PFINDER_AGENT:-} -jar -server -Xms1024M -Xmx1024M ${JAVA_OPTS} -Dspring.profiles.active=prod ${JVM_M} lib/${build.finalName}.jar -XX:ErrorFile=/export/Logs/${domain}/hs_err.log > 0 > /export/Logs/${domain}/console.log &

    sleep 1
    while true; do
        if check_instance; then
            echo "Instance started successfully"
            break
        elif (( retry == 20 ));then
            echo "ERROR: starting up instance has timed out" >&2
            exit 1
        else
            echo -n "."
            sleep 0.5
            retry=$(( $retry + 1 ))
        fi
    done
}
start_instance