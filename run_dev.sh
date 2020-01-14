#!bin/bash

watchmedo auto-restart --recursive --patterns="*.py" -- python src/api.py