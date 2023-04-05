#!/bin/bash

while true; do
    nc -l -p 443 | while read line; do
        echo "Received message: $line"
    done
done
