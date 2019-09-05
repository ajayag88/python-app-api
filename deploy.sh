#!/bin/sh
export FLASK_APP=./endpoint/bank-1.py
flask run -h 172.16.40.241 -p 5003
