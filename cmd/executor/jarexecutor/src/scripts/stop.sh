#!/bin/bash
# STOP DEMO
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
function check_instance
{
    pgrep -lf "${build.finalName}.jar" >/dev/null  # 注意此处instance_pattern不要只写应用名,会把系统启动脚本也杀掉的
}
function stop_instance
{
    local -i retry=0
    if ! check_instance; then
        echo "WARNING: instance process not found, nothing to stop" >&2
        exit 0
    fi
    pkill -f "${build.finalName}.jar" # 注意此处instance_pattern不要只写应用名,会把系统启动脚本也杀掉的
    while (( retry < 20 )); do
        if ! check_instance; then
            echo "Instance stopped successfully"
            return
        else
            echo -n "."
            sleep 0.5
            retry=$(( $retry + 1 ))
        fi
    done
    echo "ERROR: instance process still alive, sending SIGKILL ..." >&2
    pkill -9 -f "${build.finalName}.jar" # 注意此处instance_pattern不要只写应用名,会把系统启动脚本也杀掉的
    exit $?
}
stop_instance