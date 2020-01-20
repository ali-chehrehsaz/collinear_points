#!/bin/bash

counter=1
while [ $counter -le 1000 ]
  do
    echo $counter
    ((counter++))
    pytest tests/oop_dataclass -s -p no:warnings --cov=.
    sleep 5
  done
echo 1000 test cycle Completed
osascript -e 'display notification "1000 test cycle Completed"'
