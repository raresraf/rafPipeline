#!/bin/bash

if [ $# -ne 3 ]
  then
    echo "Usage: ./run_atomic <executable> <input_file_path> <output_file_path>"
fi


((/usr/bin/time -v "$1" < "$2") > /dev/null) >"$3" 2>&1

