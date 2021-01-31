#!/bin/bash

if [ $# -ne 3 ]
  then
    echo "Usage: ./run_atomic <executable> <input_file_path> <output_file_path>"
    exit 1
fi

timeout 300 $1 < $2 &>/dev/null 
if [ $? -ne 0 ]; then
    exit 1
fi

mkdir -p "$(dirname "$3")"
((/usr/bin/time -v "$1" < "$2") > /dev/null) >"$3" 2>&1


