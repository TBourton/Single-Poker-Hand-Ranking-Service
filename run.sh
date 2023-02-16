#!/bin/bash

python -m pip install -r requirements.txt
python -m pip install requests

cd solution

uvicorn --log-level=critical app:app &
app_pid=$!
sleep 1

cd ..

python3 query.py


kill $app_pid
wait $app_pid 2>/dev/null
