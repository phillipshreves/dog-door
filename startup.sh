#!/bin/sh
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>jack-door.log 2>&1
sleep 30
echo "Jack-door starting..."
sudo python3 main_reader.py
