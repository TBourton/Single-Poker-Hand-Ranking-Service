#!/bin/bash

python -m pip install -r requirements.txt
python -m pip install requests

cd solution

uvicorn app:app &
app_pid=$!
sleep 1

cd ..

python3 query.py


echo ${app_pid}
kill ${app_pid}

sleep 0.2
