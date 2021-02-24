#!/bin/sh

SCRIPT_DIR=`dirname $(readlink -f $0)`
TEMPLATE_FILE="$SCRIPT_DIR/nginx_config.mo"
MO="$SCRIPT_DIR/../lib/mo"

export NGINX_LOG_PATH="/export/servers/nginx/logs"
export NGINX_DOMAIN_CONF_PATH="/export/servers/nginx/conf/domains"

export DOMAIN=""
export PORT=""
export PROXY_NAME=""
DEBUG="false"

function usage ()
{
cat <<End-of-message
  Usage :  $0 [options] [--]

  Options:
  -h|help       Display this message
  -d|domain     Domain
  -n|proxy_name PROXY_NAME
  -p|port       Port
  -x|DEBUG      Show nginx result
End-of-message
}

while getopts "d:n:p:xh" opt
do
  case $opt in
    h|help      )  usage; exit 0          ;;
    d|domain    )  DOMAIN="$OPTARG"       ;;
    n|proxy_name)  PROXY_NAME="$OPTARG"   ;;
    p|port      )  PORT="$OPTARG"         ;;
    x|debug     )  DEBUG="true"           ;;
  esac    # --- end of case ---
done
shift $(($OPTIND-1))

if [[ -z $DOMAIN || -z $PORT ]]; then
  usage
  exit 1
fi

mkdir -vp $NGINX_DOMAIN_CONF_PATH
mkdir -vp $NGINX_LOG_PATH/$DOMAIN

NGINX_FILE="$NGINX_DOMAIN_CONF_PATH/${DOMAIN}"

if [[ -f $NGINX_FILE ]]; then
  echo "[WARN] $NGINX_FILE already existed"
  exit 1
fi

if [[ -z $PROXY_NAME ]]; then
	PROXY_NAME=`echo $DOMAIN|sed 's/\.\(7fresh\|jd\)\.\(net\|com\)//g'`
fi

NGINX_CONTENT=`$MO $TEMPLATE_FILE`

if [[ $DEBUG == "true" ]]; then
  echo "$NGINX_CONTENT"
  exit 0
fi

echo "$NGINX_CONTENT" > $NGINX_FILE
echo "add nginx content to $NGINX_FILE success"
