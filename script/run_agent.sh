#! /bin/bash

if [ ! -d output ];then
  mkdir output
fi

#nohup python3 -m cmd.agent.main near &>output/periscope_agent.log &
python3 -m cmd.agent.main near 
#python3 -m cmd.agent.main remote
