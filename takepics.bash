#!/bin/bash

cd /home/pi/burst
/home/pi/.local/bin/uv run burst.py >> cronlog.txt 2>&1
