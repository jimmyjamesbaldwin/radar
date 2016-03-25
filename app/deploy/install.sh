#!/bin/bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root!" 1>&2
   exit 1
fi

wget https://bootstrap.pypa.io/get-pip.py
chmod +x get-pip.py
python get-pip.py
rm get-pip.py
pip install Flask flask_sqlalchemy flask_table flask-script boto boto3 python-digitalocean
echo ''
echo '*** dependency install complete ***'