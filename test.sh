#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

cd $DIR

PROMPT="$1"

TEMPERATURE=1.35 # min:0, max:1.5

TOP_P=0.97 # min:0.8, max:0.99

REPETITION_PENALTY=1.1 # min:1, max:1.5

BATCH_SIZE=3 # min:1, max:3

MAX_LENGTH=512 # min:256, max:2048

python test.py -- "$PROMPT" "$TEMPERATURE" "$TOP_P" "$REPETITION_PENALTY" "$BATCH_SIZE" "$MAX_LENGTH" 
