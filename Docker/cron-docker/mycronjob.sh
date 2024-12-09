#!/bin/bash
# This is my cron job script
* * * * * echo "Hello from cron job" >> /var/log/cron.log 2>&1
