#! /bin/bash
if [[ $1 != 'start' ]] && [[ $1 != 'stop' ]]; then
  echo 'usage: ./script/run_controller.sh [start|stop]'
else
  python3 -m cmd.controller.main $1
fi

